import streamlit as st

from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home


def home_screen():
    style_background_home()
    style_base_layout()

    header_home()

    st.html(
        """
        <div class="premium-shell">
            <div class="premium-orb"></div>

            <div style="position:relative; z-index:2;">
                <div class="premium-pill">Face Recognition Attendance System</div>

                <div class="premium-title">
                    Attendance made <span class="gradient-text">intelligent.</span>
                </div>

                <div class="premium-subtitle">
                    MarkMate helps students check in using FaceID and helps teachers manage attendance records with a clean AI-powered workflow.
                </div>

                <div class="stat-row">
                    <div class="stat-card">
                        <div class="stat-value">AI</div>
                        <div class="stat-label">Face Recognition</div>
                    </div>

                    <div class="stat-card">
                        <div class="stat-value">Fast</div>
                        <div class="stat-label">Attendance Marking</div>
                    </div>

                    <div class="stat-card">
                        <div class="stat-value">Smart</div>
                        <div class="stat-label">Class Records</div>
                    </div>
                </div>
            </div>
        </div>
        """,
    )

    st.html("<div style='height:1.4rem;'></div>")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.html(
            """
            <div>
                <div class="role-icon">🎓</div>
                <div class="role-title">Student Portal</div>
                <div class="role-desc">
                    Login with FaceID, enroll in subjects, and track your attendance in one place.
                </div>
            </div>
            """,
        )

        if st.button(
            "Continue as Student",
            type="primary",
            width="stretch",
            key="home_student_portal"
        ):
            st.session_state["login_type"] = "student"
            st.rerun()

    with col2:
        st.html(
            """
            <div>
                <div class="role-icon">🧑🏻‍🏫</div>
                <div class="role-title">Teacher Portal</div>
                <div class="role-desc">
                    Create subjects, upload class photos, run AI analysis, and view attendance records.
                </div>
            </div>
            """,
        )

        if st.button(
            "Continue as Teacher",
            type="primary",
            width="stretch",
            key="home_teacher_portal"
        ):
            st.session_state["login_type"] = "teacher"
            st.rerun()

    footer_home()