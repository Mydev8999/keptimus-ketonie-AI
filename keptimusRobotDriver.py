import speech_recognition as sr
from gtts import gTTS
import os
import subprocess
import nltk
from nltk.chat.util import Chat, reflections




# Créer un objet recognizer
r = sr.Recognizer()

# Capturer l'audio à partir du microphone
with sr.Microphone() as source:
    print("Je vous écoute...")
    audio = r.listen(source)
    
# Utiliser Google Web Speech API pour transcrire l'audio en texte
try:
    aui =  r.recognize_google(audio, language='fr-FR')
    # Texte à convertir en parole
    texte = aui

    pairs = [
                    ['Bonjour', ['Bonjour !', 'Salut !', 'bonjour a toi kétonien ou kétonienne']],
                    ['Comment ça va ?', ['Je vais bien, merci de demander !', 'Je me sens bien, merci !']],
                    ['Quel est ton nom ?', ['keptimus AI pour vous servire']],
                    ['Au revoir', ['Au revoir !', 'À bientôt !', 'Au revoir kétonien ou kétonienne']],
                    ['histoire', ["La ketonie est une micronation ou tous le monde est libre ell possède sa propre monaie, une lanque national et plain d'autre chose encore"]],
                    ['qui est petit mousse', ["keptimus est une intélligence artificiel développer par l'entreprise ketlabs une entreprise technologique kétonienne"]],
                    ['tu as quel âge', ["je n'ai pas d'age je suis une IA", "j'ai l'age de ta grand mère"]]
                    # Ajoutez d'autres paires de questions-réponses selon vos besoins
                ]

    chatbot = Chat(pairs, reflections)


    print("Bonjour ! Posez-moi des questions ou dites-moi simplement bonjour.")
    while True:
        user_input = texte
        response = chatbot.respond(user_input)
        print("ChatBot:", response)


        # Créer un objet gTTS
        tts = gTTS(text=response, lang='fr')       
        # Sauvegarder la sortie audio dans un fichier
        tts.save("output.mp3")      
        # Lire la sortie audio
        # os.system("mpg123 output.mp3")
        subprocess.call(["start", "output.mp3"], shell=True)
        break

except sr.UnknownValueError:
    print("Désolé, je n'ai pas compris.")
except sr.RequestError as e:
    print("Erreur lors de la demande à l'API de reconnaissance vocale : ", e)
