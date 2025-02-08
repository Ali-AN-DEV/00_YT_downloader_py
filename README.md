# Descargador de YouTube (Video + MP3)

> Scripts en Python para descargar videos de YouTube con audio integrado o extraer solo el audio en MP3.

## Características
- **Video con audio**: Usando yt_to_mp4 descarga en MP4 con códec H.264 (compatible con todos los reproductores).
- **Audio en MP3**: Usando yt_to_mp3 extrae el audio en alta calidad (192 kbps por defecto).

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
Si el IDE no reproduce sonido en los .mp4, usa VLC Media Player https://www.videolan.org/vlc/index.es.html 
 