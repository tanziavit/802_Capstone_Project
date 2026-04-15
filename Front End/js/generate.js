document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("generateForm").addEventListener("submit", function(e) {
        e.preventDefault();

        const location = document.getElementById("location").value;
        const size = document.getElementById("size").value;
        const price = document.getElementById("price").value;
        const features = document.getElementById("features").value;
        const tone = document.getElementById("tone").value;

        // Show loading state
        document.getElementById("outputSection").style.display = "block";
        document.getElementById("listingOutput").innerText = "Generating...";
        document.getElementById("socialOutput").innerText = "";
        document.getElementById("emailOutput").innerText = "";
        document.getElementById("videoOutput").innerText = "";

        fetch("/api/generate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                location,
                size,
                price,
                features,
                tone
            })
        })
        .then(response => response.json())
        .then(data => {
            const result = data.result || "No response from AI.";

            // Since backend returns one block, show in all sections for now
            document.getElementById("listingOutput").innerText = result;
            document.getElementById("socialOutput").innerText = result;
            document.getElementById("emailOutput").innerText = result;
            document.getElementById("videoOutput").innerText = result;
        })
        .catch(error => {
            console.error("Error:", error);
            document.getElementById("listingOutput").innerText = "Error generating content.";
        });
    });

    // Logout
    document.getElementById("logoutBtn").addEventListener("click", function(e) {
        e.preventDefault();

        fetch("/api/logout", {
            method: "POST"
        })
        .then(() => {
            window.location.href = "/login";
        });
    });
});