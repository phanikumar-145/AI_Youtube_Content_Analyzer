import streamlit as st
import os
import re
from dotenv import load_dotenv
from analyzer import analyze, get_sentiment

load_dotenv()

st.set_page_config(page_title="YouTube Analyzer", page_icon="🎬", layout="wide")

st.title("🎬 YouTube Video Analyzer")
st.caption("Powered by LangChain + Groq LLaMA 3.3 70B")
st.divider()

# ✅ FIX: correct API key check
if not os.getenv("GROQ_API_KEY"):
    st.error("⚠️ GROQ_API_KEY not found. Add it to your .env file.")
    st.stop()

url = st.text_input("🔗 Paste YouTube URL", placeholder="https://www.youtube.com/watch?v=...")
analyze_btn = st.button("🚀 Analyze Video", type="primary")

if analyze_btn and url.strip():

    # 🔹 Step 1 — Metadata + sentiment
    with st.spinner("Fetching video info..."):
        meta, sentiment_label = get_sentiment(url.strip())

    # 🎥 Title
    if meta.get("title"):
        st.subheader(f"🎥 {meta['title']}")

    # 📊 Metrics row
    col1, col2, col3, col4 = st.columns(4)

    if meta.get("uploader"):
        col1.metric("Channel", meta["uploader"])

    if meta.get("view_count"):
        col2.metric("Views", f"{int(meta['view_count']):,}")

    if meta.get("like_count"):
        col3.metric("Likes", f"{int(meta['like_count']):,}")

    # Sentiment box
    col4.metric("Sentiment", sentiment_label)

    st.divider()

    # 🔹 Step 2 — AI Analysis
    with st.spinner("Analyzing video..."):
        result = analyze(url.strip(), title=meta.get("title", ""))

    if result.get("error"):
        st.error(f"❌ {result['error']}")
    else:

        # ⚠️ Show fallback warning
        if result.get("source") == "title":
            st.warning("Analysis based on video....")

        # 📄 Extract sections manually
        text = result["result"]

        summary = re.search(r"SUMMARY:(.*?)(KEY_POINTS:|$)", text, re.DOTALL)
        key_points = re.search(r"KEY_POINTS:(.*?)(IMPROVEMENTS:|$)", text, re.DOTALL)
        improvements = re.search(r"IMPROVEMENTS:(.*?)(RELEVANCE:|$)", text, re.DOTALL)
        relevance = re.search(r"RELEVANCE:(.*)", text, re.DOTALL)

        # Row 1
        c1, c2 = st.columns(2)

        with c1:
            st.subheader("📋 Summary")
            st.write(summary.group(1).strip() if summary else "Not available")

        with c2:
            st.subheader("🌍 Relevance Today")
            st.write(relevance.group(1).strip() if relevance else "Not available")

        st.divider()

        # Row 2
        c3, c4 = st.columns(2)

        with c3:
            st.subheader("🔑 Key Points")
            if key_points:
                for line in key_points.group(1).split("\n"):
                    line = line.strip()
                    if line:
                        clean = re.sub(r"^\d+[\.\)]\s*", "", line)
                        st.markdown(f"- {clean}")

        with c4:
            st.subheader("💡 Improvements")
            if improvements:
                for line in improvements.group(1).split("\n"):
                    line = line.strip()
                    if line:
                        clean = re.sub(r"^\d+[\.\)]\s*", "", line)
                        st.markdown(f"- {clean}")

elif analyze_btn:
    st.warning("Please enter a YouTube URL first.")