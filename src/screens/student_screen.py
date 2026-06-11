import streamlit as st

from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard

from PIL import Image
import numpy as np
import time

from src.pipelines.face_pipeline import (
    predict_attendance,
    get_face_embeddings,
    train_classifier
)

from src.database.db import (
    get_all_students,
    create_student,
    get_student_subjects,
    get_student_attendance,
    unenroll_student_to_subject
)

from src.components.dialog_enroll import enroll_dialog
from src.components.subject_card import subject_card


def student_dashboard():
    student_data = st.session_state.student_data
    student_id = student_data["student_id"]

    c1, c2 = st.columns([1.2, 1], vertical_alignment="center", gap="large")

    with c1:
        header_dashboard()

    with c2:
        st.html(
            f"""
            <div style="
                background:rgba(15, 15, 22, 0.72);
                border:1px solid rgba(124, 58, 237, 0.24);
                border-radius:1.4rem;
                padding:1.1rem 1.2rem;
                text-align:right;
                box-shadow:0 18px 45px rgba(0,0,0,0.28);
                backdrop-filter:blur(16px);
            ">
                <div style="
                    color:#a1a1aa;
                    font-size:0.82rem;
                    font-weight:800;
                    margin-bottom:0.25rem;
                ">
                    STUDENT DASHBOARD
                </div>

                <div style="
                    color:#ffffff;
                    font-size:1.35rem;
                    font-weight:800;
                    letter-spacing:-0.025em;
                ">
                    Welcome, {student_data["name"]}
                </div>
            </div>
            """
        )

        if st.button(
            "Logout",
            type="secondary",
            key="student_logout_btn",
            width="stretch"
        ):
            st.session_state["is_logged_in"] = False
            del st.session_state.student_data
            st.rerun()

    st.html("<div style='height:1rem;'></div>")

    with st.spinner("Loading your enrolled subjects..."):
        subjects = get_student_subjects(student_id)
        logs = get_student_attendance(student_id)

    stats_map = {}

    for log in logs:
        sid = log["subject_id"]

        if sid not in stats_map:
            stats_map[sid] = {"total": 0, "attended": 0}

        stats_map[sid]["total"] += 1

        if log.get("is_present"):
            stats_map[sid]["attended"] += 1

    total_subjects = len(subjects)
    total_classes = len(logs)
    total_attended = sum(1 for log in logs if log.get("is_present"))
    attendance_percent = round((total_attended / total_classes) * 100, 1) if total_classes else 0

    st.html(
        f"""
        <div style="
            display:grid;
            grid-template-columns:repeat(auto-fit, minmax(180px, 1fr));
            gap:1rem;
            margin:1.2rem 0 1.7rem 0;
        ">
            <div class="markmate-card">
                <div style="color:#a1a1aa; font-size:0.85rem; font-weight:800;">Enrolled Subjects</div>
                <div style="color:#ffffff; font-size:2rem; font-weight:800; margin-top:0.35rem;">{total_subjects}</div>
            </div>

            <div class="markmate-card">
                <div style="color:#a1a1aa; font-size:0.85rem; font-weight:800;">Classes Attended</div>
                <div style="color:#ffffff; font-size:2rem; font-weight:800; margin-top:0.35rem;">{total_attended}</div>
            </div>

            <div class="markmate-card">
                <div style="color:#a1a1aa; font-size:0.85rem; font-weight:800;">Total Classes</div>
                <div style="color:#ffffff; font-size:2rem; font-weight:800; margin-top:0.35rem;">{total_classes}</div>
            </div>

            <div class="markmate-card">
                <div style="color:#a1a1aa; font-size:0.85rem; font-weight:800;">Attendance</div>
                <div style="color:#ffffff; font-size:2rem; font-weight:800; margin-top:0.35rem;">{attendance_percent}%</div>
            </div>
        </div>
        """
    )

    c1, c2 = st.columns([1.4, 0.8], vertical_alignment="center")

    with c1:
        st.html(
            """
            <div>
                <div style="
                    font-size:2rem;
                    font-weight:800;
                    letter-spacing:-0.025em;
                    color:#ffffff;
                ">
                    Your Enrolled Subjects
                </div>

                <div style="
                    color:#a1a1aa;
                    font-size:0.95rem;
                    font-weight:600;
                    margin-top:0.25rem;
                ">
                    Track your subject-wise attendance and enrolled courses.
                </div>
            </div>
            """
        )

    with c2:
        if st.button(
            "Enroll in Subject",
            type="primary",
            width="stretch",
            key="student_enroll_subject_btn"
        ):
            enroll_dialog()

    st.divider()

    if not subjects:
        st.html(
            """
            <div class="markmate-card" style="text-align:center; padding:2rem;">
                <div style="color:#ffffff; font-size:1.3rem; font-weight:800; margin-top:0.5rem;">
                    No subjects enrolled yet
                </div>

                <div style="color:#a1a1aa; margin-top:0.35rem;">
                    Click on Enroll in Subject to join a course.
                </div>
            </div>
            """
        )
    else:
        cols = st.columns(2)

        for i, sub_node in enumerate(subjects):
            sub = sub_node["subjects"]
            sid = sub["subject_id"]

            stats = stats_map.get(sid, {"total": 0, "attended": 0})

            def unenroll_button(subject_id=sid, subject_name=sub["name"]):
                if st.button(
                    "Unenroll from this course",
                    type="tertiary",
                    width="stretch",
                    key=f"student_unenroll_{subject_id}"
                ):
                    unenroll_student_to_subject(student_id, subject_id)
                    st.toast(f"Unenrolled from {subject_name} successfully!")
                    st.rerun()

            with cols[i % 2]:
                subject_card(
                    name=sub["name"],
                    code=sub["subject_code"],
                    section=sub["section"],
                    stats=[
                        ("Total", "Classes", stats["total"]),
                        ("Attended", "Present", stats["attended"]),
                    ],
                    footer_callback=unenroll_button
                )

    footer_dashboard()


