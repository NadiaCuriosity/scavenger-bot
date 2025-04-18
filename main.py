from flask import Flask, request
from youtube_transcript_api import YouTubeTranscriptApi
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/get', methods=['GET'])
def get_transcript():
    video_url = request.args.get('url')
    if not video_url:
        return "Error: No URL provided", 400
    try:
        video_id = video_url.split("v=")[-1].split("&")[0]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        cleaned = "\n".join([t['text'] for t in transcript])
        return cleaned
    except Exception as e:
        return f"Error: {e}", 500
