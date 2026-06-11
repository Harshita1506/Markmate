import streamlit as st

from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen
from src.components.dialog_auto_enroll import auto_enroll_dialog


def apply_global_dark_ui():
    st.markdown(
        """
        <style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700;800&display=swap');
        :root {
            --bg: #030305;
            --panel: rgba(15, 15, 22, 0.78);
            --panel-strong: rgba(20, 20, 30, 0.92);
            --purple: #7c3aed;
            --purple-light: #a78bfa;
            --purple-soft: rgba(124, 58, 237, 0.18);
            --text: #ffffff;
            --muted: #a1a1aa;
            --border: rgba(255, 255, 255, 0.1);
            --border-purple: rgba(124, 58, 237, 0.35);
        }

        html, body, [data-testid="stAppViewContainer"], .stApp {
            background:
                radial-gradient(circle at 12% 8%, rgba(124, 58, 237, 0.32), transparent 28%),
                radial-gradient(circle at 88% 22%, rgba(167, 139, 250, 0.13), transparent 24%),
                radial-gradient(circle at 50% 100%, rgba(124, 58, 237, 0.18), transparent 32%),
                linear-gradient(135deg, #020203 0%, #07070b 45%, #111118 100%) !important;
            color: var(--text) !important;
            font-family: 'Sora', sans-serif !important;
        }

        [data-testid="stHeader"] {
            background: transparent !important;
        }

        [data-testid="stToolbar"],
        #MainMenu,
        footer {
            display: none !important;
        }

        .block-container {
            max-width: 1220px !important;
            padding-top: 2rem !important;
            padding-bottom: 2rem !important;
        }

        * {
            font-family: 'Sora', sans-serif !important;
        }

       h1, h2, h3, h4, h5, h6 {
    color: white !important;
    font-weight: 800 !important;
    letter-spacing: -0.025em !important;
}

        label {
            color: var(--muted) !important;
            font-weight: 700 !important;
        }

        .stButton > button {
            background: linear-gradient(135deg, #8b5cf6, #6d28d9) !important;
            color: white !important;
            border: 1px solid rgba(196, 181, 253, 0.45) !important;
            border-radius: 999px !important;
            font-weight: 800 !important;
            padding: 0.78rem 1.35rem !important;
            box-shadow:
                0 0 28px rgba(124, 58, 237, 0.35),
                inset 0 1px 0 rgba(255, 255, 255, 0.18) !important;
            transition: all 0.22s ease-in-out !important;
        }

        .stButton > button:hover {
            transform: translateY(-2px) scale(1.015) !important;
            box-shadow:
                0 0 42px rgba(124, 58, 237, 0.62),
                inset 0 1px 0 rgba(255, 255, 255, 0.24) !important;
            border-color: rgba(221, 214, 254, 0.85) !important;
        }

        button[kind="secondary"] {
            background: rgba(20, 20, 30, 0.9) !important;
            color: white !important;
            border: 1px solid rgba(124, 58, 237, 0.45) !important;
            box-shadow: none !important;
        }

        button[kind="tertiary"] {
            background: rgba(8, 8, 12, 0.92) !important;
            color: white !important;
            border: 1px solid rgba(255, 255, 255, 0.12) !important;
            box-shadow: none !important;
        }

        [data-testid="column"] {
            background: rgba(15, 15, 22, 0.72) !important;
            border: 1px solid rgba(124, 58, 237, 0.24) !important;
            border-radius: 2rem !important;
            padding: 2rem !important;
            box-shadow:
                0 24px 70px rgba(0, 0, 0, 0.48),
                inset 0 1px 0 rgba(255, 255, 255, 0.05) !important;
            backdrop-filter: blur(18px) !important;
        }

        [data-testid="column"]:hover {
            border-color: rgba(167, 139, 250, 0.55) !important;
            box-shadow:
                0 24px 80px rgba(0, 0, 0, 0.55),
                0 0 38px rgba(124, 58, 237, 0.2),
                inset 0 1px 0 rgba(255, 255, 255, 0.08) !important;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            background: rgba(15, 15, 22, 0.82) !important;
            border: 1px solid rgba(124, 58, 237, 0.28) !important;
            border-radius: 1.7rem !important;
            box-shadow: 0 24px 70px rgba(0, 0, 0, 0.48) !important;
            backdrop-filter: blur(18px) !important;
        }

        .stTextInput input,
        .stTextArea textarea,
        .stSelectbox div[data-baseweb="select"] > div {
            background: rgba(15, 15, 22, 0.95) !important;
            color: white !important;
            border: 1px solid rgba(255, 255, 255, 0.12) !important;
            border-radius: 1rem !important;
        }

        [data-testid="stCameraInput"],
        [data-testid="stFileUploader"] {
            background: rgba(15, 15, 22, 0.82) !important;
            border: 1px solid rgba(124, 58, 237, 0.28) !important;
            border-radius: 1.5rem !important;
            padding: 1.2rem !important;
        }

        .stAlert {
            background: rgba(15, 15, 22, 0.96) !important;
            color: white !important;
            border: 1px solid rgba(124, 58, 237, 0.28) !important;
            border-radius: 1rem !important;
        }

        hr {
            border-color: rgba(255, 255, 255, 0.08) !important;
        }

        .premium-shell {
            position: relative;
            overflow: hidden;
            border-radius: 2.2rem;
            padding: 2.2rem;
            background:
                linear-gradient(135deg, rgba(255,255,255,0.08), rgba(255,255,255,0.025)),
                rgba(15, 15, 22, 0.78);
            border: 1px solid rgba(124, 58, 237, 0.28);
            box-shadow:
                0 30px 90px rgba(0, 0, 0, 0.55),
                inset 0 1px 0 rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(22px);
        }

        .premium-orb {
            position: absolute;
            width: 220px;
            height: 220px;
            border-radius: 999px;
            background: rgba(124, 58, 237, 0.22);
            filter: blur(10px);
            right: -90px;
            top: -90px;
            z-index: 0;
        }

        .premium-pill {
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            padding: 0.42rem 0.9rem;
            border-radius: 999px;
            background: rgba(124, 58, 237, 0.16);
            border: 1px solid rgba(167, 139, 250, 0.35);
            color: #c4b5fd;
            font-size: 0.86rem;
            font-weight: 800;
        }

        .premium-title {
    color: white;
    font-size: clamp(2.7rem, 6vw, 5rem);
    line-height: 1.05;
    font-weight: 800;
    letter-spacing: -0.035em;
    margin-top: 1rem;
    margin-bottom: 1rem;
}

        .gradient-text {
    background: linear-gradient(135deg, #ddd6fe, #a78bfa 45%, #7c3aed);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

        .premium-subtitle {
            color: #a1a1aa;
            font-size: 1.08rem;
            line-height: 1.65;
            max-width: 720px;
            font-weight: 600;
        }

        .stat-row {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 0.85rem;
            margin-top: 1.5rem;
        }

        .stat-card {
            background: rgba(255, 255, 255, 0.045);
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 1.25rem;
            padding: 1rem;
        }

        .stat-value {
            color: white;
            font-size: 1.45rem;
            font-weight: 900;
            letter-spacing: -0.04em;
        }

        .stat-label {
            color: #a1a1aa;
            font-size: 0.78rem;
            font-weight: 700;
            margin-top: 0.2rem;
        }

        .role-icon {
            width: 78px;
            height: 78px;
            margin: 0 auto 1rem auto;
            border-radius: 1.55rem;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, rgba(124, 58, 237, 0.28), rgba(167, 139, 250, 0.12));
            border: 1px solid rgba(167, 139, 250, 0.32);
            box-shadow: 0 0 35px rgba(124, 58, 237, 0.22);
            font-size: 2.45rem;
        }

        .role-title {
            color: white;
            font-size: 1.75rem;
            font-weight: 900;
            letter-spacing: -0.06em;
            text-align: center;
            margin-bottom: 0.45rem;
        }

        .role-desc {
            color: #a1a1aa;
            font-size: 0.95rem;
            font-weight: 600;
            line-height: 1.55;
            text-align: center;
            margin-bottom: 1.3rem;
        }

        ::-webkit-scrollbar {
            width: 8px;
        }

        ::-webkit-scrollbar-track {
            background: #030305;
        }

        ::-webkit-scrollbar-thumb {
            background: #7c3aed;
            border-radius: 999px;
        }
        .icon-svg {
    width: 28px;
    height: 28px;
    stroke: white;
    stroke-width: 2.3;
    stroke-linecap: round;
    stroke-linejoin: round;
    fill: none;
}

.role-icon .icon-svg {
    width: 34px;
    height: 34px;
    stroke: #ffffff;
}
        </style>
        """,
        unsafe_allow_html=True
    )


def main():
    st.set_page_config(
        page_title="MarkMate - AI Attendance System",
        page_icon="✅",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    apply_global_dark_ui()

    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()

        case 'student':
            student_screen()

        case None:
            home_screen()

    join_code = st.query_params.get('join-code')

    if join_code:
        if st.session_state.login_type != 'student':
            st.session_state.login_type = 'student'
            st.rerun()

        if st.session_state.get('is_logged_in') and st.session_state.get('user_role') == 'student':
            auto_enroll_dialog(join_code)


main()