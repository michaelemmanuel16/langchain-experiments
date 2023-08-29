# YouTube AI Assistant with Streamlit

This is a Python script showcasing the **YouTube AI Assistant** using the Streamlit framework. The AI Assistant can answer questions based on a YouTube video's transcript. It employs the LangChain library for document processing, embeddings, and chat models, along with OpenAI's GPT-3.5 Turbo model for generating responses.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [License](#license)

## Introduction

The YouTube AI Assistant offers informative responses to questions about a YouTube video's transcript. By processing the transcript and employing AI-powered chat models, the assistant generates detailed and contextually relevant answers.

## Features

- Retrieve transcript and process it into a vector database.
- Input questions about the YouTube video.
- Generate informative, contextually relevant responses.
- Utilize OpenAI's GPT-3.5 Turbo model for responses.
- Presented as a Streamlit web app for easy interaction.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/michaelemmanuel16/youtube-ai-assistant.git
   cd YouTube-AI-Assistant
2. Install required dependencies. It's recommended to set up a virtual environment:
   ```
   pip install -r requirements.txt
3. Ensure you have necessary API keys and access to required libraries.

## Usage
1. Run the Streamlit application:
   ```
   streamlit run script.py
2. Open the provided link in your web browser to access the Streamlit app.
3. In the sidebar, enter the URL of the YouTube video for transcript analysis.
4. In the main interface, type your question about the video in the input box.
5. Click "Get Response" to obtain the AI-generated answer.
6. The response will be displayed below the button.

## Dependencies
- Python >= 3.7
- LangChain (Installable via requirements.txt)
- OpenAI GPT-3.5 Turbo (API access required)
- Streamlit (Installable via requirements.txt)

Note: Valid API keys and access to required libraries are necessary for effective use.