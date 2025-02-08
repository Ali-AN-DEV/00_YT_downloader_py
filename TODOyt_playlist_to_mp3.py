import os
from yt_dlp import YoutubeDL

# Get the system's Music directory path
USER_MUSIC_DIR = os.path.join(os.path.expanduser("~"), "Music")

def download_mp3(url, output_template=os.path.join(USER_MUSIC_DIR, "%(title)s.%(ext)s")):
    """
    Descarga el audio de un video de YouTube como MP3.
    
    :param url: URL del video de YouTube.
    :param output_template: Plantilla para el nombre del archivo de salida.
    """
    # Procesar la plantilla para forzar la extensión .mp3 y obtener el directorio
    output_template_mp3 = output_template.replace("%(ext)s", "mp3")
    output_dir = os.path.dirname(output_template_mp3)
    
    # Crear el directorio si no existe
    os.makedirs(output_dir, exist_ok=True)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_template_mp3,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
        'no_warnings': True,
        'progress_hooks': [lambda d: print(f"Descargando... {d['filename']}")],
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = input("Introduce la URL de YouTube: ")
    print("Iniciando descarga...")
    download_mp3(url)
    print("¡Descarga completada!")