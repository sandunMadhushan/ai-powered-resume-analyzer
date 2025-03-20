document.getElementById("uploadForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const formData = new FormData(e.target);
  const resultsDiv = document.getElementById("results");
  const loadingDiv = document.getElementById("loading");

  // Clear previous results and show loading
  resultsDiv.innerHTML = "";
  loadingDiv.style.display = "block";

  try {
    const response = await fetch("/upload", {
      method: "POST",
      body: formData,
    });

    // Hide loading indicator
    loadingDiv.style.display = "none";

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const result = await response.json();
    console.log("Raw response:", result); // Debug log

    // Check if we got an error response
    if (result.error) {
      // If it's an API quota error, show a specific message
      if (result.error.includes("quota")) {
        resultsDiv.innerHTML = `
          <div class="error">
            <h2>API Quota Exceeded</h2>
            <p>We've reached our API usage limit. Please try again later or contact support.</p>
          </div>
        `;
      } else {
        // For other errors, show the error message
        resultsDiv.innerHTML = `
          <div class="error">
            <h2>Error</h2>
            <p>${result.error}</p>
          </div>
        `;
      }
      return;
    }

    // Parse the feedback from the response
    let feedback;
    if (result.error) {
      // If we got an error object with raw_content, try to parse that
      try {
        feedback = JSON.parse(result.raw_content);
      } catch (e) {
        console.error("Failed to parse raw content:", e);
        resultsDiv.innerHTML = `
          <div class="error">
            <h2>Error</h2>
            <p>Failed to parse resume analysis. Please try again.</p>
          </div>
        `;
        return;
      }
    } else {
      feedback = result;
    }

    console.log("Processed feedback:", feedback); // Debug log

    // Add overall impression
    const overallSection = document.createElement("div");
    overallSection.className = "section";

    const overallAssessment = feedback.feedback?.overallAssessment;
    if (overallAssessment) {
      overallSection.innerHTML = `
        <h2>Overall Impression</h2>
        <div class="strengths">
          <h3>Strengths</h3>
          <ul>
            ${overallAssessment.strengths
              .map((strength) => `<li>${strength}</li>`)
              .join("")}
          </ul>
        </div>
        <div class="improvements">
          <h3>Areas for Improvement</h3>
          <ul>
            ${overallAssessment.areasForImprovement
              .map((improvement) => `<li>${improvement}</li>`)
              .join("")}
          </ul>
        </div>
      `;
    } else {
      overallSection.innerHTML = `
        <h2>Overall Impression</h2>
        <p>No overall assessment available.</p>
      `;
    }
    resultsDiv.appendChild(overallSection);

    // Add each section
    const sections = feedback.feedback || {};
    console.log("Sections to process:", sections); // Debug log

    for (const [sectionName, sectionData] of Object.entries(sections)) {
      // Skip the overallAssessment section as it's already handled
      if (sectionName === "overallAssessment") continue;

      const sectionDiv = document.createElement("div");
      sectionDiv.className = "section";

      // Format section name
      const formattedName = sectionName
        .split(/(?=[A-Z])/)
        .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
        .join(" ")
        .replace("Section", "");

      sectionDiv.innerHTML = `
        <h2>${formattedName}</h2>
        <div class="strengths">
          <h3>Strengths</h3>
          <ul>
            ${(sectionData.strengths || [])
              .map((strength) => `<li>${strength}</li>`)
              .join("")}
          </ul>
        </div>
        <div class="improvements">
          <h3>Areas for Improvement</h3>
          <ul>
            ${(sectionData.areasForImprovement || [])
              .map((improvement) => `<li>${improvement}</li>`)
              .join("")}
          </ul>
        </div>
      `;

      resultsDiv.appendChild(sectionDiv);
    }
  } catch (error) {
    // Hide loading indicator on error
    loadingDiv.style.display = "none";

    console.error("Error:", error);
    resultsDiv.innerHTML = `
      <div class="error">
        <h2>Error</h2>
        <p>An error occurred while processing your resume. Please try again later.</p>
      </div>
    `;
  }
});
