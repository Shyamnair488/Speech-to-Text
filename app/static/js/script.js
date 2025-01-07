document.getElementById("speechForm").addEventListener("submit", async function (e) {
    e.preventDefault();
    const language = document.getElementById("language").value;

    try {
        const response = await fetch("/process_speech", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ language }),
        });
        const data = await response.json();
        if (data.text) {
            document.getElementById("result").textContent = `Recognized Text: ${data.text}`;
        } else {
            document.getElementById("result").textContent = "Error: " + data.error;
        }
    } catch (error) {
        document.getElementById("result").textContent = "An unexpected error occurred.";
    }
});
