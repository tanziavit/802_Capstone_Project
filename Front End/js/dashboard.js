document.addEventListener("DOMContentLoaded", function () {

    window.goToGenerate = function () {
        window.location.href = "generate.html";
    };

    window.goToHistory = function () {
        window.location.href = "history.html";
    };

    document.getElementById("logoutBtn").addEventListener("click", function(e) {
        e.preventDefault();

        localStorage.removeItem("user");

        window.location.href = "login.html";
    });

});