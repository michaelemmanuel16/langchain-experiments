# YouTube AI Assistant with Streamlit

This is a Python script showcasing the **YouTube AI Assistant** using the Streamlit framework. The AI Assistant can answer questions based on a YouTube video's transcript. It employs the LangChain library for document processing, embeddings, and chat models, along with OpenAI's GPT-3.5 Turbo model for generating responses.

## Introduction

The YouTube AI Assistant offers informative responses to questions about a YouTube video's transcript. By processing the transcript and employing AI-powered chat models, the assistant generates detailed and contextually relevant answers.

## Features

- Retrieve transcript and process it into a vector database.
- Input questions about the YouTube video.
- Generate informative, contextually relevant responses.
- Utilize OpenAI's GPT-3.5 Turbo model for responses.
- Presented as a Streamlit web app for easy interaction.

## Usage
1. Run the Streamlit application:
   ```
   streamlit run youtube.py
2. Open the provided link in your web browser to access the Streamlit app.
3. In the sidebar, enter the URL of the YouTube video for transcript analysis.
4. In the main interface, type your question about the video in the input box.
5. Click "Get Response" to obtain the AI-generated answer.
6. The response will be displayed below the button.