# AI YouTube Content Analyzer

## Project Overview

AI YouTube Content Analyzer is a Streamlit application that analyzes YouTube video content and generates an AI-written summary, key points, improvement suggestions, and an explanation of the content's relevance.

The application attempts to retrieve an English transcript using YouTube Transcript API. If a transcript is unavailable, it can use the video title as a limited fallback. It uses LangChain and the Groq-hosted Llama 3.3 70B model to generate the analysis.

The application also retrieves available video metadata through yt-dlp and calculates a like-to-view ratio. This ratio is displayed as an engagement indicator; it is not a measurement of actual audience sentiment.

## Features

- Accepts YouTube video URLs.
- Extracts the video ID from supported URL formats.
- Attempts to retrieve English video transcripts.
- Uses the video title as a fallback when a transcript is unavailable.
- Generates a video summary.
- Extracts key points.
- Suggests content improvements.
- Explains the video's relevance.
- Retrieves available video metadata such as title, channel, views, and likes.
- Displays a like-to-view engagement indicator.
- Uses retry logic for failed LLM requests.
- Provides an interactive Streamlit interface.

## Technology Stack

| Category | Technology |
|---|---|
| Language | Python |
| User interface | Streamlit |
| LLM provider | Groq |
| Model | Llama 3.3 70B Versatile |
| LLM orchestration | LangChain |
| Transcript retrieval | YouTube Transcript API |
| Video metadata | yt-dlp |
| Environment variables | python-dotenv |

## Project Structure

```text
AI_Youtube_Content_Analyzer/
├── analyzer.py
├── app.py
├── test_transcript.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## How It Works

1. The user enters a YouTube URL in the Streamlit interface.
2. The application extracts the 11-character video ID.
3. yt-dlp attempts to retrieve available video metadata.
4. YouTube Transcript API attempts to retrieve an English transcript.
5. If a transcript is available, the application uses up to the first 8,000 characters for analysis.
6. If no transcript is available but the video title is known, the title is used as a limited fallback.
7. LangChain sends the analysis prompt to the Groq Llama model.
8. The application displays the summary, key points, improvement suggestions, and relevance section.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/phanikumar-145/AI_Youtube_Content_Analyzer.git
cd AI_Youtube_Content_Analyzer
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Groq API key

Create a local `.env` file in the project root. Use `.env.example` as a template:

```env
GROQ_API_KEY=your_actual_groq_api_key
```

Get an API key from the Groq developer console. Do not commit `.env` or publish your API key.

### 5. Run the application

```bash
streamlit run app.py
```

Open the local URL printed by Streamlit in your browser.

## Usage

1. Start the Streamlit application.
2. Paste a supported YouTube video URL.
3. Select **Analyze Video**.
4. Wait for metadata retrieval and AI analysis.
5. Review the displayed summary, key points, improvements, relevance, and available video metrics.

## Transcript Diagnostic Script

The repository includes `test_transcript.py`, which helps inspect whether transcripts are available for a video.

Run:

```bash
python test_transcript.py
```

Paste a YouTube URL when prompted. The script lists available transcript languages when the API call succeeds.

## Engagement Indicator

The application calculates:

```text
like-to-view ratio = (likes / views) * 100
```

It displays:
- Positive when the ratio is greater than 8%.
- Neutral when the ratio is greater than 3% and up to 8%.
- Negative when the ratio is 3% or lower.

This is a simple engagement heuristic. It does not analyze viewer comments or determine the audience's actual emotional sentiment. Like counts may also be unavailable.

## Limitations

- Transcript retrieval depends on captions being available and accessible.
- The current transcript request is limited to English.
- Without a transcript, title-only analysis provides very limited information.
- Only the first 8,000 characters of available transcript text are sent for analysis.
- The engagement indicator is based on likes and views, not comment sentiment.
- YouTube metadata and transcript access may fail because of platform restrictions, rate limits, or video privacy settings.
- LLM-generated analysis may be incomplete or inaccurate and should be reviewed.

## Important Compatibility Note

The current `analyzer.py` calls `YouTubeTranscriptApi.get_transcript()`. The installed version of `youtube-transcript-api` may expose a different interface. If transcript retrieval fails after installation, check the installed library version and update the code to use the API supported by that version.

## Future Improvements

- Support transcript languages beyond English.
- Add chapter-wise summaries and timestamped key points.
- Add YouTube comment retrieval and actual comment sentiment analysis.
- Process long transcripts using chunking and map-reduce summarization.
- Use structured output validation for more reliable analysis sections.
- Improve URL validation and error reporting.
- Add downloadable summaries and analysis reports.
- Add video comparison and analysis history.

## Security and Responsible Use

- Keep the Groq API key in a local `.env` file.
- Never commit API keys or other secrets.
- Respect YouTube's terms and applicable copyright rules when retrieving and processing video content.
- Review generated summaries before relying on them.

## Author

**Phani Kumar**

AI/ML and Generative AI Developer

GitHub: https://github.com/phanikumar-145
