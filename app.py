from flask import Flask, render_template, request, redirect
import os
import string
import random

app = Flask(__name__)

# In-memory short-code -> original-url map
url_map = {}

def generate_short_code(length=6):
    """Generate random short code of letters/digits."""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/shorten", methods=["POST"])
def create_short_url():
    original_url = request.form.get("original_url")
    if not original_url:
        return "Missing URL", 400

    short_code = generate_short_code()
    while short_code in url_map:
        short_code = generate_short_code()

    url_map[short_code] = original_url
    short_url = request.host_url + short_code
    return short_url

@app.route("/<short_code>")
def redirect_short_code(short_code):
    original_url = url_map.get(short_code)
    if not original_url:
        return "Invalid short URL.", 404
    return redirect(original_url)

if __name__ == "__main__":
    # Bind to 0.0.0.0 and use the PORT environment variable (default to 10000 if not set)
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)
