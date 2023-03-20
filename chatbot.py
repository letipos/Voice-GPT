import openai
import pyttsx3
import speech_recognition as sr
import os
import gradio as gr
import configparser
import random
import time 



# Set the API key with config file
openai.api_key = os.environ["OPENAI_API_KEY"]


engine = pyttsx3.init()


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






def main():

    with gr.Blocks() as demo:

        gr.Markdown("""<h1><center>ChatGPT Voice Bot with OpenAI and Gradio Demo </center></h1>
            """)
        chatbot = gr.Chatbot()
        state = gr.State()
        #msg = gr.Textbox(placeholder = prompt)
        rec_button = gr.Button(value="Record audio")
        clear = gr.Button("Clear")

        def promt(rec_button):
            text = "Say something..."
            print(text)
            return gr.update(value=text, visible=True)
        
        def rec(history):
            history = history or []
            filename ="input.wav"
            print("Start recording...")
            with sr.Microphone() as source:
                recognizer=sr.Recognizer()
                source.pause_threshold=1
                audio=recognizer.listen(source,phrase_time_limit=None,timeout=None)

                with open(filename,"wb")as f:
                    f.write(audio.get_wav_data())  
            #transcript audio to test 
            text=transcribe_audio_to_text(filename)
            print("Recognized: ", text)
            history = history + [[text, None]]
            return history, history, gr.update(value="Responding...", visible=True)

        def speak_text(text):
            engine.say(text)
            engine.runAndWait()

        def bot(history):
                history = history or []
                print(history)
                try:
                    response = generate_response(history)    
                    history[-1][1] = response
                    time.sleep(3)

                except Exception as e:
                    print("An error ocurred : {}".format(e))
                    history[-1][1] = str(e)
                    return history, history, gr.update(value="Record audio", visible=True)
                #read resopnse using GPT3
                speak_text(response)

                return history, history, gr.update(value="Record audio", visible=True)
            

        #msg.submit(bot, inputs=state, outputs=[chatbot, state], queue=False).then(bot, inputs=state, outputs=[chatbot, state])
        

        rec_button.click(promt, rec_button, rec_button).then(rec, inputs=state, outputs=[chatbot, state, rec_button]).then(bot, inputs=state, outputs=[chatbot, state, rec_button])
        
        
        clear.click(lambda: None, None, chatbot, queue=False)
        demo.launch()  

if __name__=="__main__":
    main()

