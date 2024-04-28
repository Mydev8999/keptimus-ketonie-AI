import cv2

import numpy as np

# Charger le classificateur de visage pré-entraîné
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Capturer la vidéo depuis la webcam
cap = cv2.VideoCapture(0)

while True:
    # Lire une frame de la vidéo
    ret, frame = cap.read()
    
    # Convertir l'image en niveaux de gris
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Détecter les visages dans l'image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    
    # Dessiner un rectangle autour de chaque visage détecté
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Afficher la frame avec les visages détectés
    cv2.imshow('Face Tracking', frame)
    
    # Quitter la boucle si la touche 'q' est enfoncée
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# Libérer la capture de la vidéo et détruire toutes les fenêtres OpenCV
cap.release()
cv2.destroyAllWindows()

