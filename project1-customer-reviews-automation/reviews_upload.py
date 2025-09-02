#!/usr/bin/env python3

import os
import requests

# 1. Define the directory where text files are stored
directory = "/data/feedback"

# 2. Iterate through each file in the directory
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)

    # Open only if it's a .txt file
    if filename.endswith(".txt"):
        with open(filepath, "r") as f:
            # 3. Read lines from the file
            lines = f.read().splitlines()

            # 4. Convert file data into a dictionary
            review_dict = {
                "title": lines[0],
                "name": lines[1],
                "date": lines[2],
                "feedback": " ".join(lines[3:])
            }

            # 5. Define the URL of the web service
            url = "http://<server-ip-or-localhost>/feedback/"

            # 6. Send POST request with dictionary as JSON
            response = requests.post(url, json=review_dict)

            # 7. Check if upload was successful
            if response.status_code == 201:
                print(f"Successfully uploaded {filename}")
            else:
                print(f"Failed to upload {filename}. Status code: {response.status_code}")
