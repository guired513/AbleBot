import streamlit as st
import requests

st.markdown("""
<meta name="viewport" content="width=device-width, initial-scale=1.0">
""", unsafe_allow_html=True)

API_URL = "http://127.0.0.1:5000"

st.set_page_config(
    page_title="AbleBot Research Prototype",
    page_icon="♿",
    layout="centered"
)

st.markdown(
    """
    <style>
    .main {
        background-color: #f7f9fc;
    }

    .hero-card {
        background: linear-gradient(135deg, #0f172a, #1e3a8a);
        padding: 32px;
        border-radius: 24px;
        color: white;
        margin-bottom: 24px;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.18);
    }

    .hero-title {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 8px;
    }

    .hero-subtitle {
        font-size: 18px;
        line-height: 1.6;
        color: #dbeafe;
    }

    .feature-card {
        background-color: white;
        padding: 22px;
        border-radius: 18px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 4px 14px rgba(15, 23, 42, 0.06);
        height: 100%;
    }

    .feature-title {
        font-size: 20px;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 8px;
    }

    .feature-text {
        font-size: 14px;
        color: #475569;
        line-height: 1.5;
    }

    .status-pill {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 999px;
        background-color: #dcfce7;
        color: #166534;
        font-size: 13px;
        font-weight: 700;
        margin-top: 8px;
    }

    .section-title {
        font-size: 26px;
        font-weight: 800;
        color: #0f172a;
        margin-top: 20px;
        margin-bottom: 10px;
    }

    .small-note {
        font-size: 13px;
        color: #64748b;
    }

    .result-box {
        background-color: #f8fafc;
        border-left: 5px solid #2563eb;
        padding: 16px;
        border-radius: 12px;
        margin-top: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero-card">
        <div class="hero-title">AbleBot</div>
        <div class="hero-subtitle">
            A smart accessibility chatbot research prototype using BERT-based intent classification,
            speech-to-text, and optical character recognition to support persons with disabilities.
        </div>
        <div class="status-pill">Research Prototype • Multimodal Backend Working</div>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-title">💬 Text Chat</div>
            <div class="feature-text">
                Supports rule-based and BERT-based intent classification for accessibility-related queries.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-title">📷 OCR Reader</div>
            <div class="feature-text">
                Extracts text from images using Tesseract OCR for document and sign reading support.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-title">🎙 Speech-to-Text</div>
            <div class="feature-text">
                Converts audio input into text using Whisper, allowing voice-based interaction.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown('<div class="section-title">Chatbot Interaction</div>', unsafe_allow_html=True)

left_col, right_col = st.columns([2, 1])

with left_col:
    mode = st.radio(
        "Select classification mode",
        ["rule-based", "bert"],
        horizontal=True
    )

    user_message = st.text_area(
        "Enter user query",
        placeholder="Example: How do I register for PhilHealth?",
        height=100
    )

    if st.button("Send to AbleBot", use_container_width=True):
        if not user_message.strip():
            st.warning("Please enter a message first.")
        else:
            try:
                response = requests.post(
                    f"{API_URL}/chat",
                    json={
                        "message": user_message,
                        "mode": mode
                    },
                    timeout=60
                )

                if response.status_code == 200:
                    data = response.json()

                    st.markdown("### Response")
                    st.success(data.get("response", "No response returned."))

                    st.markdown("### Classification Details")
                    c1, c2, c3 = st.columns(3)

                    c1.metric("Intent", data.get("intent", "N/A"))
                    c2.metric("Confidence", data.get("confidence", "N/A"))
                    c3.metric("Model Used", data.get("model_used", "N/A"))

                    if data.get("matched_pattern"):
                        st.info(f"Matched Pattern: {data.get('matched_pattern')}")

                else:
                    st.error(f"Backend error: {response.status_code}")

            except Exception as e:
                st.error(f"Could not connect to backend: {e}")

with right_col:
    st.markdown("### Suggested Test Queries")
    st.write("- How to apply for PWD ID?")
    st.write("- I need help with PhilHealth membership")
    st.write("- I want health insurance")
    st.write("- What are the benefits of PWD?")
    st.write("- Where is the PDAO office?")

    st.markdown("---")
    st.markdown("### Research Note")
    st.caption(
        "This interface demonstrates a dual-mode chatbot prototype. "
        "The rule-based mode acts as a baseline, while BERT mode demonstrates early AI-based semantic intent classification."
    )

st.markdown('<div class="section-title">Multimodal Accessibility Tools</div>', unsafe_allow_html=True)

ocr_col, stt_col = st.columns(2)

with ocr_col:
    st.markdown("### 📷 OCR Image Reader")
    st.caption("Upload an image containing text. AbleBot extracts readable content using Tesseract OCR.")

    image_file = st.file_uploader(
        "Upload image",
        type=["png", "jpg", "jpeg"],
        key="ocr_upload"
    )

    if st.button("Extract Text", use_container_width=True):
        if image_file is None:
            st.warning("Please upload an image first.")
        else:
            try:
                files = {"image": image_file}
                response = requests.post(
                    f"{API_URL}/ocr",
                    files=files,
                    timeout=90
                )

                if response.status_code == 200:
                    data = response.json()
                    st.text_area(
                        "Extracted Text",
                        data.get("text", ""),
                        height=200
                    )
                else:
                    st.error(f"OCR request failed: {response.status_code}")

            except Exception as e:
                st.error(f"OCR connection error: {e}")

with stt_col:
    st.markdown("### 🎙 Speech-to-Text")
    st.caption("Upload an audio file. AbleBot transcribes speech using Whisper.")

    audio_file = st.file_uploader(
        "Upload audio",
        type=["mp3", "wav", "m4a"],
        key="stt_upload"
    )

    if st.button("Transcribe Audio", use_container_width=True):
        if audio_file is None:
            st.warning("Please upload an audio file first.")
        else:
            try:
                files = {"audio": audio_file}
                response = requests.post(
                    f"{API_URL}/stt",
                    files=files,
                    timeout=180
                )

                if response.status_code == 200:
                    data = response.json()
                    st.text_area(
                        "Transcription",
                        data.get("transcription", ""),
                        height=200
                    )
                else:
                    st.error(f"STT request failed: {response.status_code}")

            except Exception as e:
                st.error(f"STT connection error: {e}")

st.markdown("---")

st.markdown(
    """
    <div class="small-note" align="center">
        AbleBot Research Prototype | Current Stage: Backend MVP with multimodal input processing and initial BERT integration.
        Full BERT fine-tuning, mobile deployment, and formal user evaluation will proceed in the next development phase.<br><br>Copyright © 2026 AbleBot | Guillermo V. Red, Jr. All rights reserved.
    </div>
    """,
    unsafe_allow_html=True
)