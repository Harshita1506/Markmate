import streamlit as st

from src.ui.base_layout import style_background_dashboard, style_base_layout

from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.components.subject_card import subject_card
from src.database.db import (
    check_teacher_exists,
    create_teacher,
    teacher_login,
    get_teacher_subjects,
    get_attendance_for_teacher
)
from src.components.dialog_create_subject import create_subject_dialog
from src.components.dialog_share_subject import share_subject_dialog
from src.components.dialog_add_photo import add_photos_dialog

from src.pipelines.face_pipeline import predict_attendance
from src.components.dialog_attendance_results import attendance_result_dialog
import numpy as np

from datetime import datetime

import pandas as pd

from src.database.config import supabase


# from src.components.dialog_voice_attendance_old import voice_attendance_dialog


def teacher_screen():
    style_background_dashboard()
    style_base_layout()

    if "teacher_data" in st.session_state:
        teacher_dashboard()
    elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type == "login":
        teacher_screen_login()
    elif st.session_state.teacher_login_type == "register":
        teacher_screen_register()


def teacher_dashboard():
    teacher_data = st.session_state.teacher_data

    c1, c2 = st.columns([1.2, 1], vertical_alignment='center', gap='large')

    with c1:
        header_dashboard()

    with c2:
        st.html(
            f"""
            <div style="
                background:rgba(17, 17, 22, 0.72);
                border:1px solid rgba(124, 58, 237, 0.22);
                border-radius:1.4rem;
                padding:1.1rem 1.2rem;
                text-align:right;
                box-shadow:0 18px 45px rgba(0,0,0,0.28);
            ">
                <div style="
                    color:#a1a1aa;
                    font-size:0.85rem;
                    font-weight:800;
                    margin-bottom:0.25rem;
                ">
                    TEACHER DASHBOARD
                </div>
                <div style="
                    color:#ffffff;
                    font-size:1.35rem;
                    font-weight:900;
                    letter-spacing:-0.04em;
                ">
                    Welcome, {teacher_data['name']}
                </div>
            </div>
            """
        )

        if st.button(
            "Logout",
            type='secondary',
            key='teacher_logout_btn',
            width='stretch'
        ):
            st.session_state['is_logged_in'] = False
            del st.session_state.teacher_data
            st.rerun()

    st.html("<div style='height:1rem;'></div>")

    if "current_teacher_tab" not in st.session_state:
        st.session_state.current_teacher_tab = 'take_attendance'

    tab1, tab2, tab3 = st.columns(3)

    with tab1:
        type1 = "primary" if st.session_state.current_teacher_tab == 'take_attendance' else "tertiary"
        if st.button(
            'Take Attendance',
            type=type1,
            width='stretch',
            key='teacher_tab_take_attendance'
        ):
            st.session_state.current_teacher_tab = 'take_attendance'
            st.rerun()

    with tab2:
        type2 = "primary" if st.session_state.current_teacher_tab == 'manage_subjects' else "tertiary"
        if st.button(
            'Manage Subjects',
            type=type2,
            width='stretch',
            key='teacher_tab_manage_subjects'
        ):
            st.session_state.current_teacher_tab = 'manage_subjects'
            st.rerun()

    with tab3:
        type3 = "primary" if st.session_state.current_teacher_tab == 'attendance_records' else "tertiary"
        if st.button(
            'Attendance Records',
            type=type3,
            width='stretch',
            key='teacher_tab_attendance_records'
        ):
            st.session_state.current_teacher_tab = 'attendance_records'
            st.rerun()

    st.divider()

    if st.session_state.current_teacher_tab == "take_attendance":
        teacher_tab_take_attendance()

    if st.session_state.current_teacher_tab == "manage_subjects":
        teacher_tab_manage_subjects()

    if st.session_state.current_teacher_tab == "attendance_records":
        teacher_tab_attendance_records()

    footer_dashboard()


