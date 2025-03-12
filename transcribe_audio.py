import subprocess
import os
import re

# Runs Whisper to transcribe speech from an audio file and returns cleaned sentences
def transcribe_audio(filename="recordings/mock_audio.wav", model="whisper.cpp/models/ggml-tiny.bin"):
    whisper_path = os.path.abspath("whisper.cpp/build/bin/whisper-cli")
    model_path = os.path.abspath(model)
    file_path = os.path.abspath(filename)

    if not os.path.exists(whisper_path):
        print(f"❌ Whisper executable not found: {whisper_path}")
        return None

    print(f"Transcribing: {file_path}...")

    try:
        result = subprocess.run(
            [whisper_path, "-m", model_path, "-f", file_path],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            print(f"❌ Whisper failed: {result.stderr}")
            return None

        return clean_transcription(result.stdout.strip())

    except FileNotFoundError:
        print(f"❌ Error: Whisper executable not found at {whisper_path}")
        return None

# Cleans up Whisper output by removing chunk headers, timestamps, and unwanted markers
def clean_transcription(text):    
    lines = text.split("\n")
    cleaned_lines = []

    for line in lines:
        # Remove chunk headers and timestamps
        line = re.sub(r"\[Chunk \d+\] \[\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}\]", "", line)
        line = re.sub(r"\[\d{2}:\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}:\d{2}\.\d{3}\]", "", line)

        # Remove blank/inaudible markers
        if "[BLANK_AUDIO]" in line or "[INAUDIBLE]" in line:
            continue

        # Clean up spaces and only keep meaningful sentences
        line = line.strip()
        if line:
            cleaned_lines.append(line)

    return " ".join(cleaned_lines)  # Return cleaned transcription as a single paragraph
