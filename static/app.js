let currentMode = "bert";

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

    responseBox.innerText = data.response || "No response received.";

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

  resultBox.innerText = "Reading image...";

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

  resultBox.innerText = "Transcribing audio...";

  const formData = new FormData();
  formData.append("audio", input.files[0]);

  try {
    const response = await fetch("/stt", {
      method: "POST",
      body: formData
    });

    const data = await response.json();
    resultBox.innerText = data.transcription || "No transcription detected.";
  } catch (error) {
    resultBox.innerText = "Speech-to-text failed.";
  }
}