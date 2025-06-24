# Descargar multimedia de YouTube (Video + MP3)

> Scripts en Python para descargar videos de YouTube con audio integrado o extraer solo el audio en MP3.

## Características
- **Video con audio**: Usando yt_to_mp4 descarga en MP4 con códec H.264 (compatible con todos los reproductores).
- **Audio en MP3**: Usando yt_to_mp3V4 extrae el audio (192 kbps por defecto) ya sea playlists o individual, y crea carpetas en agrupando la música de un mismo autor, así como organizar la existente. 

## Requisitos
- Python 3.7 o superior
- `ffmpeg` instalado y accesible en el PATH del sistema

## Instalación
1. Instalar dependencias de Python:
   ```bash
   pip install -r dependencies.txt
2. Instalar FFmpeg: 

   - Linux:  
   ```bash
   sudo apt install ffmpeg 
   ```

   - Mac:  
   ```bash
   brew install ffmpeg 
   ```
   
   - Windows: 
   ```bash
   choco install ffmpeg
   ```
    O simplemente ve a : https://ffmpeg.org/ 
   

## Problemas Comunes

Prueba a dentro de la terminal de tu IDE 

 ```bash 
   pip install python-ffmpeg
 ```