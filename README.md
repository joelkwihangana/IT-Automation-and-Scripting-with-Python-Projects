# Project 1 - Customer Reviews Automation

## Problem
Convert text files of customer reviews into JSON and upload them to the company's Django web service.

## Solution Steps
1. Use Python `os` module to loop through `.txt` files in a directory.
2. Read each file and split the content into lines.
3. Store the content in a Python dictionary with keys: title, name, date, feedback.
4. Send the dictionary as JSON to the web service using `requests.post()`.
5. Check HTTP response codes to confirm success.

## Key Learnings
- File I/O (`open`, `read`, `splitlines`)
- Python dictionaries for structured data
- JSON formatting via `requests.post(json=...)`
- HTTP status codes and error handling

