# Jarvis - A Python Voice Assistant

A simple yet powerful voice assistant built in Python, inspired by Iron Man's J.A.R.V.I.S. This assistant can perform various tasks based on voice commands, leveraging Google's Speech Recognition and Gemini AI for intelligent responses.

## Features

- **Voice-activated:** Listens for the wake word "Jarvis" to start taking commands.
- **Web Browsing:** Opens Google and performs web searches.
- **YouTube Integration:** Plays videos or music on YouTube.
- **News Headlines:** Fetches and reads the latest news headlines from BBC News.
- **AI-Powered Conversations:** Answers general questions and engages in conversation using Google's Gemini AI.
- **Conversational Memory:** Remembers the context of the current conversation for natural follow-up questions.
- **Chat Reset:** Allows clearing the AI's memory to start a fresh conversation.
- **Secure API Key Handling:** Uses a `.env` file to securely store the API key.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

- Python 3.8+
- A microphone connected to your computer.
- A Google AI API key. You can get one from Google AI Studio.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd major-project-jarvis
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate

    # For Windows
    python -m venv .venv
    .venv\Scripts\activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```
 
4.  **Set up your environment variables:**
    Copy the example environment file and then edit the new `.env` file to add your API key.
    ```bash
    cp .env.example .env
    ```
    ```
    GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
    ```

## Usage

Run the main script to start the assistant:

```bash
python main.py
```

The assistant will initialize and start listening for the wake word "Jarvis". Once it hears the wake word, it will listen for your command.

### Example Commands

- "Jarvis, what is the capital of France?"
- "Jarvis, open Google."
- "Jarvis, play a song by Queen."
- "Jarvis, tell me the latest news."
- "Jarvis, new chat."
- "Jarvis, shutdown."