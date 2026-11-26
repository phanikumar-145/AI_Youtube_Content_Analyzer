# AI YouTube Content Analyzer

## Project Overview

The AI YouTube Content Analyzer is an AI-powered application that analyzes YouTube videos and generates useful insights from their content.

Users provide a YouTube video URL, and the application retrieves the video transcript when available. It then uses the Llama 3.3 70B model through the Groq API to generate a summary, key points, improvement suggestions, and an explanation of the video's relevance.

The application also retrieves video metadata, including the channel name, views, and likes, and provides an engagement-based sentiment indication.

The frontend is built using Streamlit, while LangChain manages the interaction with the language model.

## Key Features

- Analyze YouTube videos using their URLs.
- Extract video transcripts when available.
- Generate AI-powered video summaries.
- Identify important points from video content.
- Generate content improvement suggestions.
- Explain the relevance of video content.
- Retrieve YouTube video metadata.
- Display channel name, views, and likes.
- Provide an engagement-based sentiment indication.
- Use video title as a fallback when transcript extraction is unavailable.
- Retry failed LLM requests.
- Interactive Streamlit dashboard.

## Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Frontend | Streamlit |
| Large Language Model | Llama 3.3 70B Versatile |
| LLM Provider | Groq |
| LLM Framework | LangChain |
| Transcript Extraction | YouTube Transcript API |
| Video Metadata | yt-dlp |
| Environment Management | Python dotenv |
| Text Processing | Regular Expressions |

## Project Architecture

The application follows a simple AI-powered content analysis workflow.

1. The user enters a YouTube video URL.
2. The application extracts the video ID from the URL.
3. yt-dlp retrieves available video metadata.
4. YouTube Transcript API attempts to retrieve the English transcript.
5. If the transcript is unavailable, the application uses the video title as a fallback when available.
6. LangChain constructs a prompt containing the video content.
7. Groq processes the prompt using Llama 3.3 70B.
8. The model generates the summary, key points, improvements, and relevance.
9. Streamlit displays the analysis results.

## Project Structure

```text
AI_Youtube_Content_Analyzer/
|
├── analyzer.py
├── app.py
├── requirements.txt
├── test_transcript.py
├── .gitignore
└── README.md
```

### File Description

| File | Description |
|---|---|
| analyzer.py | Handles video ID extraction, transcript retrieval, LLM analysis, retry logic, and engagement-based sentiment. |
| app.py | Streamlit frontend for entering YouTube URLs and displaying analysis results. |
| requirements.txt | Contains the Python dependencies required by the project. |
| test_transcript.py | Helps check which transcripts are available for a YouTube video. |
| .gitignore | Specifies files and folders that should not be tracked by Git. |
| README.md | Project documentation. |

## Analysis Components

### 1. Video Information

The application retrieves available video information, including:

- Video title.
- Channel name.
- Total views.
- Total likes.

### 2. Transcript Extraction

The YouTube Transcript API attempts to retrieve the English transcript of the video.

The extracted transcript is combined into a single text string for further analysis.

If transcript extraction fails, the application uses the video title as a fallback when available.

### 3. AI Video Summary

The LLM generates a short summary explaining the main content of the video.

### 4. Key Points

The application identifies important information and main ideas discussed in the video.

### 5. Content Improvements

The AI model provides suggestions for improving the analyzed content.

### 6. Relevance Analysis

The application explains why the video's content matters today.

### 7. Engagement-Based Sentiment

The application uses the ratio of likes to views to display an engagement-based sentiment indication.

The current thresholds are:

| Like-to-View Ratio | Displayed Sentiment |
|---|---|
| Above 8% | Positive |
| Above 3% and up to 8% | Neutral |
| 3% or below | Negative |

This is a simple engagement heuristic, not a true analysis of audience opinions or comments.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/phanikumar-145/AI_Youtube_Content_Analyzer.git
```

### 2. Navigate to the Project Directory

```bash
cd AI_Youtube_Content_Analyzer
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the Groq API Key

Create a `.env` file in the project directory:

```env
GROQ_API_KEY=your_groq_api_key
```

Replace the placeholder with your actual Groq API key.

Never upload your actual API key to GitHub.

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## Example Input

```text
https://www.youtube.com/watch?v=VIDEO_ID
```

Enter a valid YouTube video URL in the application and click the Analyze Video button.

## Example Analysis Output

The application generates the following sections:

### Summary

A short explanation of the video's main content.

### Key Points

Important topics and ideas discussed in the video.

### Improvements

Suggestions for improving the content.

### Relevance Today

An explanation of why the video content is useful or relevant.

### Video Metrics

Available channel, view, like, and engagement-based sentiment information.

## Transcript Testing

The project includes `test_transcript.py` to check available transcripts for a YouTube video.

Run it using:

```bash
python test_transcript.py
```

Enter a YouTube URL when prompted.

The script displays available transcript languages and whether the transcripts are automatically generated.

## Future Improvements

- Support multiple transcript languages.
- Add video comment analysis.
- Analyze audience feedback using sentiment analysis.
- Generate chapter-wise summaries.
- Add timestamp-based key points.
- Support long videos through transcript chunking.
- Generate downloadable analysis reports.
- Add video comparison functionality.
- Improve transcript extraction error handling.
- Add more detailed engagement analytics.

## Important Limitations

- Transcript extraction depends on transcript availability and YouTube access.
- When the transcript is unavailable, title-based analysis cannot provide the same depth as transcript-based analysis.
- The current analysis processes a maximum of 8,000 characters from the selected content.
- The sentiment indication is calculated from likes and views, not actual viewer comments.
- AI-generated summaries and suggestions may contain inaccuracies.

## Author

**Phani Kumar**

AI/ML and Generative AI Developer

GitHub: https://github.com/phanikumar-145
