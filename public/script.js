document.getElementById("speechForm").addEventListener("submit", async (event) => {
    event.preventDefault();
  
    const language = document.getElementById("language").value;
    const responseDiv = document.getElementById("response");
  
    responseDiv.textContent = "Processing your request...";
  
    try {
      const response = await fetch("/api/process_speech", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ language }),
      });
  
      const data = await response.json();
  
      if (response.ok) {
        responseDiv.textContent = data.text;
      } else {
        responseDiv.textContent = `Error: ${data.error}`;
      }
    } catch (error) {
      responseDiv.textContent = "An error occurred. Please try again.";
    }
  });
  