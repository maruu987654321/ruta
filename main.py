from flask import Flask, jsonify
import pytesseract
import os
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
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
