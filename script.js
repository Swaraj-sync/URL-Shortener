document.addEventListener("DOMContentLoaded", function() {
    const urlForm = document.getElementById("url-form");
    const originalUrlInput = document.getElementById("original-url");
    const shortenBtn = document.getElementById("shorten-btn");
    const shortUrlContainer = document.getElementById("short-url-container");
    const shortUrlPara = document.getElementById("short-url");

    shortenBtn.addEventListener("click", function(event) {
        event.preventDefault();
        const originalUrl = originalUrlInput.value.trim();
        if (originalUrl) {
            fetch("/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded"
                },
                body: `original_url=${originalUrl}`
            })
           .then(response => response.text())
           .then(shortUrl => {
                shortUrlPara.textContent = shortUrl;
                shortUrlContainer.style.display = "block";
            })
           .catch(error => console.error(error));
        }
    });
});
