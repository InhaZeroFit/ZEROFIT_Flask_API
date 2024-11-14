from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from PIL import Image
import io
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def generate_image():
    return "Hello Python Flask!"

if __name__ == '__main__':
    app.run(port=5000)