def teacher_tab_take_attendance():
    teacher_id = st.session_state.teacher_data['teacher_id']

    st.html(
        """
        <div style="margin-bottom:1.2rem;">
            <div style="
                display:inline-flex;
                align-items:center;
                gap:0.45rem;
                padding:0.4rem 0.85rem;
                border-radius:999px;
                background:rgba(124, 58, 237, 0.16);
                border:1px solid rgba(124, 58, 237, 0.34);
                color:#c4b5fd;
                font-size:0.85rem;
                font-weight:800;
                margin-bottom:0.8rem;
            ">
                ✨ AI Attendance
            </div>

            <div style="
                color:#ffffff;
                font-size:2.2rem;
                font-weight:900;
                letter-spacing:-0.06em;
                line-height:1.05;
            ">
                Take AI Attendance
            </div>

            <div style="
                color:#a1a1aa;
                font-size:1rem;
                font-weight:600;
                margin-top:0.45rem;
            ">
                Upload classroom photos and let MarkMate detect enrolled students automatically.
            </div>
        </div>
        """
    )

    if 'attendance_images' not in st.session_state:
        st.session_state.attendance_images = []

    subjects = get_teacher_subjects(teacher_id)

    if not subjects:
        st.warning('You havent created any subjects yet! Please create one to begin!')
        return

    subject_options = {
        f"{s['name']} - {s['subject_code']}": s['subject_id']
        for s in subjects
    }

    col1, col2 = st.columns([3, 1], vertical_alignment='bottom')

    with col1:
        selected_subject_label = st.selectbox(
            'Select Subject',
            options=list(subject_options.keys())
        )

    with col2:
        if st.button(
            'Add Photos',
            type='primary',
            width='stretch',
            key='teacher_add_photos_btn'
        ):
            add_photos_dialog()

    selected_subject_id = subject_options[selected_subject_label]

    st.divider()

    if st.session_state.attendance_images:
        st.html(
            """
            <div style="
                color:#ffffff;
                font-size:1.45rem;
                font-weight:900;
                letter-spacing:-0.04em;
                margin-bottom:0.8rem;
            ">
                Added Photos
            </div>
            """
        )

        gallery_cols = st.columns(4)

        for idx, img in enumerate(st.session_state.attendance_images):
            with gallery_cols[idx % 4]:
                st.image(img, width='stretch', caption=f'Photo {idx + 1}')

    has_photos = bool(st.session_state.attendance_images)

    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button(
            'Clear all photos',
            width='stretch',
            type='tertiary',
            disabled=not has_photos,
            key='teacher_clear_photos_btn'
        ):
            st.session_state.attendance_images = []
            st.rerun()

    with c2:
        if st.button(
            'Run Face Analysis',
            width='stretch',
            type='secondary',
            disabled=not has_photos,
            key='teacher_run_face_analysis_btn'
        ):
            with st.spinner('Deep scanning classroom photos...'):
                all_detected_ids = {}

                for idx, img in enumerate(st.session_state.attendance_images):
                    img_np = np.array(img.convert('RGB'))
                    detected, _, _ = predict_attendance(img_np)

                    if detected:
                        for sid in detected.keys():
                            student_id = int(sid)
                            all_detected_ids.setdefault(student_id, []).append(f"Photo {idx + 1}")

                enrolled_res = (
                    supabase
                    .table('subject_students')
                    .select("*, students(*)")
                    .eq('subject_id', selected_subject_id)
                    .execute()
                )

                enrolled_students = enrolled_res.data

                if not enrolled_students:
                    st.warning('No students enrolled in this course')
                else:
                    results, attendance_to_log = [], []

                    current_timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

                    for node in enrolled_students:
                        student = node['students']
                        sources = all_detected_ids.get(int(student['student_id']), [])
                        is_present = len(sources) > 0

                        results.append({
                            "Name": student['name'],
                            "ID": student['student_id'],
                            "Source": ", ".join(sources) if is_present else "-",
                            "Status": "✅ Present" if is_present else "❌ Absent"
                        })

                        attendance_to_log.append({
                            'student_id': student['student_id'],
                            'subject_id': selected_subject_id,
                            'timestamp': current_timestamp,
                            'is_present': bool(is_present)
                        })

                    attendance_result_dialog(pd.DataFrame(results), attendance_to_log)

    with c3:
        st.html(
            """
            <div style="
                background:rgba(17, 17, 22, 0.72);
                border:1px solid rgba(124, 58, 237, 0.18);
                border-radius:1rem;
                padding:0.85rem;
                text-align:center;
                color:#a1a1aa;
                font-size:0.85rem;
                font-weight:700;
            ">
                📷 Add photos first
            </div>
            """
        )


