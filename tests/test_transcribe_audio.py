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
    assert result == "I'll be traveling to Europe very soon for summer vacation and I'm very excited to go. This will be my first time going. Wish me luck.", "Transcription should match the expected output."

# Test if transcription returns None for missing audio files.
def test_invalid_audio_path():
    result = transcribe_audio("recordings/nonexistent.wav")
    assert result is None, "Transcription should return None for missing audio files."

# Test if transcription returns None for empty audio files.
def test_empty_audio_file():
    result = transcribe_audio("recordings/empty.wav")
    assert result is None, "Transcription should return None for empty audio files."

# Test if on corrupted audio file.
def test_currupted_audio_file():
    result = transcribe_audio("recordings/corrupted_audio.wav")
    assert result is None, "Transcription should return None for corrupted audio files."

# Test if on audio file with differnt sample rate.
def test_wrong_sample_rate_audio_file():
    result = transcribe_audio("recordings/wrong_sample_rate.wav")
    assert result == "Hi, my name is Will, and this is a test for 12 Hertz item.", "Transcription should return None for audio files with wrong sample rate."