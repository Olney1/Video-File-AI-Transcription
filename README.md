# Video Transcription with OpenAI's Whisper

This Python script allows you to extract audio from a video file and transcribe it into text using OpenAI's Whisper model. Whisper is an open-source neural network that approaches human-level robustness and accuracy on English speech recognition tasks. Learn more about Whisper [here](https://openai.com/research/whisper).

## Features

- **Audio Extraction:** Utilizes `ffmpeg` to extract audio from video files.
- **Speech to Text:** Leverages the Whisper model for accurate transcription.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.6 or higher
- `ffmpeg` - For audio extraction from video
- Whisper Python library - For transcribing audio to text

You can install the Whisper library using pip:

```bash
pip install openai-whisper
