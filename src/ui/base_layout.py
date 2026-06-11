import streamlit as st


def style_background_home():
    st.markdown(
        """
        <style>
            .stApp {
                background:
                    radial-gradient(circle at top left, rgba(124, 58, 237, 0.22), transparent 30%),
                    radial-gradient(circle at bottom right, rgba(124, 58, 237, 0.14), transparent 32%),
                    linear-gradient(135deg, #030303 0%, #08080c 48%, #101014 100%) !important;
                color: #ffffff !important;
            }

                        .stApp div[data-testid="stColumn"] {
                background: transparent !important;
                border: none !important;
                padding: 0rem !important;
                border-radius: 0rem !important;
                box-shadow: none !important;
                backdrop-filter: none !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )


def style_background_dashboard():
    st.markdown(
        """
        <style>
            .stApp {
                background:
                    radial-gradient(circle at top left, rgba(124, 58, 237, 0.16), transparent 30%),
                    radial-gradient(circle at bottom right, rgba(124, 58, 237, 0.10), transparent 35%),
                    linear-gradient(135deg, #030303 0%, #08080c 48%, #101014 100%) !important;
                color: #ffffff !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )


def style_base_layout():
    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

            :root {
                --bg-card: rgba(17, 17, 22, 0.9);
                --bg-card-hover: rgba(24, 24, 31, 0.95);
                --accent: #7c3aed;
                --accent-light: #a78bfa;
                --accent-soft: rgba(124, 58, 237, 0.16);
                --border: rgba(255, 255, 255, 0.09);
                --border-purple: rgba(124, 58, 237, 0.34);
                --text-main: #ffffff;
                --text-muted: #a1a1aa;
            }

            #MainMenu, footer, header {
                visibility: hidden;
            }

            * {
                font-family: 'Outfit', sans-serif !important;
            }

            .block-container {
                padding-top: 1.8rem !important;
                padding-bottom: 2rem !important;
                max-width: 1180px !important;
            }

            h1, h2, h3, h4, h5, h6 {
                color: #ffffff !important;
                font-weight: 900 !important;
                letter-spacing: -0.05em !important;
            }

            p, span, label, div {
                color: #e5e7eb;
            }

            label {
                color: #a1a1aa !important;
                font-weight: 700 !important;
            }

            .stButton > button {
                border-radius: 999px !important;
                background: linear-gradient(135deg, #7c3aed, #6d28d9) !important;
                color: #ffffff !important;
                padding: 0.72rem 1.25rem !important;
                border: 1px solid rgba(167, 139, 250, 0.28) !important;
                font-weight: 800 !important;
                box-shadow: 0 0 24px rgba(124, 58, 237, 0.32) !important;
                transition: all 0.22s ease-in-out !important;
            }

            .stButton > button:hover {
                transform: translateY(-2px) scale(1.015) !important;
                background: linear-gradient(135deg, #8b5cf6, #7c3aed) !important;
                box-shadow: 0 0 36px rgba(124, 58, 237, 0.55) !important;
                border-color: rgba(196, 181, 253, 0.65) !important;
            }

            button[kind="secondary"] {
                background: rgba(24, 24, 31, 0.96) !important;
                color: #ffffff !important;
                border: 1px solid rgba(124, 58, 237, 0.45) !important;
                box-shadow: none !important;
            }

            button[kind="tertiary"] {
                background: rgba(12, 12, 15, 0.92) !important;
                color: #ffffff !important;
                border: 1px solid rgba(255, 255, 255, 0.12) !important;
                box-shadow: none !important;
            }

            .stTextInput input,
            .stTextArea textarea,
            .stSelectbox div[data-baseweb="select"] > div {
                background: rgba(17, 17, 22, 0.96) !important;
                color: #ffffff !important;
                border: 1px solid rgba(255, 255, 255, 0.12) !important;
                border-radius: 1rem !important;
            }

            .stTextInput input:focus,
            .stTextArea textarea:focus {
                border-color: #7c3aed !important;
                box-shadow: 0 0 0 2px rgba(124, 58, 237, 0.28) !important;
            }

            div[data-testid="stVerticalBlockBorderWrapper"] {
                background: rgba(17, 17, 22, 0.9) !important;
                border: 1px solid rgba(124, 58, 237, 0.26) !important;
                border-radius: 1.7rem !important;
                box-shadow: 0 20px 55px rgba(0, 0, 0, 0.38) !important;
                backdrop-filter: blur(16px) !important;
            }

            [data-testid="stCameraInput"],
            [data-testid="stFileUploader"] {
                background: rgba(17, 17, 22, 0.86) !important;
                border: 1px solid rgba(124, 58, 237, 0.24) !important;
                border-radius: 1.5rem !important;
                padding: 1.2rem !important;
            }

            .stAlert {
                background: rgba(17, 17, 22, 0.96) !important;
                border: 1px solid rgba(124, 58, 237, 0.28) !important;
                border-radius: 1rem !important;
                color: #ffffff !important;
            }

            [data-testid="stDataFrame"] {
                border-radius: 1.2rem !important;
                overflow: hidden !important;
                border: 1px solid rgba(124, 58, 237, 0.22) !important;
            }

            hr {
                border-color: rgba(255, 255, 255, 0.08) !important;
            }

            .markmate-card {
                background: rgba(17, 17, 22, 0.9);
                border: 1px solid rgba(124, 58, 237, 0.26);
                border-radius: 1.6rem;
                padding: 1.4rem;
                box-shadow: 0 20px 55px rgba(0, 0, 0, 0.36);
                backdrop-filter: blur(16px);
            }

            .markmate-card:hover {
                transform: translateY(-4px);
                border-color: rgba(167, 139, 250, 0.58);
                box-shadow: 0 0 34px rgba(124, 58, 237, 0.2),
                            0 20px 55px rgba(0, 0, 0, 0.42);
            }

            ::-webkit-scrollbar {
                width: 8px;
            }

            ::-webkit-scrollbar-track {
                background: #030303;
            }

            ::-webkit-scrollbar-thumb {
                background: #7c3aed;
                border-radius: 999px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )