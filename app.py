from flask import Flask, render_template, request, jsonify
from core import convert_video_to_mp3

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/", methods = ["GET"])
def index():
    return render_template("index.html")

@app.route("/convert", methods = ["POST"])
def convert():
    if "video-name" not in request.files:
        return jsonify({
            "success" : False,
            "message" : "No file in request"
        })
    file = request.files["video-name"]
    message, success = convert_video_to_mp3(file)

    return jsonify({
        "success"  : success,
        "message" : message
    })

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)