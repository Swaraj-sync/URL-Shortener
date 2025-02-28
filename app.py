import string
import random
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

# In-memory dictionary for short_code -> original_url
url_map = {}

def generate_short_code(length=6):
    """Generate a random short code."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

@app.route("/", methods=["GET"])
def index():
    """Show the index page (URL shortener form)."""
    return render_template("index.html")

@app.route("/", methods=["POST"])
def create_short_url():
    """
    Handle the form submission or fetch request:
    - Retrieve 'original_url' from form data.
    - Generate a short code.
    - Store in the dictionary.
    - Return the short link as plain text.
    """
    original_url = request.form.get("original_url")
    if not original_url:
        return "No URL provided", 400

    # Generate a short code that’s not already in use
    short_code = generate_short_code()
    while short_code in url_map:
        short_code = generate_short_code()

    # Store it in the dictionary
    url_map[short_code] = original_url

    # Return the full short URL as text (the client script uses this)
    return request.host_url + short_code

@app.route("/<short_code>")
def redirect_to_original(short_code):
    """Redirect the user to the original URL for the given short code."""
    original_url = url_map.get(short_code)
    if original_url:
        return redirect(original_url)
    return "Invalid short URL.", 404

if __name__ == "__main__":
    # Bind to 0.0.0.0 and use the PORT environment variable (default to 10000 if not set)
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)
