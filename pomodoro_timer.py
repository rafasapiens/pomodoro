# Programa timer para aplicar a técnica Pomodoro, que consiste em trabalhar focado por 25 minutos, fazer uma pausa de 5 minutos e voltar a repetir.

''' Dependencias 
sudo apt update && sudo apt install espeak ffmpeg libespeak1 
sudo apt-get install alsa-utils

Instale o ambiente virtual com:
    python3 -m venv pomodoro
Ative o ambiente virtual com:
    source pomodoro/bin/activate
Instale as bibliotecas:
    pip install pyttsx3==2.71
    pip install gTTS

'''

import time
import pyttsx3

import os
from gtts import gTTS


start = time.time()
#print(start)
print(time.ctime)
print("\nComeçando Pomodoro em 20 segundos...\n\nConcentre-se na sua tarefa pelos próximos 25 minutos!\n\nBom trabalho!")

# Tempo do timer em segundos

time.sleep(1)  # Aqui deverá inserir o tempo em segundos
end = time.time()
#print(end)

#Inicio do Speach
engine = pyttsx3.init()
#Chanching voices
voices = engine.getProperty('voices')
engine.setProperty('voice', 'brazil')  #voices[1].id)

# Set properties _before_ you add things to say
engine.setProperty('rate', 200)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)  # Volume 0-1
engine.setProperty('voice', 'brazil')  
'''
for voice in voices:
    print(voice)
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)    
    engine.setProperty('voice', voice.id)
for voice in voices:
    if 'brazil' in voice.id: # or 'en_GB' in voice.languages:
        print(voice.id)
'''
#Speaching text
engine.say("Olá! Eu sou o seu computador! A tarefa, Já vai começar! Concentre-se!     Silvio Santos.     já pode.       parar. de.     tirar.     as.     bó.     las ")
engine.runAndWait()
#print(pyttsx3.voice.Voice)

#print(end - start)
print(time.ctime)

#Usando modulo gTTS
mytext = "Bem vindo a tecnica Pomodoro! Concentre-se na sua tarefa pelos próximos 25 minutos!"

language = 'pt'

myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("pomodoro.mp3")
os.system("mpv --speed=1.75  pomodoro.mp3")

print(time.ctime)


while True:

    #Iniciando os 25 minutos
    time.sleep(25*60) # Aqui deverá ser 25 minutos para a técnica Pomodoro
    print(time.ctime)


    mytext = "Descanse por cinco minutos e então concentre-se novamente em sua tarefa por mais 25 minutos. Divirta-se! Ah vai se fudê.  Me deixa manca e quer que eu faça as coisa!   Desculpe estou nervosa!  Mas sou sincera, então se eu estiver nervosa vou mandar você se fuder!  Always look on the bright side of life! Pronto melhorei, estou feliz denovo! "

    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("pomodoro.mp3")
    os.system("mpv --speed=1.75  pomodoro.mp3")

    os.system("mpv EricIdle-Always_look_on_the_bright_side_of_life.webm")


    #Descanso de 5 minutos
    time.sleep(2*60) #Tempo do video de 3 minutos mais 2 minutos de timer
    print(time.ctime)


    mytext = "Ok, acabou a moleza, bora trabalhar por mais 25 minutos!"

    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("pomodoro.mp3")
    os.system("mpv --speed=1.75  pomodoro.mp3")





