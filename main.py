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
    import urllib.parse
    video_id = urllib.parse.parse_qs(urllib.parse.urlparse(video_url).query).get("v", [None])[0]
    if not video_id:
        video_id = video_url.split("/")[-1]

    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    cleaned = "\n".join([t['text'] for t in transcript])
    return cleaned

    except Exception as e:
        return f"Error: {e}", 500
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
