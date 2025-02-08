from yt_dlp import YoutubeDL

def download_video(url, output_template="%(title)s.%(ext)s"):
    ydl_opts = {
        # Target H.264 video + AAC audio (no VP9)
        'format': 'bestvideo[ext=mp4][vcodec^=avc1]+bestaudio[ext=m4a]/best[ext=mp4]',
        'merge_output_format': 'mp4',
        'outtmpl': output_template,
        'quiet': True,
        'no_warnings': True,
        'progress_hooks': [lambda d: print(f"Downloading... {d['filename']}")],
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = input("Enter the YouTube URL: ")
    print("Starting download...")
    download_video(url)
    print("Download complete!")