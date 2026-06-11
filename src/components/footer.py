import streamlit as st


def footer_home():
    st.markdown(
        """
        <div style="
            margin-top:2rem;
            display:flex;
            justify-content:center;
            align-items:center;
            text-align:center;
        ">
            <div style="
                padding:0.7rem 1.05rem;
                border-radius:999px;
                background:rgba(15, 15, 22, 0.68);
                border:1px solid rgba(124, 58, 237, 0.22);
                color:#a1a1aa;
                font-size:0.85rem;
                font-weight:750;
                box-shadow:0 14px 35px rgba(0,0,0,0.28);
                backdrop-filter:blur(16px);
            ">
                Built with care by <span style="color:#c4b5fd;">HARSHITA</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def footer_dashboard():
    st.markdown(
        """
        <div style="
            margin-top:2.5rem;
            display:flex;
            justify-content:center;
            align-items:center;
            text-align:center;
        ">
            <div style="
                padding:0.7rem 1.05rem;
                border-radius:999px;
                background:rgba(15, 15, 22, 0.68);
                border:1px solid rgba(124, 58, 237, 0.22);
                color:#a1a1aa;
                font-size:0.85rem;
                font-weight:750;
                box-shadow:0 14px 35px rgba(0,0,0,0.28);
                backdrop-filter:blur(16px);
            ">
                Built with care by <span style="color:#c4b5fd;">HARSHITA</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )