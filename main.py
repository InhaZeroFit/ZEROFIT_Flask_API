from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

app_port = 5005

@app.route('/', methods=['GET'])
def get_server():
    return jsonify("Hello Flask Server!")  # JSON 형식으로 응답

@app.route('/user-image', methods=['GET'])
def get_user_name():
    # 응답 바디에 JSON 형식으로 message 포함
    response = {
        "message": "pretty!"
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=app_port)