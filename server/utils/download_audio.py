from pytube import YouTube
from moviepy.editor import *
from datetime import datetime
import os

# Function to download audio
def download_audio_from_url(url: str) -> str:
    """
    Function to download audio in mp3 format from the given url

    Params:
    -------
    - url: str -> Url of the source

    Returns:
    --------
    - file_path: str -> returns the filename of the downloaded file 
    """ 

    try:
        # Download audio
        yt = YouTube(url=url)
        stream = yt.streams.filter(only_audio=True).first()

        # Check if stream is available
        if stream:
            # Save the audio
            os.makedirs("./outputs/", exist_ok=True)
            filename = f"{str(datetime.now())}.mp3"
            file_path = os.path.join("./outputs/", filename)

            stream.download(output_path="./outputs/", filename=filename)

            return file_path
        else:
            raise Exception("No audio stream available for the given URL.")
    except Exception as e:
        # Handle exceptions
        print(f"Error occurred: {e}")
        return None

# Example usage
"""url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Example YouTube URL
downloaded_file = download_audio_from_url(url)
if downloaded_file:
    print(f"Audio downloaded successfully: {downloaded_file}")
else:
    print("Failed to download audio.")
"""