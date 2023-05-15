from flask import Flask, send_file
import json
import base64

app = Flask(__name__)

@app.route("/ping", methods=['GET'])
def ping():
    return json.dumps({"status":"ok"}), 200

@app.route('/capture', methods=['GET'])
def capture():
    with open('classroom.jpg', 'rb') as image:
        return base64.b64encode(image.read()), 200

if __name__ == '__main__':
    app.run(debug=True)