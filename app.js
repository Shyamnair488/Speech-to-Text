const express = require("express");
const path = require("path");

const app = express();

// Middleware to parse JSON requests
app.use(express.json());

// Serve the static files from the public folder
app.use(express.static(path.join(__dirname, "public")));

// API endpoint (matches the structure in `api/processSpeech.js`)
app.post("/api/process_speech", (req, res) => {
  const INDIAN_LANGUAGES = [
    "en", "hi", "bn", "te", "ml", "ta", "mr", "gu", "kn", "pa", "or", "as", "ur", "ne", "si", "th", "sa", "kok"
  ];

  const { language } = req.body;

  if (!language) {
    return res.status(400).json({ error: "Invalid request, 'language' is required in JSON data" });
  }

  if (!INDIAN_LANGUAGES.includes(language)) {
    return res.status(400).json({
      error: `Invalid language code: ${language}. Supported languages: ${INDIAN_LANGUAGES.join(", ")}`,
    });
  }

  res.status(200).json({ text: `Processed speech in ${language}` });
});

// Serve the frontend index.html for any unmatched route
app.get("*", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "index.html"));
});

// Start the server on a local port
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
