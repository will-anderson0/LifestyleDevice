from transcribe import transcribe_audio
from habit_analysis import analyze_habits
from record_audio import record_audio
import os
import time

def main():
    try:
        chunk_counter = 0
        while True:
            # Generate a unique filename for each recording
            filename = os.path.join("recordings/", f"chunk_{chunk_counter}.wav")
            record_audio(filename)
            transcription = transcribe_audio(filename)

            if transcription:
                print(f"✅ Transcription Output: {transcription}")
                with open("transcriptions.log", "a") as log_file:
                    log_file.write(f"[Chunk {chunk_counter}] {transcription}\n")

            chunk_counter += 1
            time.sleep(0.5)  # Small delay to avoid overlapping recordings

    except KeyboardInterrupt:
        print("\nStopping continuous recording.")

if __name__ == "__main__":
    main()