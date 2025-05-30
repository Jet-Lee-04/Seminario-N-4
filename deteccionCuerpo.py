import cv2
import cv2.data

# Cargar el clasificador de cuerpo completo
cuerpo = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

# Capturar video desde la cámara
camara = cv2.VideoCapture(0)

if not camara.isOpened():
    print("Error!! No se pudo abrir la cámara")
    exit()

print("Usuario presione 's' para salir.")

while True:
    ret, frame = camara.read()
    if not ret:
        print("Error!! No se pudo leer la imagen.")
        break

    # Convertir a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar cuerpos
    cuerpos = cuerpo.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    # Dibujar rectángulo y mostrar coordenadas
    for i, (x, y, w, h) in enumerate(cuerpos):
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        print(f"Cuerpo {i+1}: x = {x}, y = {y}, ancho = {w}, alto = {h}")

    # Mostrar imagen en pantalla
    cv2.imshow('Detección de Cuerpo Completo', frame)

    # Salir con la tecla 's'
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

# Liberar recursos
camara.release()
cv2.destroyAllWindows()
