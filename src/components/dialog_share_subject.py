import streamlit as st
import segno
import io


@st.dialog("Share MarkMate Class Link")
def share_subject_dialog(subject_name, subject_code):
    # Keep this as the actual deployed URL for now.
    # Change this only after redeploying the app with the new MarkMate URL.
    app_domain = "snapclass-main.streamlit.app"

    join_url = f"https://{app_domain}/?join-code={subject_code}"

    st.markdown(
        f"""
        <div style="margin-bottom:1rem;">
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
                🔗 Share Class
            </div>

            <div style="
                color:#ffffff;
                font-size:1.8rem;
                font-weight:900;
                letter-spacing:-0.05em;
                line-height:1.05;
            ">
                Share {subject_name}
            </div>

            <div style="
                color:#a1a1aa;
                font-size:0.95rem;
                font-weight:600;
                margin-top:0.4rem;
            ">
                Students can scan the QR code or use the join code to enroll.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    qr = segno.make(join_url)

    out = io.BytesIO()
    qr.save(out, kind='png', scale=10, border=1)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Copy Link")
        st.code(join_url, language="text")

        st.markdown("### Join Code")
        st.code(subject_code, language="text")

        st.info("Copy this link or code to share with students on WhatsApp or email.")

    with col2:
        st.markdown("### Scan to Join")
        st.image(out.getvalue(), caption="MarkMate class joining QR code")