# AbleBot: AI Chatbot for Digital Accessibility

**Towards Inclusive AI: A Smart Accessibility Chatbot Using BERT and Multimodal Input for Empowering Persons with Disabilities**

AbleBot is a research-based mobile chatbot system designed to assist persons with disabilities (PWDs) through multimodal interaction — including voice, text, and image input. This project is developed by Bicol University Polangui and aligns with SDG 10 (Reduced Inequalities) and SDG 9 (Industry, Innovation, and Infrastructure).

## 🎯 Features
- 🎤 Voice-based interaction (Whisper STT)
- 🧠 Intent recognition (BERT via HuggingFace Transformers)
- 📷 Visual text reading (OCR using Tesseract)
- 🔊 Spoken responses (Google Cloud TTS)
- 🌐 Mobile-first accessible UI (WCAG 2.2-compliant)
- 📅 Smart scheduling, reminders, and API-based service links

## 🧰 Tech Stack
- BERT (fine-tuned) for NLP
- Whisper (OpenAI) for speech-to-text
- Tesseract OCR for image-based text input
- Google Cloud TTS for responses
- React Native for mobile UI
- Flask / FastAPI for backend logic
- Firebase or Render for hosting

## 📁 Folder Structure
```
AbleBot/
│
├── /docs/                      # Research files, mockups
├── /models/                    # AI and NLP models (BERT, Whisper)
├── /api/                       # Python backend for chatbot logic
├── /ui/                        # Frontend mobile UI (React Native)
├── /data/                      # Datasets or input samples
├── .gitignore                  # Ignore rules for Git
├── README.md                   # Project overview and documentation
├── requirements.txt            # Backend Python dependencies
└── LICENSE                     # Licensing (TBD)
```

## 🔗 Acknowledgments
- HuggingFace Transformers
- OpenAI Whisper
- Google Cloud Text-to-Speech
- Tesseract OCR
- Bicol University Research and Development Management Division
- Bicol University Office of the Vice President for Research, Development and Extension
---

_This repository is maintained as part of the 2025–2026 research project by Bicol University Polangui._