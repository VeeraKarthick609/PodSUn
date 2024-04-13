from flask import Flask, request, jsonify
from utils.download_audio import download_audio_from_url
from utils.transcribe import transcribe_audio

app = Flask(__name__)

@app.route("/", methods=["POST"])
def get_url():
    try:
        # Get JSON data from request body
        request_data = request.get_json()

        # Check if 'url' key is present in the JSON data
        if 'url' not in request_data:
            return jsonify({"error": "URL parameter is missing."}), 400

        # Extract URL from JSON data
        audio_url = request_data['url']

        # Download audio and get the file name
        file_name = download_audio_from_url(audio_url)
        print("File downloaded")   

        if file_name is None:
            return jsonify({"error": "Failed to download audio from the provided URL."}), 500

        # Transcribe
        print(file_name)
        text = transcribe_audio(file_name=file_name)
        print("transcribe done!!!")
        if text is None:
            return jsonify({"error": "Failed to transcribe audio."}), 500

        # Prepare server response
        response = {"transcribed_text": text}
        return jsonify(response)

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
