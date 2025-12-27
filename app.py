from flask import Flask, render_template, request, jsonify
from core import convert_video_to_mp3
import os

app = Flask(__name__, static_folder="static", template_folder="templates")

ALLOWED_EXTENSIONS = {".mp4", ".mkv", ".avi", ".mov", ".webm"}

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

    
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        return jsonify({
            "success" : "False",
            "message" : "Invaild video format. Only .mp4, .mkv, .avi, .mov and .webm are allowed"
        })

    message, success = convert_video_to_mp3(file)

    return jsonify({
        "success"  : success,
        "message" : message
    })

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)