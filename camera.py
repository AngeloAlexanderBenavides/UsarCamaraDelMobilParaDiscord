import cv2
import pyvirtualcam
import numpy as np
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv("config.vne", encoding="utf-8")


ip = os.getenv("IP")
if not ip:
    print("Error: No se pudo cargar la IP desde config.vne")
    exit()

url = f"http://{ip}:4747/video"
print(f"Conectando a: {url}")  # Depuración

cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("Error: No se pudo conectar con DroidCam. Verifica la IP y que la app esté abierta.")
    exit()

with pyvirtualcam.Camera(width=640, height=480, fps=30, backend="obs") as cam:
    print(f'Usando cámara virtual: {cam.device}')

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: No se pudo capturar el fotograma.")
            break

        frame = cv2.resize(frame, (640, 480))

        # Recortar la parte superior del frame
        y = 50
        frame = frame[y:, :]  

        # Redimensionar el frame al tamaño esperado
        frame = cv2.resize(frame, (640, 480))

        # Convertir el frame a formato compatible con OBS
        if frame.shape[-1] == 4:  
            frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)
        elif len(frame.shape) == 2:  
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
        else:
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Voltear el frame si es necesario
        frame = cv2.flip(frame, 0)

        # Enviar el frame a la cámara virtual
        cam.send(frame)
        cam.sleep_until_next_frame()

cap.release()
cv2.destroyAllWindows()
