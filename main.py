import os
from flask import Flask, render_template, request, redirect
from moviepy.editor import *

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

def script(message,link):
    return f"<script>window.alert('{message}'); window.location.href='{link}'</script>"

@app.route('/', methods=['GET','POST'])
def convertToMp3():
    if 'video-name' in request.files:
        video_file = request.files['video-name']
        if video_file.filename != '':
            deskop_path = os.path.join(os.path.expanduser('~'),'Desktop')
            video_path = os.path.join(deskop_path,video_file.filename)
            mp3_path = os.path.join(deskop_path,os.path.splitext(video_file.filename)[0]+'.mp3')
            try :
                video_file.save(video_path)
                video_clip = VideoFileClip(video_path)
                audio_clip = video_clip.audio
                audio_clip.write_audiofile(mp3_path)
                video_clip.close()
                message = 'The mp3 file saved on your desktop.'
                link = 'http://localhost:8000'
                return script(message,link)
            except Exception as error:
                return f"Error: {error}"
  
    return "Error: File not found or form not submitted properly. Please choose a video file."

if __name__ == '__main__':
    app.run(host='localhost', port=8000, debug=True)