# AI Email Automation

An AI-powered automation workflow that reads emails from Gmail, analyzes them using AI, and converts important messages into actionable tasks.

## Features

* Connects to Gmail using the Gmail API
* Uses AI to summarize incoming emails
* Extracts action items from messages
* Stores tasks in a local SQLite database
* Runs as a Python automation workflow

## Tech Stack

* Python
* Gmail API
* OpenAI API
* SQLite

## Project Structure

ai-email-automation
│
├── main.py — Main workflow runner
├── gmail_reader.py — Reads emails from Gmail API
├── ai_processor.py — Processes email content using AI
├── slack_sender.py — Sends notifications (optional)
├── database.py — Handles SQLite storage
├── tasks.db — Local database file
├── requirements.txt — Python dependencies

## How to Run

1. Clone the repository
   git clone https://github.com/Muazsuhaib/AI-email-automation.git

2. Navigate into the project folder
   cd AI-email-automation

3. Install dependencies
   pip install -r requirements.txt

4. Configure environment variables for API keys

5. Run the automation
   python main.py

## Author

Muaz
