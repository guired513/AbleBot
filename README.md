# AbleBot: An AI-Powered Multimodal Accessibility Assistance Platform for Persons with Disabilities (PWDs)

**Towards Inclusive AI: A Smart Accessibility Chatbot Using BERT and Multimodal Input for Empowering Persons with Disabilities**

AbleBot is a research-based mobile chatbot system designed to assist persons with disabilities (PWDs) through multimodal interaction — including voice, text, and image input. This project is developed by Bicol University Polangui and aligns with SDG 10 (Reduced Inequalities) and SDG 9 (Industry, Innovation, and Infrastructure).



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
---

# Project Vision

AbleBot aims to become a deployable and implementable accessibility platform that can assist PWD users in accessing information, services, and communication tools through adaptive multimodal interaction.

The platform is specifically designed to support:
- general PWD users
- visually impaired individuals
- hearing-impaired individuals

through accessible mobile-first interaction workflows.

---

# Current System Status

## Core AI Features

### Chatbot Modes
AbleBot currently supports three AI interaction modes:

1. Rule-Based NLP
2. BERT Intent Matching
3. Fine-Tuned BERT Classifier

### Supported Intents
(as of february 2026)
- greeting
- pwd_id
- philhealth
- benefits
- location_pdao
- medical_help
- reminder

### Fine-Tuned BERT

Current development includes:
- custom intent dataset
- fine-tuned BERT classification
- local model deployment
- HuggingFace Transformers integration

Current experimental accuracy:
- approximately 84.6%

---

# Multimodal Features


## OCR (Optical Character Recognition)
- Tesseract OCR integration
- image-to-text extraction
- API endpoint support

## Speech-to-Text
- Whisper integration
- audio transcription pipeline
- FFmpeg support

## Text-to-Speech
- browser-based speech synthesis
- planned cloud neural voice integration

## 🎯 Features
- 🎤 Voice-based interaction (Whisper STT)
- 🧠 Intent recognition (BERT via HuggingFace Transformers)
- 📷 Visual text reading (OCR using Tesseract)
- 🔊 Spoken responses (Google Cloud TTS)
- 🌐 Mobile-first accessible UI (WCAG 2.2-compliant)
- 📅 Smart scheduling, reminders, and API-based service links

---

# Mobile Application Transition

AbleBot is currently transitioning from a web/PWA prototype into a native Flutter mobile application.

## Current Mobile Status

### Completed
- Flutter mobile foundation
- Android deployment pipeline
- real-device testing
- Flutter-to-Flask API communication
- chatbot interaction on Android

### Planned
- Play Store testing deployment
- accessibility gesture system
- haptic feedback
- voice-first interaction workflows
- OCR camera assistant
- accessibility onboarding

---

# Accessibility Features Roadmap

## Visual Impairment Support

Planned features include:

- voice-guided onboarding
- accessibility mode activation
- tap-and-hold speech interaction
- spoken chatbot responses
- OCR document reading assistant
- haptic feedback
- simplified high-contrast interface

## Hearing-Impaired Support

Planned features include:

- caption-first interaction
- readable large-text interface
- visual interaction indicators
- non-audio feedback system
- accessible notification system

---

# System Architecture

```text
Flutter Mobile App
        ↓
Flask Backend API
        ↓
AI Services
├── Rule-Based NLP
├── BERT
├── Fine-Tuned BERT
├── Whisper STT
├── OCR Pipeline
└── TTS Services
        ↑
Existing PWA Client
```

The existing Progressive Web App (PWA) remains active as:
- a browser-accessible client
- an iOS-compatible fallback
- a rapid demonstration platform

---

# Technology Stack

## Backend
- Python
- Flask
- HuggingFace Transformers
- BERT
- Whisper
- Tesseract OCR

## Frontend
- HTML
- CSS
- JavaScript
- Progressive Web App

## Mobile
- Flutter
- Android deployment

## Planned Cloud Services
- Google Cloud TTS
- Google Cloud STT
- Google Vision OCR

---

# Research and Evaluation

The project includes:
- AI model comparison
- usability testing
- accessibility evaluation
- OCR evaluation
- STT/TTS evaluation
- pilot deployment testing

Evaluation methodologies include:
- functional testing
- task completion analysis
- user interaction observation
- usability scoring
- model performance comparison

---

# Deployment Targets

## Android
- Flutter mobile application
- Google Play testing deployment

## iOS
- Progressive Web App (PWA) fallback

## Backend Hosting
- Render cloud deployment

---

# Research Significance

AbleBot is designed not merely as a chatbot system, but as a multimodal accessibility-centered AI platform that explores how AI technologies can support inclusive digital access for Persons with Disabilities.

The project combines:
- conversational AI
- accessibility engineering
- mobile computing
- multimodal interaction
- assistive technology research

into a deployable research-grade system.

---

## 🔗 Acknowledgments
- HuggingFace Transformers
- OpenAI Whisper
- Google Cloud Text-to-Speech
- Tesseract OCR
- Bicol University Research and Development Management Division
- Bicol University Office of the Vice President for Research, Development and Extension
---

_This repository is maintained as part of the 2025–2026 research project by Bicol University Polangui._

---

# Maintainer

Developed under:
- Bicol University Polangui
- Research and Development initiatives on Inclusive AI and Accessibility Technologies

---