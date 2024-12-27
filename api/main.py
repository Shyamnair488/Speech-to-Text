import traceback

from flask import Flask, jsonify, request

app = Flask(__name__)

INDIAN_LANGUAGES = ["en", "hi", "ta", "te", "bn", "gu", "kn", "ml", "mr", "pa", "ur"]

def speech_to_text(language):
    try:
        # Simulate speech-to-text processing (replace with actual logic)
        # Example: Use vosk or any other ASR library
        if language in INDIAN_LANGUAGES:
            return f"Processed speech in {language}"
        return None
    except Exception as e:
        print(f"Speech processing error: {str(e)}")
        print(traceback.format_exc())
        return None

@app.route("/process_speech", methods=["POST"])
def process_speech():
    try:
        # Parse the incoming JSON data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid request, JSON data is required"}), 400

        language = data.get("language", "en")
        if language not in INDIAN_LANGUAGES:
            return jsonify({"error": f"Invalid language code: {language}. Supported languages: {INDIAN_LANGUAGES}"}), 400

        # Perform speech-to-text
        text = speech_to_text(language)
        if text:
            return jsonify({"text": text}), 200
        else:
            return jsonify({"error": "No valid speech input detected"}), 500

    except Exception as e:
        # Log the error and return a generic error message
        print(f"Internal Server Error: {str(e)}")
        print(traceback.format_exc())
        return jsonify({"error": "Internal Server Error"}), 500

# Ensure the app works for Vercel
if __name__ == "__main__":
    app.run(debug=True)
