"""
Simple SpotDL FLAC Downloader with Rate Limit Management
Downloads music from Spotify URLs in FLAC format with full metadata
"""

import subprocess
import sys
import os
import time
import json
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


def setup_spotify_credentials():
    """Setup custom Spotify credentials to avoid rate limiting"""
    config_dir = Path.home() / '.spotdl'
    config_file = config_dir / 'config.json'
    
    print("\n🔧 Setting up Spotify credentials to avoid rate limiting...")
    print("\n📋 To get your own Spotify credentials:")
    print("1. Go to: https://developer.spotify.com/dashboard")
    print("2. Log in with your Spotify account")
    print("3. Click 'Create App'")
    print("4. Fill in any app name (e.g., 'My Music Downloader')")
    print("5. Add redirect URI: http://localhost:8080/callback")
    print("6. Copy your Client ID and Client Secret")
    
    print(f"\n📁 Config will be saved to: {config_file}")
    
    # Check if config already exists
    if config_file.exists():
        print("\n✅ Found existing config file")
        with open(config_file, 'r') as f:
            config = json.load(f)
        
        if config.get('client_id') and config.get('client_secret'):
            if config['client_id'] != 'f8a606e5583643beaa27ce62c48e3fc1':  # Not default
                print("✅ Custom credentials already configured!")
                return True
            else:
                print("⚠️ Using default shared credentials (causes rate limiting)")
    
    # Ask user if they want to set up credentials
    setup = input("\nSet up your own Spotify credentials now? (y/n): ").lower().strip()
    if setup not in ['y', 'yes', 's', 'si', 'sí']:
        print("⚠️ Continuing with shared credentials (may hit rate limits)")
        return False
    
    # Get credentials from user
    print("\nEnter your Spotify Developer credentials:")
    client_id = input("Client ID: ").strip()
    client_secret = input("Client Secret: ").strip()
    
    if not client_id or not client_secret:
        print("❌ Invalid credentials. Continuing with defaults.")
        return False
    
    # Create config directory if it doesn't exist
    config_dir.mkdir(exist_ok=True)
    
    # Load existing config or create new
    if config_file.exists():
        with open(config_file, 'r') as f:
            config = json.load(f)
    else:
        config = {}
    
    # Update with new credentials
    config.update({
        'client_id': client_id,
        'client_secret': client_secret,
        'load_config': True
    })
    
    # Save config
    with open(config_file, 'w') as f:
        json.dump(config, f, indent=2)
    
    print("✅ Credentials saved successfully!")
    return True


def download_music_with_retries(url, output_dir=None, max_attempts=3):
    """Download music with intelligent retry for rate limiting"""
    
    for attempt in range(1, max_attempts + 1):
        print(f"\n🔄 Attempt {attempt}/{max_attempts}")
        
        success = download_music(url, output_dir, attempt)
        if success:
            return True
        
        if attempt < max_attempts:
            wait_time = 60 * attempt  # Progressive wait: 60s, 120s, 180s
            print(f"⏳ Waiting {wait_time} seconds before retry...")
            time.sleep(wait_time)
    
    print(f"\n❌ Failed after {max_attempts} attempts")
    return False


def download_music(url, output_dir=None, attempt=1):
    """Download music using spotdl with FLAC format"""
    
    # Set default output directory to current directory
    if output_dir is None:
        output_dir = Path.cwd()
    else:
        output_dir = Path(output_dir)
    
    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Build spotdl command with rate limit friendly settings
    cmd = [
        'spotdl', 'download', url,
        '--format', 'flac',              # FLAC format
        '--bitrate', 'disable',          # Keep original quality
        '--output', str(output_dir / '{artists} - {title}.{output-ext}'),
        '--audio', 'youtube-music', 'youtube', 'soundcloud',  # Multiple audio providers
        '--lyrics', 'genius', 'azlyrics', 'musixmatch',       # Multiple lyrics providers
        '--generate-lrc',                # Generate LRC files
        '--overwrite', 'skip',           # Skip existing files
        '--max-retries', '10',           # High retry count for individual tracks
        '--threads', '1',                # Single thread to reduce API calls
        '--config',                      # Use config file (with custom credentials)
    ]
    
    if attempt == 1:  # Only show this info on first attempt
        print(f"🎵 Downloading to: {output_dir}")
        print(f"📀 Format: FLAC (lossless)")
        print(f"🎯 URL: {url}")
    
    print(f"🚀 Starting download (attempt {attempt})...")
    
    try:
        # Run spotdl command
        result = subprocess.run(cmd, timeout=600)  # 10 minute timeout
        
        # Check if any files were actually downloaded
        flac_files = list(output_dir.glob('*.flac'))
        
        if result.returncode == 0 and flac_files:
            print(f"\n🎉 Download completed successfully!")
            print(f"📁 Downloaded {len(flac_files)} file(s)")
            for file in flac_files[-3:]:  # Show last 3 files
                print(f"   ✅ {file.name}")
            if len(flac_files) > 3:
                print(f"   ... and {len(flac_files) - 3} more files")
            return True
        elif flac_files:
            print(f"\n⚠️ Download completed with warnings, but files were downloaded:")
            for file in flac_files[-3:]:
                print(f"   ✅ {file.name}")
            return True
        else:
            if "rate limit" in str(result.stderr).lower() or result.returncode == 1:
                print(f"⚠️ Rate limit detected, will retry...")
                return False
            else:
                print(f"❌ Download failed - no files were created")
                return False
            
    except subprocess.TimeoutExpired:
        print("❌ Download timed out (took longer than 10 minutes)")
        return False
    except KeyboardInterrupt:
        print("\n\n⏹️ Download cancelled by user")
        return False
    except Exception as e:
        print(f"❌ Error during download: {e}")
        return False


def main():
    """Main function"""
    print("=" * 50)
    print("🎵 SpotDL FLAC Downloader")
    print("=" * 50)
    
    # Check if spotdl is available
    if not check_spotdl():
        sys.exit(1)
    
    # Setup Spotify credentials to avoid rate limiting
    setup_spotify_credentials()
    
    print("\nSupported URLs:")
    print("🎵 Single track: https://open.spotify.com/track/...")
    print("💿 Album: https://open.spotify.com/album/...")
    print("📝 Playlist: https://open.spotify.com/playlist/...")
    print("🎤 Artist (all songs): https://open.spotify.com/artist/...")
    print("🔍 Search query: 'Artist - Song Title'")
    
    print("\n💡 TIP: Search queries often work better than URLs!")
    print("Example: 'Bad Bunny - Un Verano Sin Ti'")
    
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
        
        # Download with retries
        success = download_music_with_retries(url, output_dir)
        
        if success:
            continue_choice = input("\nDownload another? (y/n): ").strip().lower()
            if continue_choice not in ['y', 'yes', 's', 'si']:
                print("👋 Goodbye!")
                break
        else:
            print("\n💡 Try using a search query instead of URL")
            print("Example: 'Artist Name - Song Title'")


if __name__ == "__main__":
    main()