def teacher_tab_manage_subjects():
    teacher_id = st.session_state.teacher_data['teacher_id']

    col1, col2 = st.columns([1.4, 0.8], vertical_alignment='center')

    with col1:
        st.html(
            """
            <div>
                <div style="
                    font-size:2rem;
                    font-weight:900;
                    letter-spacing:-0.05em;
                    color:#ffffff;
                ">
                    Manage Subjects
                </div>
                <div style="
                    color:#a1a1aa;
                    font-size:0.95rem;
                    font-weight:600;
                    margin-top:0.25rem;
                ">
                    Create, share, and track your active subject sections.
                </div>
            </div>
            """
        )

    with col2:
        if st.button(
            'Create New Subject',
            width='stretch',
            type='primary',
            key='teacher_create_subject_btn'
        ):
            create_subject_dialog(teacher_id)

    st.html("<div style='height:1rem;'></div>")

    subjects = get_teacher_subjects(teacher_id)

    if subjects:
        total_subjects = len(subjects)
        total_students = sum(sub.get('total_students', 0) for sub in subjects)
        total_classes = sum(sub.get('total_classes', 0) for sub in subjects)

        st.html(
            f"""
            <div style="
                display:grid;
                grid-template-columns:repeat(auto-fit, minmax(180px, 1fr));
                gap:1rem;
                margin:1rem 0 1.5rem 0;
            ">
                <div class="markmate-card">
                    <div style="color:#a1a1aa; font-size:0.85rem; font-weight:800;">📚 Subjects</div>
                    <div style="color:#ffffff; font-size:2rem; font-weight:900; margin-top:0.35rem;">{total_subjects}</div>
                </div>

                <div class="markmate-card">
                    <div style="color:#a1a1aa; font-size:0.85rem; font-weight:800;">🫂 Students</div>
                    <div style="color:#ffffff; font-size:2rem; font-weight:900; margin-top:0.35rem;">{total_students}</div>
                </div>

                <div class="markmate-card">
                    <div style="color:#a1a1aa; font-size:0.85rem; font-weight:800;">🕰️ Classes</div>
                    <div style="color:#ffffff; font-size:2rem; font-weight:900; margin-top:0.35rem;">{total_classes}</div>
                </div>
            </div>
            """
        )

        cols = st.columns(2)

        for i, sub in enumerate(subjects):
            stats = [
                ("🫂", "Students", sub['total_students']),
                ("🕰️", "Classes", sub['total_classes']),
            ]

            def share_btn(subject_name=sub['name'], subject_code=sub['subject_code']):
                if st.button(
                    f"Share Code: {subject_code}",
                    key=f"teacher_share_{subject_code}",
                    width='stretch',
                    type='secondary'
                ):
                    share_subject_dialog(subject_name, subject_code)

            with cols[i % 2]:
                subject_card(
                    name=sub['name'],
                    code=sub['subject_code'],
                    section=sub['section'],
                    stats=stats,
                    footer_callback=share_btn
                )
    else:
        st.html(
            """
            <div class="markmate-card" style="text-align:center; padding:2rem;">
                <div style="font-size:2.3rem;">📭</div>
                <div style="color:#ffffff; font-size:1.3rem; font-weight:900; margin-top:0.5rem;">
                    No subjects found
                </div>
                <div style="color:#a1a1aa; margin-top:0.35rem;">
                    Create a new subject to begin taking attendance.
                </div>
            </div>
            """
        )


