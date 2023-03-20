# AI Chatbot with OpenAI's GPT-3

This is a Python program that allows users to interact with an AI chatbot using voice commands. The chatbot is powered by OpenAI's GPT-3 language model and uses speech recognition and text-to-speech technologies to facilitate conversations with the user. 

## Requirements
- OpenAI API key
- Python 3.x
- `openai`, `pyttsx3`, `speech_recognition`, and `pyaudio` Python packages

## Installation
1. Clone or download the repository to your local machine
2. Install the required Python packages using pip or conda
3. Set your OpenAI API key as an environment variable with the name `OPENAI_API_KEY`

## Usage
1. Run the `main()` function in the `chatbot.py` file
2. The program will prompt the user to say "Hey" to start recording their question
3. Once the user says "Hey", they can ask their question
4. The program will record the user's question, transcribe it into text, generate a response using GPT-3, and then read the response back to the user using text-to-speech technology
5. The conversation will continue until the user stops the program

## Acknowledgements
This program was developed with the help of OpenAI's GPT-3 language model, the `pyttsx3` text-to-speech library, and the `speech_recognition` and `pyaudio` speech recognition libraries.

# ChatGPT Voice Bot with OpenAI and Gradio

This project implements a voice-based chatbot using OpenAI's GPT-3 API and Gradio's user interface. The chatbot is capable of recognizing and transcribing voice inputs, generating responses to those inputs using GPT-3, and delivering those responses through a text-based user interface.

## Requirements
- OpenAI API key
- Python 3.x
- `openai`, `gradio`, `pyttsx3`, `speech_recognition`, and `pyaudio` Python packages

## Usage

To get started with this project, follow these steps:

1. Clone the repository to your local machine using `git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY`.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Set your OpenAI API key by adding `export OPENAI_API_KEY=yourkeyhere` to your environment variables, replacing "yourkeyhere" with your actual OpenAI API key.
4. Run the application by running `python app.py`.
5. Open the application in your web browser by navigating to `http://localhost:7860`.

## Usage

Once the application is running, you can use it to have a conversation with the chatbot. Follow these steps to start a conversation:

1. Click the "Record audio" button to begin recording your voice input.
2. Speak your message into the microphone.
3. Click the "Stop recording" button to stop recording your voice input.
4. Wait for the chatbot to generate a response.

You can clear the chat history at any time by clicking the "Clear" button.

## License

This project is licensed under the [MIT License](LICENSE).
