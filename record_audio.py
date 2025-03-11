import sounddevice as sd
import numpy as np
import wave
import os

# Set recording parameters
DURATION = 20  # Record for 20 seconds
SAMPLE_RATE = 16000  # 16 kHz sample rate (Whisper standard)
CHANNELS = 1  # Mono audio
OUTPUT_DIR = "./recordings/"  # Directory to save recordings

# Ensure recordings directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def record_audio(filename):
    """Records a 20-second audio chunk and saves it with a sequential filename."""

    print(f"Recording {DURATION} seconds... (Saving as {filename})")

    # Record audio
    audio = sd.rec(int(SAMPLE_RATE * DURATION), samplerate=SAMPLE_RATE, channels=CHANNELS, dtype='int16')
    sd.wait()

    print("✅ Recording complete. Saving audio file...")

    # Save as a .wav file using wave module
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(2)  # 16-bit PCM
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(audio.tobytes())

    print(f"✅ Audio saved as {filename}")
    return filename
