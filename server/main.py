from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.summarizer import getLLAmaSummary
from utils.download_audio import download_audio_from_url
from utils.transcribe import transcribe_audio

app = Flask(__name__)

CORS(app)

@app.route("/", methods=["POST"])
def get_url():
    try:
        # Get JSON data from request body
        request_data = request.get_json()
        print("Got URL!!!")

        # Check if 'url' key is present in the JSON data
        if 'url' not in request_data:
            return jsonify({"error": "URL parameter is missing."}), 400

        # Extract URL from JSON data
        audio_url = request_data['url']
        print("Downloading audio!!!")
        print(audio_url)
        # Download audio and get the file name
        file_name = download_audio_from_url(audio_url)
        if file_name is None:
            return jsonify({"error": "Failed to download audio from the provided URL."}), 500
        print("Download completed!!!")

        print("Starting Transcribing!!!")
        # Transcribe
        """text = transcribe_audio(file_name=file_name)
        if text is None:
            return jsonify({"error": "Failed to transcribe audio."}), 500"""
        print("Done transcribing!!!")

        # Summarize the text
        #summarised_text = getLLAmaSummary(text)
        summarised_text = "Hey done with the summary"
        if summarised_text is None:
            return jsonify({"error": "Failed to summarize text."}), 500

        # Prepare server response
        response = {"summarized_text": summarised_text}
        return jsonify(response)

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
