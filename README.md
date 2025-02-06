# 📷 Proyecto de Cámara Virtual con OpenCV y PyVirtualCam

Este proyecto usa **OpenCV** y **PyVirtualCam** para capturar video desde **DroidCam** y enviarlo a una cámara virtual compatible con OBS.

## 🚀 Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

- Python 3.x
- OpenCV (`opencv-python`)
- PyVirtualCam (`pyvirtualcam`)
- NumPy (`numpy`)
- python-dotenv (`python-dotenv`)

## ⚙️ Configuración
- Crea un archivo de configuración llamado config.vne en la carpeta del proyecto:

#Editar
IP=000.000.000.00  # Reemplaza con la IP de tu DroidCam previamente descargada en tu mobil
#Ejecuta el script:

## Instálalos con:

📝 Explicación del Código

- Carga la IP de config.vne usando dotenv para conectarse a DroidCam.
- Captura el video desde la IP con OpenCV (cv2.VideoCapture).
- Ajusta el frame (recorta, redimensiona, convierte a formato OBS).
- Envía el video a una cámara virtual usando PyVirtualCam.

## 🔧 Posibles Errores y Soluciones
- ❌ Error: No se pudo conectar con DroidCam
- ✅ Asegúrate de que la app esté abierta y usa la IP correcta en config.vne.
- ❌ UnicodeDecodeError en config.vne
- ✅ Guarda el archivo con codificación UTF-8 sin BOM.

```sh
pip install opencv-python pyvirtualcam numpy python-dotenv




#python camera.py



Este `README.md` explica el propósito, instalación, configuración y solución de errores. 🚀 ¿Quieres agregar algo más? 😎


"""