def student_screen():
    style_background_dashboard()
    style_base_layout()

    if "student_data" in st.session_state:
        student_dashboard()
        return

    c1, c2 = st.columns([1.2, 0.8], vertical_alignment="center", gap="large")

    with c1:
        header_dashboard()

    with c2:
        if st.button(
            "Go back to Home",
            type="secondary",
            key="student_login_back_btn",
            width="stretch"
        ):
            st.session_state["login_type"] = None
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
                FaceID Login
            </div>

            <div style="
                color:#ffffff;
                font-size:2.3rem;
                font-weight:800;
                letter-spacing:-0.025em;
                line-height:1.08;
            ">
                Login using FaceID
            </div>

            <div style="
                color:#a1a1aa;
                font-size:1rem;
                font-weight:600;
                margin-top:0.45rem;
            ">
                Position your face clearly in the camera frame.
            </div>
        </div>
        """
    )

    show_registration = False

    with st.container(border=True):
        photo_source = st.camera_input("Position your face in the center")

    if photo_source:
        img = np.array(Image.open(photo_source).convert("RGB"), dtype=np.uint8)

        with st.spinner("AI is scanning..."):
            detected, all_ids, num_faces = predict_attendance(img)

            if num_faces == 0:
                st.warning("Face not found!")
            elif num_faces > 1:
                st.warning("Multiple faces found")
            else:
                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    student = next(
                        (s for s in all_students if s["student_id"] == student_id),
                        None
                    )

                    if student:
                        st.session_state.is_logged_in = True
                        st.session_state.user_role = "student"
                        st.session_state.student_data = student
                        st.toast(f"Welcome Back {student['name']}")
                        time.sleep(1)
                        st.rerun()
                else:
                    st.info("Face not recognized! You might be a new student.")
                    show_registration = True

    if show_registration:
        st.html("<div style='height:1rem;'></div>")

        with st.container(border=True):
            st.html(
                """
                <div style="margin-bottom:1rem;">
                    <div style="
                        color:#ffffff;
                        font-size:1.55rem;
                        font-weight:800;
                        letter-spacing:-0.025em;
                    ">
                        Register New Profile
                    </div>

                    <div style="
                        color:#a1a1aa;
                        font-size:0.95rem;
                        font-weight:600;
                        margin-top:0.25rem;
                    ">
                        Create your MarkMate student profile using FaceID.
                    </div>
                </div>
                """
            )

            new_name = st.text_input(
                "Enter your name",
                placeholder="E.g. Harshita Singhal"
            )

            if st.button(
                "Create Account",
                type="primary",
                width="stretch",
                key="student_create_account_btn"
            ):
                if new_name:
                    with st.spinner("Creating profile..."):
                        img = np.array(Image.open(photo_source).convert("RGB"), dtype=np.uint8)
                        encodings = get_face_embeddings(img)

                        if encodings:
                            face_emb = encodings[0].tolist()

                            response_data = create_student(
                                new_name,
                                face_embedding=face_emb
                            )

                            if response_data:
                                train_classifier()

                                st.session_state.is_logged_in = True
                                st.session_state.user_role = "student"
                                st.session_state.student_data = response_data[0]

                                st.toast(f"Profile Created! Hi {new_name}!")

                                time.sleep(1)
                                st.rerun()
                        else:
                            st.error("Could not capture your facial features for registration.")
                else:
                    st.warning("Please enter your name!")

    footer_dashboard()