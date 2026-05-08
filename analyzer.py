import os
import re
import time
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def get_video_id(url):
    match = re.search(r"(?:v=|youtu\.be/)([A-Za-z0-9_-]{11})", url)
    return match.group(1) if match else None


def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
        return " ".join(seg["text"] for seg in transcript)
    except Exception:
        return None


def call_with_retry(chain, inputs, retries=3):
    for i in range(retries):
        try:
            return chain.invoke(inputs)
        except Exception:
            time.sleep(2)
    raise Exception("API failed after retries")


def analyze(url, title=""):
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.3,
        groq_api_key=os.getenv("GROQ_API_KEY")
    )

    video_id = get_video_id(url)
    if not video_id:
        return {"error": "Invalid YouTube URL."}

    transcript = get_transcript(video_id)

    # fallback → use title
    if transcript:
        content = transcript
        source = "transcript"
    elif title:
        content = title
        source = "title"
    else:
        return {"error": "No transcript available and no title fallback."}

    prompt = PromptTemplate(
        input_variables=["text"],
        template="""
Analyze this YouTube content and give:

SUMMARY:
Short summary

KEY_POINTS:
- Point 1
- Point 2
- Point 3

IMPROVEMENTS:
- Suggestion 1
- Suggestion 2

RELEVANCE:
Why it matters today

Content:
{text}
"""
    )

    chain = prompt | llm | StrOutputParser()
    result = call_with_retry(chain, {"text": content[:8000]})

    return {"result": result, "source": source}


def get_sentiment(url):
    try:
        import yt_dlp
        with yt_dlp.YoutubeDL({"quiet": True}) as ydl:
            info = ydl.extract_info(url, download=False)
            likes = info.get("like_count", 0)
            views = info.get("view_count", 1)

            ratio = (likes / views) * 100

            if ratio > 8:
                sentiment = "😊 Positive"
            elif ratio > 3:
                sentiment = "😐 Neutral"
            else:
                sentiment = "😟 Negative"

            return info, sentiment
    except:
        return {}, "Unknown"