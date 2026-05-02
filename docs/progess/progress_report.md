# AbleBot Project – Progress Notes (May Report)

## 1. Project Overview

AbleBot is an AI-powered assistive chatbot designed to support Persons with Disabilities (PWDs) by providing accessible information services through natural language interaction. The system integrates multiple Natural Language Processing (NLP) components, including text-based chat, speech-to-text (STT), and optical character recognition (OCR), with Machine Learning (ML)-based intent classification.

---

## 2. Current Development Status

### 2.1 System Architecture (Objective 1)

The system has been successfully developed as a working prototype with the following components:

- Backend API using Flask
- Intent classification system:
  - Rule-based matching
  - BERT-based semantic matching
- Web-based mobile-accessible interface (Progressive Web App style)
- Modular structure:
  - Chatbot logic
  - OCR module (Tesseract)
  - STT module (Whisper)
  - Intent service

Status:
> Objective 1 is substantially completed through a functional prototype.

---

### 2.2 Feature Integration (Objective 2)

The system currently supports the following features:

#### Text-based Chat
- Users can input queries in natural language
- System responds based on intent classification

#### Speech-to-Text (STT)
- Audio file upload processed using Whisper
- Transcription automatically displayed and usable as chatbot input

#### Optical Character Recognition (OCR)
- Image upload processed using Tesseract
- Extracted text displayed to the user

#### Accessibility Features (Initial)
- Large-button mobile-friendly interface
- Text-to-speech (browser-based) for chatbot responses
- Voice input (browser-based, limited support depending on device)

Status:
> Objective 2 has been initiated and partially implemented.

---

### 2.3 Machine Learning Integration (Objective 3)

#### Rule-Based Intent Matching
- Keyword and pattern-based matching using `intents.json`

#### BERT-Based Semantic Matching
- Pretrained BERT model used for semantic similarity
- Supports more flexible understanding of user input

#### Initial BERT Fine-Tuning
- Training dataset generated from `intents.json`
- Total samples: 51 labeled entries
- Model trained for 1 epoch
- Initial test accuracy: 0.27
- Model artifacts successfully generated and saved locally

Status:
> Objective 3 has been initiated with both rule-based and ML-based approaches implemented.

---

## 3. Dataset Status

Current dataset:

- Total samples: 51
- Number of intents: 7
- Samples per intent range: 5–14

Observation:
- Dataset is sufficient for pipeline validation
- Dataset is not yet sufficient for stable ML performance

Planned improvement:
> Expand dataset to 150–250 samples to improve model accuracy and enable meaningful evaluation.

---

## 4. Demonstrable Outputs

The following features can be demonstrated:

- Chatbot interaction (text input)
- Rule-based vs BERT mode switching
- OCR functionality (image to text)
- STT functionality (audio to text)
- Mobile-accessible interface (Android, iOS, browser)
- Initial BERT training pipeline and saved model

---

## 5. Issues Encountered

### Technical Issues

- Dependency conflicts (transformers, huggingface-hub)
- Installation issues for ML libraries
- GitHub push failure due to large model files (>100MB)
- Browser limitations for speech recognition on mobile devices

### System Limitations

- Small dataset affecting BERT accuracy
- Voice input not fully reliable on mobile browsers (HTTP restrictions)
- OCR and STT currently use upload-based interaction instead of real-time capture

---

## 6. Actions Taken

- Resolved dependency conflicts by aligning package versions
- Replaced HuggingFace `datasets` pipeline with PyTorch-based training pipeline
- Implemented `.gitignore` and removed model files from Git history
- Enabled successful GitHub push after cleaning repository
- Implemented fallback strategies for voice features
- Verified functionality across Windows, Android, and iOS devices

---

## 7. Next Steps

### Immediate (Next Phase)
- Expand intent dataset to 150–250 samples
- Retrain BERT model and compare performance
- Improve classification accuracy

### Short-Term
- Improve accessibility interaction design:
  - Tap-to-speak interface
  - Automatic voice response
  - Simplified UI for PWD users

### Long-Term
- Develop native mobile application (Flutter)
- Implement camera-based OCR
- Conduct formal model evaluation and comparison
- Enhance system usability for different types of disabilities

---

## 8. Summary

The AbleBot system has progressed from conceptual design to a functional prototype integrating NLP and ML components. The current implementation demonstrates the feasibility of an accessible AI chatbot for PWD support. While machine learning performance is still limited by dataset size, the foundational pipeline for BERT-based intent classification has been successfully established.


## BERT Fine-Tuning Update

The AbleBot intent dataset was expanded from 51 labeled samples to 195 labeled samples across seven intent categories. A BERT fine-tuning pipeline was executed using the expanded dataset.

Training was conducted for three epochs. The average training loss decreased across epochs:

- Epoch 1: 1.9192
- Epoch 2: 1.4861
- Epoch 3: 1.0694

The initial test accuracy reached 84.62%.

This result indicates that the supervised BERT fine-tuning pipeline is functional and that dataset expansion improved the model’s intent classification performance. Further validation with larger and real user-derived datasets will be conducted in the next phase.