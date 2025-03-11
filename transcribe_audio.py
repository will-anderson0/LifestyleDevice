import subprocess
import os

# Runs Whisper to transcribe speech from an audio file.
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

        transcription = result.stdout.strip()
        print(f"✅ Transcription: {transcription}")
        return transcription

    except FileNotFoundError:
        print(f"❌ Error: Whisper executable not found at {whisper_path}")
        return None
