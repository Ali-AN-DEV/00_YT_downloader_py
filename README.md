# SpotDL FLAC Downloader

A simple Python script to download music from Spotify in FLAC format using spotdl.

## Installation

1. **Install Python** (3.7 or higher)
2. **Install spotdl:**
   ```bash
   pip install spotdl
   ```
3. **Run the script:**
   ```bash
   python yt_to_flac.py
   ```

## Features

- ✅ Downloads in **FLAC format** (lossless quality)
- ✅ Includes full **metadata** (artist, album, track number, etc.)
- ✅ Downloads **lyrics** and **LRC files** with timing
- ✅ Supports tracks, albums, playlists, and artists
- ✅ Search functionality with artist and song names
- ✅ Multiple audio providers for better success rates

## Supported URLs

| Type | Example |
|------|---------|
| **Single Track** | `https://open.spotify.com/track/3bbIIVIwBoLqVcLebiEJFo` |
| **Album** | `https://open.spotify.com/album/4yP0hdKOZPNshxUOjY0cZj` |
| **Playlist** | `https://open.spotify.com/playlist/37i9dQZF1E8UXBoz02kGID` |
| **Artist** | `https://open.spotify.com/artist/1Xyo4u8uXC1ZmMpatF05PJ` |
| **Search Query** | `'Taylor Swift - Anti-Hero'` (use quotes) |

## Usage

1. Run the script: `python yt_to_flac.py`
2. Enter a Spotify URL or search query
3. Choose output directory (or press Enter for current directory)
4. Wait for download to complete

## Troubleshooting

### Common Issues

#### 1. Rate Limit Errors
**Problem:** `WARNING: Your application has reached a rate/request limit`

**Solutions:**
- Wait 2-3 minutes between downloads
- Use `--threads 1` (already included in script)
- Try downloading one song at a time instead of playlists

#### 2. YT-DLP Download Errors
**Problem:** `AudioProviderError: YT-DLP download error`

**Solutions:**
- Try using a **search query** instead of Spotify URL:
  - Instead of: `https://open.spotify.com/track/...`
  - Use: `'Bad Bunny - Un Verano Sin Ti'`
- Try a different song (some are region-blocked)
- Wait and try again later

#### 3. No Files Downloaded
**Problem:** Script says "success" but no FLAC files appear

**Solutions:**
- Check if files were downloaded with a different name
- Try a different output directory
- Use search queries instead of URLs
- Some songs may not be available in your region

#### 4. Invalid Audio Provider Error
**Problem:** `invalid choice: 'slider-kz'`

**Solution:**
- This is fixed in the current version
- Valid providers: `youtube-music`, `youtube`, `soundcloud`, `bandcamp`, `piped`

### Best Practices

1. **Use Search Queries for Better Success:**
   ```
   'Artist Name - Song Title'
   'Taylor Swift - Shake It Off'
   'The Beatles - Yesterday'
   ```

2. **For Albums, try the album search:**
   ```
   'album:Dark Side of the Moon Pink Floyd'
   ```

3. **Wait Between Downloads:**
   - Don't download too many songs rapidly
   - Wait 30-60 seconds between individual tracks
   - For playlists, expect longer wait times

### Audio Providers Priority

The script tries these providers in order:
1. **YouTube Music** (best quality, most songs)
2. **YouTube** (fallback, good quality)
3. **SoundCloud** (alternative source)

### Output Format

Files are saved as:
```
Artist Name - Song Title.flac
```

With additional files:
- `Artist Name - Song Title.lrc` (synced lyrics)

### Alternative Solutions

If the script continues to fail:

1. **Try spotdl directly in terminal:**
   ```bash
   spotdl download "search query" --format flac
   ```

2. **Use different audio provider:**
   ```bash
   spotdl download "URL" --format flac --audio soundcloud
   ```

3. **Check spotdl version:**
   ```bash
   spotdl --version
   ```
   (Should be 4.0+ for best compatibility)

### Getting Help

If you continue having issues:

1. Check the [official spotdl documentation](https://spotdl.rtfd.io/)
2. Visit the [spotdl GitHub repository](https://github.com/spotDL/spotify-downloader)
3. Try running spotdl commands directly to isolate the issue

### Legal Notice

This tool is for personal use only. Ensure you comply with:
- Spotify's Terms of Service
- Local copyright laws
- YouTube's Terms of Service

Download only music you have the right to access.