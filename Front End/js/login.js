document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("loginForm").addEventListener("submit", function(e) {
        e.preventDefault();

        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;

        if (!email || !password) {
            alert("Please fill all fields");
            return;
        }

        // Dummy login logic (optional check)
        if (email === "test@example.com" && password === "123456") {
            // Redirect to dashboard
            window.location.href = "dashboard.html";
        } else {
            alert("Invalid email or password");
        }
    });
});