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
