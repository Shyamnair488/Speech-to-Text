export default function handler(req, res) {
    const INDIAN_LANGUAGES = [
        "en", "hi", "bn", "te", "ml", "ta", "mr", "gu", "kn", "pa"
    ];

    if (req.method !== "POST") {
        return res.status(405).json({ error: "Method not allowed" });
    }

    const { language } = req.body;

    if (!language) {
        return res.status(400).json({ error: "Invalid request, 'language' is required in JSON data" });
    }

    if (!INDIAN_LANGUAGES.includes(language)) {
        return res.status(400).json({
            error: `Invalid language code: ${language}. Supported languages: ${INDIAN_LANGUAGES.join(", ")}`,
        });
    }

    // If the language is valid, simulate speech processing
    res.status(200).json({ text: `Processed speech in ${language}` });
}
