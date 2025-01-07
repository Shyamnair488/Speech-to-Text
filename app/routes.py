import pyttsx3
import speech_recognition as sr
from flask import Blueprint, jsonify, render_template, request

app_routes = Blueprint('app_routes', __name__)

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Supported languages
INDIAN_LANGUAGES = [
    "as", "awa", "bho", "bn", "brx", "doi", "en", "gbm", "gu", "hi", "hne", "kok", "kfy", "kn", "ks", "mai",
    "mag", "ml", "mni", "mr", "ne", "or", "pa", "raj", "rwr", "sa", "sd", "si", "ta", "tcy", "te", "th", "ur"
]

def speech_to_text(language="en"):
    """
    Capture speech input and convert it to text.
    """
    with sr.Microphone() as source:
        try:
            print(f"Listening for speech in {language}...")
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=7)
            text = recognizer.recognize_google(audio, language=language)
            return text
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            return None
        except sr.WaitTimeoutError:
            return None

@app_routes.route("/")
def index():
    return render_template("index.html")

@app_routes.route("/process_speech", methods=["POST"])
def process_speech():
    language = request.json.get("language", "en")
    if language not in INDIAN_LANGUAGES:
        return jsonify({"error": "Invalid language code"}), 400

    text = speech_to_text(language)
    if text:
        return jsonify({"text": text})
    else:
        return jsonify({"error": "No valid speech input detected"}), 500
