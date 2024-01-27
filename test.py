# Import the Speech-to-Text client library
from google.cloud import speech
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import threading
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
from pydub import AudioSegment
import requests
import random
import datetime

API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"

i = random.randint(0, 3)
if i == 0:
    headers = {"Authorization": "Bearer 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"}
if i == 1:
    headers = {"Authorization": "Bearer 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"}
if i == 2:
    headers = {"Authorization": "Bearer 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"}
else: 
    headers = {"Authorization": "Bearer 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"}


fs=44100   
duration= 20



def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    print(response.json())
 

 


def record():

    while True: 
        print("recording")
        myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
        
 
        sd.wait()
        print("finished recording")
 
        myrecording = np.int16(myrecording * 32767)
        
        main_file = f'life, the universe, and everything/{datetime.datetime.now()}0.wav'

        wav.write(main_file, fs, myrecording)
        
 
        audio = AudioSegment.from_wav(main_file)
        
 
        amplified_audio = audio + 30   
        
        tuned_file = f'life, the universe, and everything/{datetime.datetime.now()}1.wav'
        amplified_audio.export(tuned_file, format="wav")
        
        print("finished processing recording")
        t = threading.Thread(target=query, args=(tuned_file,))
        t.start()
        
        
    

record()
