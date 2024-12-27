const express = require("express");

const app = express();
app.use(express.json());

// Supported languages
const INDIAN_LANGUAGES = [
  "en", "hi", "bn", "te", "ml", "ta", "mr", "gu", "kn", "pa", "or", "as", "ur", "ne", "si", "th", "sa", "kok"
];

app.post("/api/process_speech", (req, res) => {
  const { language } = req.body;

  if (!language) {
    return res.status(400).json({ error: "Invalid request, 'language' is required in JSON data" });
  }

  if (!INDIAN_LANGUAGES.includes(language)) {
    return res.status(400).json({
      error: `Invalid language code: ${language}. Supported languages: ${INDIAN_LANGUAGES.join(", ")}`,
    });
  }

  // Simulated Speech-to-Text processing
  res.status(200).json({ text: `Processed speech in ${language}` });
});

module.exports = app;
