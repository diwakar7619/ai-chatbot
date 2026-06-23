# AI Chatbot

A conversational AI chatbot built with Python, Streamlit, and Groq's Llama model. The application provides a clean chat interface, supports multi-turn conversations using chat history, and securely manages API keys through environment variables.

## Live Demo

[Live Demo](https://ai-chatbot-zxmgwtvbr99cqdg6ejxcew.streamlit.app/)

## Features

* Conversational AI powered by Groq
* Multi-turn chat memory
* Streamlit chat interface
* Clear Chat functionality
* Environment variable support using `.env`
* GitHub version control and deployment-ready structure

## Tech Stack

* Python 3.13
* Streamlit
* Groq API
* Llama 3.3 70B Versatile
* python-dotenv
* uv
* Git & GitHub

## Project Structure

```text
ai-chatbot/
├── main.py
├── README.md
├── pyproject.toml
├── uv.lock
├── .gitignore
└── .env
```

## How It Works

1. User enters a message in the Streamlit chat interface.
2. Message is stored in Streamlit session state.
3. Entire conversation history is sent to Groq.
4. Groq generates a response using Llama 3.
5. Response is displayed and added to chat history.

## Local Setup

### Clone Repository

```bash
git clone https://github.com/diwakar7619/ai-chatbot.git
cd ai-chatbot
```

### Create Environment

```bash
uv sync
```

### Create Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

### Run Application

```bash
streamlit run main.py
```

## Learning Outcomes

This project helped me learn:

* LLM API integration
* Prompt and message structures
* Session state management
* Chat history handling
* Environment variable management
* Streamlit application development
* Git and GitHub workflows
* Cloud deployment basics

## Future Improvements

* Streaming responses
* Model selection dropdown
* Conversation export
* Usage analytics
* System prompts
* Dark/light theme customization

## Author

Pratham Diwakar

GitHub: https://github.com/diwakar7619
