import os
from yt_dlp import YoutubeDL

def get_default_music_dir():
    """Returns the system's default Music directory path."""
    home_dir = os.path.expanduser("~")
    return os.path.join(home_dir, "Music")

def download_mp3(url, output_template=None):
    """
    Downloads audio from a YouTube video as MP3.
    """
    # Set default output path to the system's Music directory
    if output_template is None:
        music_dir = get_default_music_dir()
        output_template = os.path.join(music_dir, "%(title)s.%(ext)s")

    output_template_mp3 = output_template.replace("%(ext)s", "mp3")
    output_dir = os.path.dirname(output_template_mp3)

    try:
        os.makedirs(output_dir, exist_ok=True)
    except PermissionError:
        print(f"Error: No permission to create/write to '{output_dir}'.")
        return
    except Exception as e:
        print(f"Unexpected error: {e}")
        return

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
        'progress_hooks': [lambda d: print(f"Downloading... {d['filename']}")],
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"Download failed: {e}")

if __name__ == "__main__":
    url = input("Enter YouTube URL: ")
    print("Starting download...")
    download_mp3(url)
    print("Download completed! You can hopefully find it in your music directory :)")