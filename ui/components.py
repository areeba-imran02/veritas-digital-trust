import streamlit as st


def render_header():

    st.markdown(
        """
        <div class="veritas-header">

            <div class="veritas-brand-area">

                <div class="veritas-wordmark">
                    VERITAS
                </div>

                <div class="veritas-tagline">
                    Understand. Verify. Trust.
                </div>

                <div class="veritas-description">
                    Digital Trust & Safety Intelligence Platform
                    for suspicious messages, content and online threats.
                </div>

            </div>


            <div class="veritas-status">

                <div class="status-dot"></div>

                <div>
                    <div class="status-label">
                        INTELLIGENCE CORE
                    </div>

                    <div class="status-value">
                        Operational
                    </div>
                </div>

            </div>

        </div>


        <style>

        .veritas-header {
            width: 100%;
            background: #ffffff;

            border: 1px solid #e5e7eb;
            border-radius: 16px;

            padding: 30px 34px;

            display: flex;
            align-items: center;
            justify-content: space-between;

            margin-bottom: 28px;

            box-shadow:
                0 1px 2px rgba(15, 23, 42, 0.03),
                0 10px 30px rgba(15, 23, 42, 0.05);
        }


        .veritas-brand-area {
            min-width: 0;
        }


        .veritas-wordmark {
            display: inline-block;

            font-family: 'Inter', sans-serif;

            font-size: 38px;
            line-height: 1;

            font-weight: 800;
            letter-spacing: 4px;

            color: #0f172a;

            /* subtle dimensional wordmark */
            text-shadow:
                0 1px 0 #cbd5e1,
                0 2px 3px rgba(15, 23, 42, 0.10);
        }


        .veritas-tagline {
            margin-top: 10px;

            font-size: 17px;
            font-weight: 700;

            color: #2563eb;
            letter-spacing: -0.01em;
        }


        .veritas-description {
            margin-top: 7px;

            color: #6b7280;

            font-size: 13px;
            line-height: 1.6;
        }


        .veritas-status {
            display: flex;
            align-items: center;
            gap: 10px;

            background: #f8fafc;

            border: 1px solid #e5e7eb;

            border-radius: 10px;

            padding: 10px 14px;

            min-width: 150px;
        }


        .status-dot {
            width: 8px;
            height: 8px;

            background: #10b981;

            border-radius: 50%;

            box-shadow: 0 0 0 4px rgba(16, 185, 129, 0.10);
        }


        .status-label {
            color: #9ca3af;

            font-size: 9px;
            font-weight: 700;

            letter-spacing: 1px;
        }


        .status-value {
            color: #111827;

            font-size: 12px;
            font-weight: 600;

            margin-top: 2px;
        }


        @media (max-width: 700px) {

            .veritas-header {
                padding: 24px;
                align-items: flex-start;
                flex-direction: column;
                gap: 20px;
            }

            .veritas-wordmark {
                font-size: 32px;
            }

        }

        </style>
        """,
        unsafe_allow_html=True,
    )


def render_file_dropzone(label: str):
    return st.file_uploader(
        label,
        type=["png", "jpg", "jpeg", "pdf", "txt"],
    )


def render_metric_gauge(label: str, value: str):
    st.metric(
        label=label,
        value=value,
    )
