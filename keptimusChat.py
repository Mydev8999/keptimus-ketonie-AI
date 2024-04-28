import nltk
from nltk.chat.util import Chat, reflections


pairs = [
    ['Bonjour', ['Bonjour !', 'Salut !', 'bonjour a toi kétonien']],
    ['Comment ça va ?', ['Je vais bien, merci de demander !', 'Je me sens bien, merci !']],
    ['Quel est ton nom ?', ['keptimus AI pour vous servir']],
    ['Au revoir', ['Au revoir !', 'À bientôt !']],
    # Ajoutez d'autres paires de questions-réponses selon vos besoins
]

chatbot = Chat(pairs, reflections)


print("Bonjour ! Posez-moi des questions ou dites-moi simplement bonjour.")
while True:
    user_input = input("Vous: ")
    response = chatbot.respond(user_input)
    print("ChatBot:", response)
