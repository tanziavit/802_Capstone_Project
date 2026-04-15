// Dummy data (later replace with backend data)
let historyData = [
    {
        id: 1,
        location: "New York",
        listing: "Beautiful 3BHK apartment in New York...",
        tone: "formal"
    },
    {
        id: 2,
        location: "Los Angeles",
        listing: "Amazing luxury villa in LA...",
        tone: "promotional"
    }
];

function loadHistory() {
    const container = document.getElementById("historyList");
    container.innerHTML = "";

    if (historyData.length === 0) {
        container.innerHTML = "<p>No history available.</p>";
        return;
    }

    historyData.forEach(item => {
        const card = document.createElement("div");
        card.className = "history-card";

        card.innerHTML = `
            <h3>${item.location}</h3>
            <p><strong>Listing:</strong> ${item.listing}</p>
            <p><strong>Tone:</strong> ${item.tone}</p>
            <button class="delete-btn" onclick="deleteItem(${item.id})">Delete</button>
        `;

        container.appendChild(card);
    });
}

function deleteItem(id) {
    historyData = historyData.filter(item => item.id !== id);
    loadHistory();
}

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

// Load on start
loadHistory();