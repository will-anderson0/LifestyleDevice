import sounddevice as sd
import numpy as np
import wave
import os

# Set recording parameters
DURATION = 30  # Record for 30 seconds
SAMPLE_RATE = 16000  # 16 kHz sample rate (Whisper standard)
CHANNELS = 1  # Mono audio

# Records a 30-second audio chunk and saves it with a sequential filename.
def record_audio(filename):
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
