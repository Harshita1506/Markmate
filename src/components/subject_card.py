import streamlit as st


def subject_card(name, code, section, stats=None, footer_callback=None):
    stats_html = ""

    if stats:
        stats_html += """
            <div style="
                display:grid;
                grid-template-columns:repeat(auto-fit, minmax(110px, 1fr));
                gap:0.75rem;
                margin-top:1.15rem;
            ">
        """

        for icon, label, value in stats:
            stats_html += f"""
                <div style="
                    background:rgba(124, 58, 237, 0.12);
                    border:1px solid rgba(124, 58, 237, 0.24);
                    padding:0.8rem 0.9rem;
                    border-radius:1rem;
                ">
                    <div style="
                        color:#a1a1aa;
                        font-size:0.78rem;
                        font-weight:700;
                        margin-bottom:0.25rem;
                    ">
                        {icon} {label}
                    </div>

                    <div style="
                        color:#ffffff;
                        font-size:1.35rem;
                        font-weight:900;
                        line-height:1;
                    ">
                        {value}
                    </div>
                </div>
            """

        stats_html += "</div>"

    html = f"""
        <div style="
            position:relative;
            background:rgba(15, 15, 22, 0.86);
            border:1px solid rgba(124, 58, 237, 0.28);
            border-radius:1.8rem;
            padding:1.4rem;
            margin-bottom:1.25rem;
            box-shadow:
                0 24px 70px rgba(0, 0, 0, 0.42),
                inset 0 1px 0 rgba(255,255,255,0.06);
            overflow:hidden;
            backdrop-filter:blur(18px);
        ">
            <div style="
                position:absolute;
                top:-65px;
                right:-65px;
                width:160px;
                height:160px;
                border-radius:50%;
                background:rgba(124, 58, 237, 0.22);
                filter:blur(8px);
            "></div>

            <div style="
                display:flex;
                align-items:flex-start;
                justify-content:space-between;
                gap:1rem;
                position:relative;
                z-index:2;
            ">
                <div>
                    <div style="
                        display:inline-flex;
                        align-items:center;
                        gap:0.45rem;
                        padding:0.35rem 0.75rem;
                        border-radius:999px;
                        background:rgba(124, 58, 237, 0.14);
                        border:1px solid rgba(167, 139, 250, 0.28);
                        color:#c4b5fd;
                        font-size:0.78rem;
                        font-weight:800;
                        margin-bottom:0.8rem;
                    ">
                        {code}
                    </div>

                    <div style="
                        margin:0;
                        color:#ffffff;
                        font-size:1.45rem;
                        font-weight:800;
                        letter-spacing:-0.025em;
                        line-height:1.15;
                    ">
                        {name}
                    </div>

                    <div style="
                        margin:0.55rem 0 0 0;
                        color:#a1a1aa;
                        font-size:0.92rem;
                        font-weight:600;
                    ">
                        Section <span style="color:#ffffff;">{section}</span>
                    </div>
                </div>

                <div style="
                    width:48px;
                    height:48px;
                    border-radius:1rem;
                    background:linear-gradient(135deg, #8b5cf6, #6d28d9);
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    box-shadow:0 0 28px rgba(124, 58, 237, 0.38);
                    color:white;
                    font-size:1.1rem;
                    font-weight:900;
                    flex-shrink:0;
                ">
                    📘
                </div>
            </div>

            <div style="position:relative; z-index:2;">
                {stats_html}
            </div>
        </div>
    """

    st.html(html)

    if footer_callback:
        footer_callback()