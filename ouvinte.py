import sys
import speech_recognition as sr

def ouvir_microfone():  #Funcao responsavel por ouvir e reconhecer a fala
    microfone = sr.Recognizer() #Habilita o microfone para ouvir o usuario

    with sr.Microphone() as source:

        microfone.adjust_for_ambient_noise(source)  #Chama a funcao de reducao de ruido disponivel na  speech_recognition

        print("Diga alguma coisa : ")   #Avisa ao usuario que esta pronto para ouvir

        audio = microfone.listen(source)
    try :
        frase = microfone.recognize_google(audio,language ='pt-BR')
        print("Você disse : "+ frase)

    except sr.UnkownValueError:
        print("Não entendi ")


ouvir_microfone()