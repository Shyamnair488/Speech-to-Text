async function startSpeechRecognition() {
    const micButton = document.getElementById("micButton");
    const language = document.getElementById("language").value;

    micButton.classList.add("active");
    document.getElementById("output").innerText = "Processing...";

    try {
        const response = await fetch("/process_speech", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ language }),
        });

        const data = await response.json();
        micButton.classList.remove("active");

        if (response.ok) {
            document.getElementById("output").innerText = "Recognized Text: " + data.text;
        } else {
            document.getElementById("output").innerText = "Error: " + data.error;
        }
    } catch (error) {
        micButton.classList.remove("active");
        document.getElementById("output").innerText = "Error: Unable to process speech.";
    }
}
