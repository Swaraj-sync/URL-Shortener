document.addEventListener("DOMContentLoaded", function() {
    const urlForm = document.getElementById("url-form");
    const shortenedUrlDiv = document.getElementById("shortened-url");
    const shortUrlAnchor = document.getElementById("short-url");

    urlForm.addEventListener("submit", function(event) {
        event.preventDefault();

        const formData = new FormData(urlForm);

        fetch("/shorten", {
            method: "POST",
            body: new URLSearchParams(formData)
        })
            .then(response => {
                if (!response.ok) throw new Error("Failed to shorten URL");
                return response.text();
            })
            .then(shortUrl => {
                shortUrlAnchor.textContent = shortUrl;
                shortUrlAnchor.href = shortUrl;
                shortenedUrlDiv.classList.remove("hidden");
            })
            .then(response => response.json())
            .catch(error => {
                console.error(error);
            });
    });
});