def teacher_tab_attendance_records():
    st.html(
        """
        <div style="margin-bottom:1rem;">
            <div style="
                font-size:2rem;
                font-weight:900;
                letter-spacing:-0.05em;
                color:#ffffff;
            ">
                Attendance Records
            </div>
            <div style="
                color:#a1a1aa;
                font-size:0.95rem;
                font-weight:600;
                margin-top:0.25rem;
            ">
                View previously marked attendance sessions.
            </div>
        </div>
        """
    )

    teacher_id = st.session_state.teacher_data['teacher_id']

    records = get_attendance_for_teacher(teacher_id)

    if not records:
        st.html(
            """
            <div class="markmate-card" style="text-align:center; padding:2rem;">
                <div style="font-size:2.3rem;">🗂️</div>
                <div style="color:#ffffff; font-size:1.3rem; font-weight:900; margin-top:0.5rem;">
                    No attendance records yet
                </div>
                <div style="color:#a1a1aa; margin-top:0.35rem;">
                    Attendance sessions will appear here after analysis.
                </div>
            </div>
            """
        )
        return

    data = []

    for r in records:
        ts = r.get('timestamp')

        data.append({
            "ts_group": ts.split(".")[0] if ts else None,
            "Time": datetime.fromisoformat(ts).strftime("%Y-%m-%d %I:%M %p") if ts else "N/A",
            "Subject": r['subjects']['name'],
            "Subject Code": r['subjects']['subject_code'],
            "is_present": bool(r.get('is_present', False))
        })

    df = pd.DataFrame(data)

    summary = (
        df.groupby(['ts_group', 'Time', 'Subject', 'Subject Code'])
        .agg(
            Present_Count=('is_present', 'sum'),
            Total_Count=('is_present', 'count')
        )
        .reset_index()
    )

    summary['Attendance Stats'] = (
        "✅ " + summary['Present_Count'].astype(str) + " / "
        + summary['Total_Count'].astype(str) + ' Students'
    )

    display_df = (
        summary.sort_values(by='ts_group', ascending=False)
        [['Time', 'Subject', 'Subject Code', 'Attendance Stats']]
    )

    st.dataframe(display_df, width='stretch', hide_index=True)


def login_teacher(username, password):
    if not username or not password:
        return False

    teacher = teacher_login(username, password)

    if teacher:
        st.session_state.user_role = 'teacher'
        st.session_state.teacher_data = teacher
        st.session_state.is_logged_in = True
        return True

    return False


def teacher_screen_login():
    c1, c2 = st.columns([1.2, 0.8], vertical_alignment='center', gap='large')

    with c1:
        header_dashboard()

    with c2:
        if st.button(
            "Go back to Home",
            type='secondary',
            key='teacher_login_back_btn',
            width='stretch'
        ):
            st.session_state['login_type'] = None
            st.rerun()

    st.html(
        """
        <div style="
            margin:1.6rem 0 1.2rem 0;
            text-align:center;
        ">
            <div style="
                display:inline-flex;
                align-items:center;
                gap:0.45rem;
                padding:0.4rem 0.85rem;
                border-radius:999px;
                background:rgba(124, 58, 237, 0.16);
                border:1px solid rgba(124, 58, 237, 0.34);
                color:#c4b5fd;
                font-size:0.85rem;
                font-weight:800;
                margin-bottom:0.8rem;
            ">
                🔐 Teacher Login
            </div>

            <div style="
                color:#ffffff;
                font-size:2.3rem;
                font-weight:900;
                letter-spacing:-0.06em;
                line-height:1.05;
            ">
                Login using password
            </div>

            <div style="
                color:#a1a1aa;
                font-size:1rem;
                font-weight:600;
                margin-top:0.45rem;
            ">
                Access your MarkMate teacher dashboard.
            </div>
        </div>
        """
    )

    with st.container(border=True):
        teacher_username = st.text_input("Enter username", placeholder='Enter username')

        teacher_pass = st.text_input("Enter password", type='password', placeholder="Enter password")

        st.divider()

        btnc1, btnc2 = st.columns(2)

        with btnc1:
            if st.button(
                'Login',
                width='stretch',
                key='teacher_login_btn'
            ):
                if login_teacher(teacher_username, teacher_pass):
                    st.toast("Welcome back!", icon="👋")
                    import time
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("Invalid username and password combo")

        with btnc2:
            if st.button(
                'Register Instead',
                type="primary",
                width='stretch',
                key='teacher_go_register_btn'
            ):
                st.session_state.teacher_login_type = 'register'
                st.rerun()

    footer_dashboard()


