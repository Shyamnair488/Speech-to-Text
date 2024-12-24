from flask import Flask, request, jsonify, render_template
import pyttsx3
import speech_recognition as sr

app = Flask(__name__)

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Supported languages
INDIAN_LANGUAGES = [
    "en", "hi", "bn", "te", "ml", "ta", "mr", "gu", "kn", "pa", "or", "as", "ur", "ne", "si", "th", "sa", "kok"
]

def calibrate_microphone():
    """
    Calibrate the microphone for ambient noise.
    """
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.8)

def speech_to_text(language="en"):
    """
    Capture speech input and convert it to text.
    """
    with sr.Microphone() as source:
        try:
            print(f"Listening for speech in {language}...")
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=7)
            text = recognizer.recognize_google(audio, language=language)
            print(f"Recognized Text: {text}")
            return text
        except sr.UnknownValueError:
            print("Error: Unable to understand the audio.")
            return None
        except sr.RequestError:
            print("Error: Network issue.")
            return None
        except sr.WaitTimeoutError:
            print("Error: No speech detected.")
            return None

@app.route("/")
def index():
    """
    Render the main HTML page.
    """
    return render_template("index.html")

@app.route("/process_speech", methods=["POST"])
def process_speech():
    """
    Handle speech processing requests.
    """
    language = request.json.get("language", "en")
    if language not in INDIAN_LANGUAGES:
        return jsonify({"error": "Invalid language code"}), 400

    text = speech_to_text(language)
    if text:
        return jsonify({"text": text})
    else:
        return jsonify({"error": "No valid speech input detected"}), 500

if __name__ == "__main__":
    app.run(debug=True)
