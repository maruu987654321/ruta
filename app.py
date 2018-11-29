from flask import Flask, jsonify
import pytesseract
import os
port = int(os.environ.get('PORT', 5000))

try:
    import Image
except ImportError:
    from PIL import Image

app = Flask(__name__)

@app.route('/')
def homepage():
    # Basic OCR
    return(pytesseract.image_to_string(Image.open('1.jpg')).encode('utf-8'))

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)