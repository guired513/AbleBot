let currentMode = "bert";
let lastResponse = "";

function setMode(mode) {
  currentMode = mode;

  const buttons = document.querySelectorAll(".access-btn");
  buttons.forEach(btn => btn.classList.remove("active"));

  if (mode === "rule-based") {
    buttons[0].classList.add("active");
  } else {
    buttons[1].classList.add("active");
  }
}

function speakText(text) {
  if (!text || !text.trim()) {
    alert("There is no response to speak yet.");
    return;
  }

  if (!("speechSynthesis" in window)) {
    alert("Text-to-speech is not supported in this browser.");
    return;
  }

  window.speechSynthesis.cancel();

  const speech = new SpeechSynthesisUtterance(text);
  speech.lang = "en-US";
  speech.rate = 0.9;
  speech.pitch = 1;
  speech.volume = 1;

  window.speechSynthesis.speak(speech);
}

function startListening() {
  const SpeechRecognition =
    window.SpeechRecognition || window.webkitSpeechRecognition;

  if (!SpeechRecognition) {
    alert(
      "Voice input is not supported in this browser. Please use the audio upload Speech-to-Text feature instead."
    );
    return;
  }

  const recognition = new SpeechRecognition();
  recognition.lang = "en-US";
  recognition.interimResults = false;
  recognition.maxAlternatives = 1;

  recognition.onstart = function () {
    document.getElementById("responseBox").innerText = "Listening...";
  };

  recognition.onresult = function (event) {
    const transcript = event.results[0][0].transcript;
    document.getElementById("message").value = transcript;
    document.getElementById("responseBox").innerText =
      "Voice captured. Tap Send Message to ask AbleBot.";
  };

  recognition.onerror = function (event) {
    document.getElementById("responseBox").innerText =
      "Voice input error: " + event.error + ". You may use audio upload instead.";
  };

  recognition.start();
}

async function sendMessage() {
  const message = document.getElementById("message").value;
  const responseBox = document.getElementById("responseBox");
  const metaBox = document.getElementById("metaBox");

  if (!message.trim()) {
    responseBox.innerText = "Please enter a question first.";
    return;
  }

  responseBox.innerText = "AbleBot is thinking...";
  metaBox.innerText = "";

  try {
    const response = await fetch("/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        message: message,
        mode: currentMode
      })
    });

    const data = await response.json();

    lastResponse = data.response || "No response received.";
    responseBox.innerText = lastResponse;

    metaBox.innerHTML = `
      <strong>Intent:</strong> ${data.intent || "N/A"}<br>
      <strong>Confidence:</strong> ${data.confidence ?? "N/A"}<br>
      <strong>Model Used:</strong> ${data.model_used || "N/A"}
      ${data.matched_pattern ? `<br><strong>Matched Pattern:</strong> ${data.matched_pattern}` : ""}
    `;
  } catch (error) {
    responseBox.innerText = "Could not connect to AbleBot backend.";
  }
}

async function sendOCR() {
  const input = document.getElementById("imageInput");
  const resultBox = document.getElementById("ocrResult");

  if (!input.files[0]) {
    resultBox.innerText = "Please upload an image first.";
    return;
  }

  resultBox.innerText = "Image selected: " + input.files[0].name + "\nReading image...";


  const formData = new FormData();
  formData.append("image", input.files[0]);

  try {
    const response = await fetch("/ocr", {
      method: "POST",
      body: formData
    });

    const data = await response.json();
    resultBox.innerText = data.text || "No text detected.";
  } catch (error) {
    resultBox.innerText = "OCR failed.";
  }
}

async function sendSTT() {
  const input = document.getElementById("audioInput");
  const resultBox = document.getElementById("sttResult");

  if (!input.files[0]) {
    resultBox.innerText = "Please upload an audio file first.";
    return;
  }

  resultBox.innerText = "Audio selected: " + input.files[0].name + "\nTranscribing audio...";

  const formData = new FormData();
  formData.append("audio", input.files[0]);

  try {
    const response = await fetch("/stt", {
      method: "POST",
      body: formData
    });

    const data = await response.json();
    resultBox.innerText = data.transcription || "No transcription detected.";

    if (data.transcription) {
      document.getElementById("message").value = data.transcription;
    }
  } catch (error) {
    resultBox.innerText = "Speech-to-text failed.";
  }
}

function toggleAccessibility() {
  document.body.classList.toggle("accessibility");
}