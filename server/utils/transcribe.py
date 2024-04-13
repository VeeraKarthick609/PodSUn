import whisper

# Function to transcribe audio to text
def transcribe_audio(file_name: str) -> str:
    """
    Function that transcribes audio to text using OpenAI-whisper model

    Params:
    -------
    - file_name: str -> input audio file name

    Returns:
    --------
    - text: str -> transcribed text
    """

    try:
        model = whisper.load_model("tiny")
        transcribe = model.transcribe(file_name)
        text = transcribe["text"]
        return text
    except Exception as e:
        # Handle exceptions
        print(f"Error occurred during transcription: {e}")
        return None

# Example usage
"""audio_file = "example_audio.mp3"  # Example audio file name
transcribed_text = transcribe_audio(audio_file)
if transcribed_text:
    print(f"Transcription: {transcribed_text}")
else:
    print("Failed to transcribe audio.")
"""