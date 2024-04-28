import cv2
import numpy as np

# Charger l'image
image = cv2.imread('cellule.jpg')

# Conversion en niveaux de gris
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Filtrage Gaussien pour réduire le bruit
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Seuillage adaptatif pour accentuer les zones d'intérêt
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

# Trouver les contours dans l'image seuillée
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dessiner les contours sur l'image originale
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# Afficher l'image avec les contours détectés
cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
