
# AbleBot: NLP and Multimodal Toolchain Overview

## Purpose
This document outlines the finalized AI toolchain to be used in the development of the AbleBot system, focusing on accessibility for Persons with Disabilities (PWDs) through multimodal interactions — text, speech, and images.

## Core Components

| Component | Role in AbleBot | Tool / Framework |
|-----------|-----------------|------------------|
| Text Understanding (NLP) | Intent recognition, response generation | 🤖 BERT via HuggingFace Transformers |
| Speech-to-Text (STT) | Voice command input from PWD users | 🗣️ Whisper by OpenAI |
| Text-to-Speech (TTS) | Speak responses for visually impaired users | 🔊 Google Cloud TTS API |
| Optical Character Recognition (OCR) | Read signs, text documents, IDs from camera input | 👁️ Tesseract OCR Engine |
| Fallback NLP Option | Backup chatbot using GPT-based generation | 💬 OpenAI GPT API (Optional) |

## Tool Descriptions

### BERT
Platform: HuggingFace Transformers  
Use: Classify user intents (e.g., “Apply for PhilHealth,” “Where is the nearest hospital?”)  
Customization: Fine-tuned on localized intents + Filipino/Bicol samples  
Output: Intent label → triggers appropriate module

### Whisper (STT)
Platform: OpenAI Whisper (base or small model)  
Use: Converts user voice commands to text  
Advantage: High accuracy for Filipino-accented English and regional dialects  
Output: Transcribed text → sent to BERT for intent classification

### Tesseract (OCR)
Platform: Tesseract OCR engine (open source)  
Use: Converts images (e.g., IDs, documents, signs) to machine-readable text  
Use case: Assist users in reading real-world text captured through the phone camera

### Google Cloud Text-to-Speech
Converts bot’s response into natural-sounding voice  
Useful for blind users or those with low literacy  
Languages: English, Filipino supported

### GPT-3.5 Turbo (Optional)
Used only in fallback conversations or open-ended interactions  
Rate-limited and controlled to reduce costs

## Integration Flow

```
[Voice Input] ──▶ Whisper STT ──▶ BERT ──▶ Response ──▶ Google TTS
     │                              │
     └───────▶ OCR (if image) ──────┘
```

## GitHub Repository Structure

```
/models
   └── bert_intent_classifier
   └── whisper_stt
   └── ocr_reader
/api
   └── chatbot_logic.py
   └── audio_pipeline.py
/docs
   └── toolchain_overview.md
   └── usage_examples/
