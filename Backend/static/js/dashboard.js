function goToGenerate() {
    window.location.href = "/generate";
}

function goToHistory() {
    window.location.href = "/history";
}

document.getElementById("logoutBtn").addEventListener("click", function(e) {
    e.preventDefault();

    fetch("/api/logout", {
        method: "POST"
    })
    .then(() => {
        window.location.href = "/login";
    });
});