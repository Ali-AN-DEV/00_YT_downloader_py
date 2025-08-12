"""
Simple SpotDL FLAC Downloader
Downloads music from Spotify URLs in FLAC format with full metadata
"""

import subprocess
import sys
import os
from pathlib import Path


def check_spotdl():
    """Check if spotdl is installed"""
    try:
        result = subprocess.run(['spotdl', '--version'], 
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print(f"✅ spotdl found: {result.stdout.strip()}")
            return True
    except (FileNotFoundError, subprocess.SubprocessError, subprocess.TimeoutExpired):
        pass
    
    print("❌ spotdl not found!")
    print("Install with: pip install spotdl")
    return False


def download_music(url, output_dir=None):
    """Download music using spotdl with FLAC format"""
    
    # Set default output directory to current directory
    if output_dir is None:
        output_dir = Path.cwd()
    else:
        output_dir = Path(output_dir)
    
    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Build spotdl command with improved error handling
    cmd = [
        'spotdl', 'download', url,
        '--format', 'flac',              # FLAC format
        '--bitrate', 'disable',          # Keep original quality
        '--output', str(output_dir / '{artists} - {title}.{output-ext}'),
        '--audio', 'youtube-music', 'youtube', 'soundcloud',  # Multiple audio providers for fallback
        '--lyrics', 'genius', 'azlyrics', 'musixmatch',      # Multiple lyrics providers
        '--generate-lrc',                # Generate LRC files
        '--overwrite', 'skip',           # Skip existing files
        '--print-errors',                # Show any errors
        '--max-retries', '5',            # More retries for rate limiting
        '--threads', '1',                # Single thread to avoid rate limiting
    ]
    
    print(f"🎵 Downloading to: {output_dir}")
    print(f"📀 Format: FLAC (lossless)")
    print(f"🎯 URL: {url}")
    print("🚀 Starting download...")
    print("⏳ Note: This may take a moment due to rate limiting...\n")
    
    try:
        # Run spotdl command
        result = subprocess.run(cmd)
        
        # Check if any files were actually downloaded
        flac_files = list(output_dir.glob('*.flac'))
        
        if result.returncode == 0 and flac_files:
            print(f"\n🎉 Download completed successfully!")
            print(f"📁 Downloaded {len(flac_files)} file(s)")
            for file in flac_files:
                print(f"   ✅ {file.name}")
            return True
        elif flac_files:
            print(f"\n⚠️ Download completed with warnings, but files were downloaded:")
            for file in flac_files:
                print(f"   ✅ {file.name}")
            return True
        else:
            print(f"\n❌ Download failed - no files were created")
            print("💡 Try one of these solutions:")
            print("   1. Wait a few minutes and try again (rate limiting)")
            print("   2. Try a different song")
            print("   3. Use a search query instead: 'Artist - Song Title'")
            return False
            
    except KeyboardInterrupt:
        print("\n\n⏹️ Download cancelled by user")
        return False
    except Exception as e:
        print(f"\n❌ Error during download: {e}")
        return False


def main():
    """Main function"""
    print("=" * 50)
    print("🎵 SpotDL FLAC Downloader")
    print("=" * 50)
    
    # Check if spotdl is available
    if not check_spotdl():
        sys.exit(1)
    
    print("\nSupported URLs:")
    print("🎵 Single track: https://open.spotify.com/track/...")
    print("💿 Album: https://open.spotify.com/album/...")
    print("📝 Playlist: https://open.spotify.com/playlist/...")
    print("🎤 Artist (all songs): https://open.spotify.com/artist/...")
    print("🔍 Search query: 'Artist - Song Title'")
    
    while True:
        print("\n" + "-" * 50)
        
        # Get URL from user
        url = input("Enter Spotify URL or search query (or 'quit' to exit): ").strip()
        
        if url.lower() in ['quit', 'q', 'exit']:
            print("👋 Goodbye!")
            break
        
        if not url:
            print("❌ Please enter a valid URL or search query")
            continue
        
        # Optional: Ask for output directory
        output = input("Output directory (press Enter for current directory): ").strip()
        output_dir = output if output else None
        
        # Download
        success = download_music(url, output_dir)
        
        if success:
            continue_choice = input("\nDownload another? (y/n): ").strip().lower()
            if continue_choice not in ['y', 'yes', 's', 'si']:
                print("👋 Goodbye!")
                break


if __name__ == "__main__":
    main()