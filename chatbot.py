import openai
import pyttsx3
import speech_recognition as sr
import os
import pyaudio


# Set the API key
openai.api_key = "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"


engine = pyttsx3.init()

def transcribe_audio_to_test(filename):
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
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response ["Choices"][0]["text"]
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        #Waith for user say "hey"
        print("Say 'Hey' to start recording your question")
        with sr.Microphone() as source:
            recognizer=sr.Recognizer()
            audio=recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower()=="hey":
                    #record audio
                    filename ="input.wav"
                    print("Say your question")
                    with sr.Microphone() as source:
                        recognizer=sr.Recognizer()
                        source.pause_threshold=1
                        audio=recognizer.listen(source,phrase_time_limit=None,timeout=None)
                        with open(filename,"wb")as f:
                            f.write(audio.get_wav_data())
                            
                            
                        
                        
                    #transcript audio to test 
                    text=transcribe_audio_to_test(filename)
                    if text:
                        print(f"yuo said {text}")
                        
                        #Generate the response
                        response = generate_response(text)
                        print(f"Chat GPT-3 says: {response}")
                            
                        #read resopnse using GPT3
                        speak_text(response)
            except Exception as e:
                
                print("An error ocurred : {}".format(e))
if __name__=="__main__":
    main()
