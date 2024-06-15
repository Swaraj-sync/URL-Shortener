from flask import Flask, request, redirect, url_for, render_template
import uuid

app = Flask(__name__)


shortened_urls = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['original_url']
        short_code = str(uuid.uuid4())[:6]  
        shortened_urls[short_code] = original_url
        return render_template('index.html', short_url=f"http://localhost:5000/{short_code}")
    return render_template('index.html')

@app.route('/<short_code>')
def redirect_url(short_code):
    original_url = shortened_urls.get(short_code)
    if original_url:
        return redirect(original_url)
    return 'Invalid short code', 404

if __name__ == '__main__':
    app.run(debug=True)