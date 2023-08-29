# Celebrity Search Result using OpenAI Language Models

This Python script utilizes OpenAI's language models to provide information about celebrities based on user input. It employs the LangChain library to construct a chain of interactions with the model, enabling the extraction of details about a celebrity's name, date of birth (DOB), and significant events related to their DOB.

## Introduction

The **Celebrity Search Result** script employs OpenAI's language models and LangChain's conversational structure to gather information about celebrities. It prompts the user for a celebrity's name, retrieves the celebrity's DOB, and then provides significant events that occurred around their DOB.

## Features

- Interactive conversation with the user using OpenAI's language models.
- Extracts celebrity information such as name, DOB, and significant events.
- Utilizes LangChain to manage conversation flow and memory.
- Presented as a Streamlit web application for easy interaction.

## Usage
1. Run the Streamlit application:
   ```bash
   streamlit run main.py
2. Open the provided link in your web browser to access the Streamlit app.
3. Enter the celebrity's name in the input box.
4. The app will display the celebrity's DOB and significant events related to their DOB.