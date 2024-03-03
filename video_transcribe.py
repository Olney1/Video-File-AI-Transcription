import subprocess
from pathlib import Path
import whisper

# This is a simple script to extract audio from a video and transcribe it using the OpenAI open-source neural network called Whisper that approaches human level robustness and accuracy on English speech recognition.
# (https://openai.com/research/whisper)

def extract_audio(video_path):
    # Here we are using ffmpeg to extract audio from the video
    audio_path = Path(video_path).stem + '.wav'
    cmd = ['ffmpeg', '-i', video_path, '-ab', '160k', '-ac', '2', '-ar', '44100', '-vn', audio_path]
    subprocess.run(cmd, check=True)
    return audio_path

def transcribe_audio(audio_path):
    # Here we are using the whisper library to transcribe the audio
    model = whisper.load_model("base")  # You can choose different model sizes based on your needs
    result = model.transcribe(audio_path)
    return result['text']

# Example usage must be mp4 file
video_path = 'path/to/your/video.mp4'
audio_path = extract_audio(video_path)
transcription = transcribe_audio(audio_path)

# We print the transcription to the console but you can save it to a file or use it in any other way
print(transcription)

# Example of saving the transcription to a text file
with open('transcription.txt', 'w') as file:
    file.write(transcription)