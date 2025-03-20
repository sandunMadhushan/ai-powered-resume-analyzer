document.getElementById("uploadForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const formData = new FormData(e.target);

  const response = await fetch("/upload", {
    method: "POST",
    body: formData,
  });

  const result = await response.json();

  // Create a pre element
  const pre = document.createElement("pre");
  pre.style.cssText =
    "background-color: #f5f5f5; padding: 20px; border-radius: 5px; overflow: auto; max-height: 600px; font-family: monospace;";

  // Set the formatted JSON content
  pre.textContent =
    typeof result === "string" ? result : JSON.stringify(result, null, 2);

  // Clear previous results and add the new pre element
  const resultsDiv = document.getElementById("results");
  resultsDiv.innerHTML = "";
  resultsDiv.appendChild(pre);
});
