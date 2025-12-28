# 🚀 SpotiBeam V7 - Feature Packed Music Download Tool

**"Never gonna give you up. Never gonna let you down. Never gonna fail to download that track."**

SpotiBeam is a high-performance, fun TUI (Terminal User Interface) designed for the "OverLords" of music. It doesn't just download music; it conducts rescue missions for tracks other tools leave behind.

---

## ✨ Features

* **Bulk Download Support:** Can download Playlists and Albums too. Just make sure your Spotjfy playlist is public before downloading. If not,first make it public.
* **GodMode Engine:** Intelligent fallback logic that cycles through **YouTube Music** → **Bandcamp** → **SoundCloud** until the mission is accomplished.
* **Rescue Ops:** Built-in `yt-dlp` rescue protocols for those stubborn tracks that refuse to be found.
* **Auto-Organized Media:** Everything is smartly sorted into folders (Tracks, Albums, Playlists) so you don't have to play digital janitor.
* **Lyric Sync:** Automatic organization of `.lrc` files so you can actually sing along.
* **Metadata Mastery:** Complete metadata embedding—album art, artist names, and more.
* **Multi-Threaded Turbo:** Enabled 4-thread vibes for bulk downloads that are faster than a potato on a rocket.
* **Easter Eggs:** Includes built-in memes and Rick Astley ASCII art because life is too short for boring terminals.

---
## 🎁 Versions
* **SpotiBeam_v7Ultra :**  My fastest tool yet. Visible Download Progress for each song. Multiple track simultaneous downloads (which is why in very large playlists, it randomly skips songs).
* **SpotiBeam_v7Airborne:** Reliable. Dont show individual song progress on screen, hence lightweight. Downloads each song one by one, intead of a sudden burst, hence making it more stable. Due to this, takes more time to download,but reduces accidental track skipping.



## 🛠️ Installation & Launch

I've made the setup as easy as possible. Linux users, I trust your instincts; Windows users, follow the light.

### 1. The Essentials (Do this first!)
* **Python 3.8+:** Download from [python.org](https://www.python.org/). 
    * **⚠️ CRITICAL:** On Windows, you **MUST** tick the box that says **"Add Python to PATH"** during installation. If you miss this, the script won't even wake up.
* **FFmpeg:** The powerhouse used for audio conversion and metadata.
    * **Setup:** Download FFmpeg and add it to your **System Variables (PATH)**. 
    * **Verify:** Open a terminal (CMD or PowerShell) and type `ffmpeg`. If you don't see an error, you've passed the test.

### 2. How to Run
1. Clone this repository or download the `SpotiBeam_v7Ultra.py` or `SpotiBeam_v7Airborne.py` file.
2. Open your terminal in that folder.
3. Type `SpotiBeam_v7Ultra.py` or `SpotiBeam_v7Airborne.py` and hit Enter.

> **Note:** On first launch, SpotiBeam will automatically detect and install missing dependencies like `spotdl` and `colorama` etc. 

---
## 📱 Mobile Support (Termux)
SpotiBeam can run on Android via **Termux**, though this is considered an "Advanced" setup.

* **Requirements:** You must install `python`, `ffmpeg`, and `binutils` within the Termux environment.
* **Note:** Due to how Android handles file permissions, you may need to run `termux-setup-storage` to save music to your phone's internal memory.
* **Support:** Since mobile environments vary wildly, you might have to do quite much research (unless you are a pro). If you get it working, you're an official OverLord.

## 🛠️ Troubleshooting (The "Fix It" Corner)

| Problem | Likely Cause | Solution |
| :--- | :--- | :--- |
| **"Stuck" for >5 mins** | CPU/Internet hiccup or initial setup lag. | Close the terminal and **restart your system**. It usually loads directly the second time. |
| **"FFmpeg not found"** | PATH variables are wrong. | Search Google for "How to add FFmpeg to PATH" and follow the steps carefully. |
| **Python Errors** | Python isn't installed system-wide. | Re-install Python and ensure "Add to PATH" is checked. |
| **Bulk Download lag** | Engine warming up. | Try downloading a **single track** first to "warm up" the CPU. |
| **Error related to lyrics** | Lyrics aren't available | Nothing can be done about it 😅 |

---

## 💡 Pro-Tips for OverLords
* **The "Pilot" Run:** Always try a single track before throwing a 500-song playlist at it. I personally recommend downloading playlist/album with <100 tracks. My tool starts to slow down after it and it will randomly skip tracks then.
* **Connection:** The very first download might take up to 5 minutes depending on your setup. Let it cook. If it is stuck even after 5 minutes, check troubleshooting section.
* **Old PC Warning:** If you're on a "potato" PC and it's acting up, a system restart solves 99% of problems.
* Download speed may vary device to device.
---
## 🎧 Technical Note: Audio Quality (Bitrate)
SpotiBeam downloads audio at **128kbps** by default. 

**Why not 320kbps?**
 * YouTube and YouTube Music simply do not host audio in 320kbps MP3 format.
 * Standard/Free Users: YouTube Music streams at 128kbps OPUS/AAC.
 * Premium Users: High-quality streaming is capped at 256kbps AAC.
 * Video Audio: Standard YouTube videos usually have an audio track capped at roughly 128-160kbps OPUS.

​**The "320kbps" Trap:** ​When a tool says "Download in 320kbps," what it is actually doing is:
  * ​Downloading the 128kbps source.
  * ​Using a tool like FFmpeg to re-encode (transcode) that file into a 320kbps MP3.
  * ​This makes the file much larger, but because the "data" wasn't there to begin with, the quality stays exactly the same. In fact, re-encoding can sometimes hurt quality slightly due to "generation loss."

**SpotiBeam's Philosophy:** 
 * SpotiBeam download the **native** source quality. This gives you the best possible sound at the smallest possible file size (approx. 3MB vs 8MB). No fake padding, no wasted space.
---

## 📝 Personal Notes
I initially designed SpotiBeam for my own personal use, but it worked so well for me (10GB+ downloaded in 4-5 hours which otherwise would have taken me days to manually do it with all the lrc files anf folder organisation!) that I had to share it. It’s not perfect, but it’s powerful and was made as a fun project only. **Use it wisely.**
This is the 7th Iteration of my project SpotiBeam, but I am not uploading previous versions because they had a lot of missing features and bugs (Still functional, serve basic purpose, but lack features). 

## 🙏 Credits
* [spotdl](https://github.com/spotDL/spotify-downloader) - The engine that makes this possible.
* [FFmpeg](https://ffmpeg.org/) - The industry standard for handling audio.

---

### ⚖️ License
This project is licensed under the **GNU GPL v3**. It is free, open-source, and shall remain so.
