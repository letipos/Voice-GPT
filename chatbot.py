# Import required libraries
import openai
import pyttsx3
import speech_recognition as sr
import os
import gradio as gr

# Set the OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Define start and restart sequences for the chatbot prompt
start_sequence = "\nAI:"
restart_sequence = "\nHuman: "
prompt = "The following is a conversation with an AI. \n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you?\nHuman: "

def transcribe_audio_to_text(filename):
            recogizer=sr.Recognizer()
            with sr.AudioFile(filename)as source:
                audio=recogizer.record(source) 
            try:
                return recogizer.recognize_google(audio)
            except:
                print("skipping unkown error")
       # Define a function to generate a response using OpenAI's GPT-3

def generate_response(prompt):
    response= openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text      

# Define a function called "speak_text" that takes in text as input
def speak_text(text):
    # Use the text-to-speech engine to read the text aloud
    engine.say(text)
    engine.runAndWait()


def main():

    # Create a Gradio interface for the chatbot
    with gr.Blocks() as demo:

        # Add a title to the interface
        gr.Markdown("""<h1><center>ChatGPT Voice Bot with OpenAI and Gradio Demo </center></h1>""")

        # Create a chatbot instance and a state object
        chatbot = gr.Chatbot()
        state = gr.State()

        # Create a button to trigger audio recording
        rec_button = gr.Button(value="Record audio")

        # Create a button to clear the chat history
        clear = gr.Button("Clear")

        # Define a function to update the chat prompt when the record audio button is clicked
        def promt(rec_button):
            text = "Say something..."
            print(text)
            return gr.update(value=text, visible=True)

        # Define a function to record audio and transcribe it to text
        def rec(history):
            history = history or []
            filename ="input.wav"
            print("Start recording...")

            # Use SpeechRecognition library to record audio from microphone
            with sr.Microphone() as source:
                recognizer=sr.Recognizer()
                source.pause_threshold=1
                audio=recognizer.listen(source,phrase_time_limit=None,timeout=None)

                # Save audio to file
                with open(filename,"wb")as f:
                    f.write(audio.get_wav_data())  

            # Transcribe audio to text
            text=transcribe_audio_to_text(filename)
            print("Recognized: ", text)

            # Add user input to chat history
            history = history + [[text, None]]
            return history, history, gr.update(value="Responding...", visible=True)  
        

        # Define a function called "bot" that takes in the chat history as input
        def bot(history):
            # If history is not defined, initialize an empty list
            history = history or []
            # Print the chat history for debugging purposes
            print(history)
            try:
                # Generate a response from the OpenAI API using the chat history
                response = generate_response(history)
                # Add the response to the chat history
                history[-1][1] = response
                # Wait for 3 seconds to simulate typing time
                time.sleep(3)

            except Exception as e:
                # If an error occurs, print the error message and add it to the chat history
                print("An error occurred: {}".format(e))
                history[-1][1] = str(e)
                # Return the chat history and prompt the user to record audio again
                return history, history, gr.update(value="Record audio", visible=True)
            
        #msg.submit(bot, inputs=state, outputs=[chatbot, state], queue=False).then(bot, inputs=state, outputs=[chatbot, state])
        

        rec_button.click(promt, rec_button, rec_button).then(rec, inputs=state, outputs=[chatbot, state, rec_button]).then(bot, inputs=state, outputs=[chatbot, state, rec_button])
        
        
        clear.click(lambda: None, None, chatbot, queue=False)
        demo.launch()  

if __name__=="__main__":
    main()

