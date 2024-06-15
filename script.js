document.getElementById('url-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const originalUrl = document.getElementById('original-url').value;
    const shortenedUrlDiv = document.getElementById('shortened-url');
    const shortUrlElement = document.getElementById('short-url');

    fetch('/shorten', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url: originalUrl }),
    })
    .then(response => response.json())
    .then(data => {
        const shortUrl = `${window.location.origin}/${data.short_url}`;
        shortUrlElement.href = shortUrl;
        shortUrlElement.textContent = shortUrl;
        shortenedUrlDiv.classList.add('visible');
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
