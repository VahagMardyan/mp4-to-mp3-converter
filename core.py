import os
from moviepy.editor import VideoFileClip

DESKTOP_DIR = os.path.join(os.path.expanduser("~"),"Desktop")

def convert_video_to_mp3(file_storage) -> tuple[str, bool]:
    try:
        if file_storage.filename == "":
            return ("No file selected", False)
        video_path = os.path.join(DESKTOP_DIR, file_storage.filename)
        mp3_path = os.path.join(
            DESKTOP_DIR,
            os.path.splitext(file_storage.filename)[0] + ".mp3"
        )

        file_storage.save(video_path)
        video_clip = VideoFileClip(video_path)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(mp3_path)

        audio_clip.close()
        video_clip.close()

        return ("mp3 file saved on Desktop", True)
    except Exception as e:
        return (str(e), False)
    
