import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

from transcribe_audio import transcribe_audio

@pytest.fixture
# Ensure a test audio file exists before running tests.
def test_audio():
    audio_file = "recordings/mock_audio.wav"
    model = "whisper.cpp/models/ggml-tiny.bin"

    if not os.path.exists(audio_file):
        pytest.skip("Skipping test: Test audio file missing.")

    if not os.path.exists(model):
        pytest.skip("Skipping test: Whisper model missing.")

    return audio_file

# Test if transcription runs successfully.
def test_transcription_runs(test_audio):
    result = transcribe_audio(test_audio)
    assert isinstance(result, str), "Transcription should return a string."
    assert len(result) > 0, "Transcription should not be empty."
    assert result == "Hi I will be travelling to Europe very soon for summer vacation.", "Transcription should match the expected output."


# Test if transcription returns None for missing audio files.
def test_invalid_audio_path():
    result = transcribe_audio("recordings/nonexistent.wav")
    assert result is None, "Transcription should return None for missing audio files."
