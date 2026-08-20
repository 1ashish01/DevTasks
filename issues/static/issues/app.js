const API_URL = "/api/issues/";


async function loadIssues() {

    const response = await fetch(API_URL);

    const issues = await response.json();

    const container = document.getElementById("issuesList");

    container.innerHTML = "";

    if (issues.length === 0) {
        container.innerHTML = "<p>No issues found.</p>";
        return;
    }

    issues.forEach(issue => {

        const div = document.createElement("div");

        div.className = "issue";

        div.innerHTML = `
            <h3>${issue.title}</h3>

            <p>${issue.description}</p>

            <span class="badge">
                Status: ${issue.status}
            </span>

            <span class="badge">
                Priority: ${issue.priority}
            </span>

            <span class="badge">
                Reporter: ${issue.reporter}
            </span>
        `;

        container.appendChild(div);
    });
}


document
    .getElementById("issueForm")
    .addEventListener("submit", async function(event) {

        event.preventDefault();

        const issue = {
            title: document.getElementById("title").value,
            description: document.getElementById("description").value,
            status: document.getElementById("status").value,
            priority: document.getElementById("priority").value,
            reporter: Number(document.getElementById("reporter").value)
        };

        const response = await fetch(API_URL, {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(issue)
        });

        if (response.ok) {

            alert("Issue created successfully!");

            document.getElementById("issueForm").reset();

            loadIssues();

        } else {

            const error = await response.json();

            console.log(error);

            alert("Failed to create issue.");
        }
    });


loadIssues();