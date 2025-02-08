from yt_dlp import YoutubeDL

def download_mp3(url, output_template="%(title)s.%(ext)s"):
    """
    Descarga el audio de un video de YouTube como MP3.
    
    :param url: URL del video de YouTube.
    :param output_template: Plantilla para el nombre del archivo de salida.
    """
    ydl_opts = {
        'format': 'bestaudio/best',       # Mejor calidad de audio disponible
        'outtmpl': output_template.replace('%(ext)s', 'mp3'),  # Fuerza extensión .mp3
        'postprocessors': [{              # Conversión a MP3 usando FFmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',    # Calidad del audio (192 kbps)
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