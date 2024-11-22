"""
mega_api.py

A simple Flask application that provides an endpoint to start downloads 
from MEGA links. The application listens for POST requests and processes 
the provided MEGA links to initiate downloads. This module is intended 
for lightweight API interactions to handle MEGA file downloads.

Features:
- `/download` endpoint to trigger downloads via MEGA links.
- Configurable download path (currently hardcoded as "/downloads").
- Utilizes subprocess to run shell commands for the download process.

Usage:
- Start the application by running this script.
- Send a POST request to the `/download` endpoint with a JSON payload 
  containing the `mega_link` key to initiate a download.

Requirements:
- Flask
- MEGA Command-Line Interface (CLI) tools (optional, commented out in code).
"""

import subprocess
from flask import Flask, request

app = Flask(__name__)


@app.route("/download", methods=["POST"])
def download():
    """
    Endpoint to start a download from a MEGA link.

    This endpoint accepts a POST request with a JSON payload containing
    a `mega_link` key. It initiates the download process for the given link
    using a predefined command.

    Returns:
        dict: A JSON response indicating the status of the request.
        - On success, returns {"message": "Download started"} with a 200 status code.
        - On failure, returns {"error": "No link provided"} with a 400 status code.
    """
    data = request.json
    if "mega_link" not in data:
        return {"error": "No link provided"}, 400
    mega_link = data["mega_link"]
    download_path = "/downloads"
    command = f"echo {mega_link}, {download_path}"
    # command = f"megadl --path {download_path} {mega_link}"
    subprocess.run(command, shell=True, check=False)
    return {"message": "Download started"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
