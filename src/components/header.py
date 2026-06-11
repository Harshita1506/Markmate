import streamlit as st


def header_home():
    st.html(
        """
        <div style="
            display:flex;
            justify-content:center;
            align-items:center;
            margin-top:0.6rem;
            margin-bottom:1.4rem;
        ">
            <div style="
                display:flex;
                align-items:center;
                gap:0.75rem;
                padding:0.65rem 1rem;
                border-radius:999px;
                background:rgba(15, 15, 22, 0.72);
                border:1px solid rgba(124, 58, 237, 0.28);
                box-shadow:0 18px 45px rgba(0,0,0,0.35);
                backdrop-filter:blur(18px);
            ">
                <div style="
                    width:38px;
                    height:38px;
                    border-radius:12px;
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    background:linear-gradient(135deg, #8b5cf6, #6d28d9);
                    color:white;
                    font-size:1.15rem;
                    font-weight:900;
                    box-shadow:0 0 24px rgba(124,58,237,0.45);
                "><svg class="icon-svg" viewBox="0 0 24 24">
    <path d="M9 12l2 2 4-5"></path>
    <circle cx="12" cy="12" r="9"></circle>
</svg></div>

                <div style="
                    color:white;
                    font-size:1.05rem;
                    font-weight:900;
                    letter-spacing:-0.04em;
                ">MarkMate</div>

                <div style="
                    color:#a1a1aa;
                    font-size:0.82rem;
                    font-weight:700;
                    padding-left:0.6rem;
                    border-left:1px solid rgba(255,255,255,0.1);
                ">AI Attendance</div>
            </div>
        </div>
        """,
    )


def header_dashboard():
    st.html(
        """
        <div style="
            display:flex;
            align-items:center;
            justify-content:flex-start;
            gap:0.85rem;
            margin-bottom:0.8rem;
        ">
            <div style="
                width:54px;
                height:54px;
                border-radius:17px;
                background:linear-gradient(135deg, #8b5cf6, #6d28d9);
                display:flex;
                align-items:center;
                justify-content:center;
                box-shadow:0 0 30px rgba(124, 58, 237, 0.42);
                color:white;
                font-size:1.35rem;
                font-weight:900;
                flex-shrink:0;
            ">M</div>

            <div>
                <div style="
                    font-size:1.8rem;
                    line-height:1;
                    font-weight:950;
                    letter-spacing:-0.07em;
                    background:linear-gradient(135deg, #ffffff, #c4b5fd);
                    -webkit-background-clip:text;
                    -webkit-text-fill-color:transparent;
                ">MarkMate</div>

                <div style="
                    color:#a1a1aa;
                    font-size:0.82rem;
                    font-weight:800;
                    margin-top:0.28rem;
                ">AI Attendance Dashboard</div>
            </div>
        </div>
        """,
    )