def register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm):
    if not teacher_username or not teacher_name or not teacher_pass:
        return False, "All Fields are required!"

    if check_teacher_exists(teacher_username):
        return False, "Username already taken"

    if teacher_pass != teacher_pass_confirm:
        return False, "Password doesn't match"

    try:
        create_teacher(teacher_username, teacher_pass, teacher_name)
        return True, "Sucessfully Created! Login Now"
    except Exception:
        return False, "Unexpected Error!"


def teacher_screen_register():
    c1, c2 = st.columns([1.2, 0.8], vertical_alignment='center', gap='large')

    with c1:
        header_dashboard()

    with c2:
        if st.button(
            "Go back to Home",
            type='secondary',
            key='teacher_register_back_btn',
            width='stretch'
        ):
            st.session_state['login_type'] = None
            st.rerun()

    st.html(
        """
        <div style="
            margin:1.6rem 0 1.2rem 0;
            text-align:center;
        ">
            <div style="
                display:inline-flex;
                align-items:center;
                gap:0.45rem;
                padding:0.4rem 0.85rem;
                border-radius:999px;
                background:rgba(124, 58, 237, 0.16);
                border:1px solid rgba(124, 58, 237, 0.34);
                color:#c4b5fd;
                font-size:0.85rem;
                font-weight:800;
                margin-bottom:0.8rem;
            ">
                ✨ Teacher Registration
            </div>

            <div style="
                color:#ffffff;
                font-size:2.3rem;
                font-weight:900;
                letter-spacing:-0.06em;
                line-height:1.05;
            ">
                Register your teacher profile
            </div>

            <div style="
                color:#a1a1aa;
                font-size:1rem;
                font-weight:600;
                margin-top:0.45rem;
            ">
                Create your MarkMate account to manage subjects and attendance.
            </div>
        </div>
        """
    )

    with st.container(border=True):
        teacher_username = st.text_input("Enter username", placeholder='Enter username')

        teacher_name = st.text_input("Enter name", placeholder='Enter username')

        teacher_pass = st.text_input("Enter password", type='password', placeholder="Enter password")

        teacher_pass_confirm = st.text_input("Confirm your password", type='password', placeholder="Enter password")

        st.divider()

        btnc1, btnc2 = st.columns(2)

        with btnc1:
            if st.button(
                'Register now',
                width='stretch',
                key='teacher_register_btn'
            ):
                success, message = register_teacher(
                    teacher_username,
                    teacher_name,
                    teacher_pass,
                    teacher_pass_confirm
                )

                if success:
                    st.success(message)
                    import time
                    time.sleep(2)
                    st.session_state.teacher_login_type = "login"
                    st.rerun()
                else:
                    st.error(message)

        with btnc2:
            if st.button(
                'Login Instead',
                type="primary",
                width='stretch',
                key='teacher_go_login_btn'
            ):
                st.session_state.teacher_login_type = 'login'
                st.rerun()

    footer_dashboard()