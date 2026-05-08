# test_transcript.py
# Run this to see exactly what transcripts are available for your video

from youtube_transcript_api import YouTubeTranscriptApi
import re

url = input("Paste YouTube URL: ").strip()

# Extract video ID
match = re.search(r"(?:v=|youtu\.be/)([A-Za-z0-9_-]{11})", url)
if not match:
    print("❌ Invalid URL")
    exit()

video_id = match.group(1)
print(f"\n✅ Video ID: {video_id}")

try:
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    print("\n📋 Available transcripts:")
    for t in transcript_list:
        print(f"  - Language: {t.language} ({t.language_code}) | Auto-generated: {t.is_generated}")
except Exception as e:
    print(f"\n❌ Error: {e}")
    print("\n💡 Possible reasons:")
    print("  1. The video has no captions at all")
    print("  2. YouTube is rate-limiting your IP — wait a few minutes and retry")
    print("  3. The video is age-restricted or private")
    print("  4. Try: pip install --upgrade youtube-transcript-api")