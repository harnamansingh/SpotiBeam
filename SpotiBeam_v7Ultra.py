#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
                        SpotiBeam_v7Ultimate++ (OverLord Edition)
    The True Final Form: Sock-Powered, Potato-Enhanced, and ClippyAGI-Fused
Now with smart fallback, dependency healing, Real Vibes Only (no Upscaling), and meme-tier elegance.
                         Engineered by OverLord Harnaman 🎃
"""

import os
import sys
import re
import shutil
import subprocess
import random
import threading

try:
    from colorama import Fore, Style, init
    from pyfiglet import Figlet
except ImportError:
    print("Missing dependencies. Installing...")
    subprocess.run(["pip", "install", "colorama", "pyfiglet"])
    from colorama import Fore, Style, init
    from pyfiglet import Figlet

init(autoreset=True)

# --- ASCII Rickroll for critical failure ---
def rick_ascii():
    ascii_art = r"""
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣻⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡽⣯⣻⣻⡽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣻⣻
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡿⣿⣿⣿⣿⣿⣿⡿⣻⣻⣻⣻⣻⣻⡽⣯⣟⢷⠍⠟⠉⠛⢿⢿⣻⣻⢿⣿⣿⣯⣻⡽⣯⣻⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⢯
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣻⣻⣻⡟⡅⠀⠀⠀⠠⠀⠀⠆⡹⣻⣻⡽⣯⣻⡽⣯⣻⡽⣻⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣻⣻
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⡟⡛⡜⡜⣎⢦⢶⣖⡴⡀⠠⣿⣿⣿⣟⣟⣟⣟⣟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣻⣻⣻
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣻⢆⢭⢎⢎⢞⡝⣝⡽⡽⡣⢂⣟⢯⢯⢯⣿⣻⣻⡽⣻⡽⣻⣻⣿⣿⣿⣿⣿⣿⣿⡿⣟⣿⣿⣿⣿⣻
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⢧⡒⡔⢆⢯⢎⠚⡜⡇⣼⣿⣿⣯⣻⣻⣻⣻⢯⣿⣿⣻⣻⣻⣻⢿⣿⣿⣿⣿⡿⣻⣻⣻⣟⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢹⢧⢣⢣⠡⡋⡯⣫⢯⡹⣹⣿⣿⣿⣿⣯⣻⣻⣻⣿⣿⣻⣻⣻⣿⣟⣟⢿⣿⣿⣿⣿⣻⢿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠧⢣⢢⢌⣍⡹⡽⣹⣽⣿⣿⣿⣿⣿⡽⣯⣻⢯⣻⢯⣻⣻⣿⣿⣿⣿⣻⣻⣻⣻⢿⢿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡽⣍⢎⢎⢝⢏⢏⣝⢿⣿⣿⣿⣿⣿⣿⣻⡽⣯⣻⣻⣿⣿⣟⢿⣿⢿⣻⣻⣿⣿⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣟⣟⣟⡜⡜⡜⡝⡭⣫⢫⠂⢫⣿⣿⣿⣟⢯⣻⣻⣻⡽⣻⣿⣿⣿⣟⣿⣿⣿⣻⣟⣟⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⢿⡿⣿⢿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⡿⡽⡻⡿⣇⢣⢣⠱⡱⡱⣽⣿⠀⠀⠀⠀⠐⢉⠍⡛⢿⢯⣻⣻⣿⣿⡿⣿⣿⣿⣿⣟⣟⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣟⢿⣿⣿⣿⡿⣿⣿⣟⢿⣻⣻⡿⣏⢋⠀⠀⠀⣹⣻⡇⢣⠱⣥⣻⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣻⣿⣿⣿⣟⣟⣟⡽⣻⣿⡿⡿⣿⣿⣿
⣿⣿⣿⣿⣿⢿⣿⣿⣿⢿⣻⣿⢿⣿⣿⢿⣻⣻⣻⡃⠀⠀⠀⠀⠀⠀⠠⠠⡣⢢⠱⡉⠙⠛⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣻⡽⣻⣿⢯⣻⣿⣿⢯⣻⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⢿⣻⣻⣿⣟⣟⣟⣿⣿⣿⣿⣿⡿⣟⣟⠄⠀⠀⠀⠀⠀⠀⠀⢀⢆⡑⠡⠉⠋⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣻⢯⣻⡽⣻⣻⡿⣯⢿⣿⣿⣿⣿⣿
⣿⣻⣟⣟⣿⣿⣿⣿⣟⣟⣟⣟⣿⣿⣿⣿⣟⣟⡽⡄⠀⠀⠀⠀⠀⠀⠀⢀⠁⣯⠚⠹⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣻⢯⢯⣻⣿⣿⣻⣻⣻⣿⣿⣿⣿⣿
⣿⣟⢿⣿⣿⣿⣿⣿⣻⣿⡿⣻⣻⣿⣿⣿⢿⣻⢯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣟⠖⡖⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⢿⣻⣿⣻⣿⣿⣿⣿⣿⣻⢯⣻⣻⣻
⣿⣻⣻⣿⣿⣿⣿⣻⣽⣿⣿⣟⣟⢿⣿⣿⡿⣻⣻⠀⠀⠀⠀⠀⠀⠀⠀⠀⢦⢢⣠⣀⠀⠀⠀⠀⠩⡛⡝⡜⡖⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣻⣻⣻⣿⣿⡿⣻⣿⣿⣻⣻⣿⣿⡿⣿⣻⣻⣻⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⡜⠈⠁⠀⠀⠀⠀⠀⠌⣌⢎⡜⡜⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣻⣿⣿⡿⣟⢿⣿⣿⣿
⣟⣿⣿⣿⡽⡽⡽⣻⣹⡽⣿⣿⣿⣻⣻⣻⣻⡽⣻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢢⠣⠒⠀⠀⠀⠀⠀⠀⠎⢎⢎⢎⢎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⡽⣿⣿⣻⣻⣻⢿⣿⣿
⣿⣿⢿⣿⣯⣫⣏⢯⣫⣿⣿⣿⣿⣟⣟⣟⣟⡽⡽⠀⡀⠀⠀⠀⠀⢀⢀⠀⠰⡰⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡝⡽⡽⣿⣿⣿⣻⡝⡽
⣯⣯⣯⣯⢯⣫⢫⣻⡿⣻⣿⣿⣿⣿⣿⣻⡽⡽⣭⠂⠀⡰⡱⠡⠢⢂⠆⠀⢠⠰⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢯⢫⣫⡿⣻⣿⣿⣿⣻⡹
⡿⡿⣻⣻⣻⢭⣚⢧⢫⣻⣿⣿⡿⡽⡽⡽⡽⣹⣝⢇⠄⠀⠀⠄⠄⠄⡐⠀⠄⡐⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡝⣝⡽⣹⢽⢯⡻⣻⣟⢯⢫⣚⣟⣟⣟⣟⣟⣟⡝
⣯⣻⡽⣯⣻⡜⡵⡽⣎⢭⣻⡝⡽⣽⡽⣝⣝⣝⡝⣗⢭⢎⠀⠀⠂⠂⠀⠀⠀⡐⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣹⣝⣝⡝⣝⡽⡽⡹⣚⠵⡭⢯⢯⢯⣻⡽⡽⣣
⣟⣟⡽⣯⢯⢎⢎⢯⣏⡗⡝⣝⡽⣻⢯⣫⢫⢫⣫⣻⢯⡳⡱⡱⡱⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡝⡝⡝⣝⡝⡝⡭⣫⢫⢭⣚⣝⣝⣝⡽⣹⣹⢧
⢏⠯⢫⢫⢫⢪⢎⢯⢏⠳⡹⡹⣻⡿⡯⣫⢫⡹⡹⡽⡽⡹⡸⡜⡄⠀⠀⢀⢂⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡭⡭⣫⡹⡹⡭⣫⢫⢫⣚⡜⡝⡝⣝⣝⢽⡹⡭
⠀⠀⠀⠀⠀⠀⠀
               Never gonna give you up. Never gonna let you down.
"""
    print(Fore.WHITE + ascii_art)

# --- Banner ---
def print_banner():
    banner = r"""
                         ░▒█▀▀▀█░▄▀▀▄░▄▀▀▄░▀█▀░░▀░░▒█▀▀▄░█▀▀░█▀▀▄░█▀▄▀█
                         ░░▀▀▀▄▄░█▄▄█░█░░█░░█░░░█▀░▒█▀▀▄░█▀▀░█▄▄█░█░▀░█
                         ░▒█▄▄▄█░█░░░░░▀▀░░░▀░░▀▀▀░▒█▄▄█░▀▀▀░▀░░▀░▀░░▒▀
            SpotiBeam_v7Ultra - Clippy.exe X Elon_Don EDITION (Real Vibes Only)
                               Forged by OverLord Harnaman 🎃

                          
    """
    print(Fore.CYAN + Style.BRIGHT + banner)


# --- Greetings ---
def random_greeting():
    lines = [
        "💡 Ultimate Mode: Chaos Engine Online.",
        "🧦 Socks calibrated. Potatoes aligned.",
        "🚀 4-thread AGI download system primed.", 
        "🎧 Your commands shall echo through the multiverse.",
        "🔥 320kbps? That’s the minimum standard for Overlords."
    ]
    print(Fore.MAGENTA + random.choice(lines))

# --- Dependency Check ---
def check_dependencies():
    tools = ["spotdl", "yt-dlp"]
    missing = []
    for tool in tools:
        try:
            subprocess.run([tool, "--version"], capture_output=True, check=True)
        except Exception:
            missing.append(tool)

    if missing:
        print(Fore.YELLOW + f"📦 Installing missing tools: {', '.join(missing)}")
        subprocess.run(["pip", "install"] + missing)
        print(Fore.CYAN + "✅ Dependencies healed. Please restart if issues persist.")

# --- Engine ---
class SpotiBeamUltimate:
    def __init__(self):
        self.base = "SpotiBeam_Downloads"
        self.prepare_dirs()

    def prepare_dirs(self):
        for t in ["Playlists", "Albums", "Singles"]:
            os.makedirs(os.path.join(self.base, t), exist_ok=True)
        os.makedirs(os.path.join(self.base, "Singles", "Lyrics"), exist_ok=True)

    def safe_name(self, raw):
        name = re.sub(r'[^\w\s-]', '', raw)
        return re.sub(r'\s+', '_', name.strip())[:40]

    def route_folder(self, mode, link_or_query):
        name = self.safe_name(link_or_query)
        if mode == "playlist":
            return os.path.join(self.base, "Playlists", name)
        elif mode == "album":
            return os.path.join(self.base, "Albums", name)
        else:
            return os.path.join(self.base, "Singles")

    def handle_lyrics(self, folder, mode):
        lyrics_folder = os.path.join(folder, "Lyrics") if mode != "track" else os.path.join(self.base, "Singles", "Lyrics")
        os.makedirs(lyrics_folder, exist_ok=True)
        for file in os.listdir(folder):
            if file.endswith(".lrc"):
                shutil.move(os.path.join(folder, file), os.path.join(lyrics_folder, file))

    def download_threaded(self, link_or_query, mode):
        folder = self.route_folder(mode, link_or_query)
        os.makedirs(folder, exist_ok=True)
        print(Fore.CYAN + f"\nDownloading to: {folder}")

        sources = ["youtube-music", "bandcamp", "soundcloud", "youtube"]  # fallback order

        def do_download():
            success = False
            for src in sources:
                print(Fore.YELLOW + f"🎯 Trying source: {src}")
                try:
                    subprocess.run([
                        "spotdl", "download", link_or_query,
                        "--output", folder,
                        "--format", "mp3",
                        "--audio", src,
                        "--threads", "4",
                        "--generate-lrc"
                    ], check=True)
                    self.handle_lyrics(folder, mode)
                    print(Fore.GREEN + f"\n✅ Download complete via {src}!")
                    success = True
                    break
                except subprocess.CalledProcessError:
                    print(Fore.RED + f"❌ {src} failed. Moving to next source...")
            
            if not success:
                print(Fore.RED + "\n💀 All sources failed. Rick time:")
                rick_ascii()

        thread = threading.Thread(target=do_download)
        thread.start()
        thread.join()


# --- Main ---
def main():
    print_banner()
    random_greeting()
    check_dependencies()

    engine = SpotiBeamUltimate()

    while True:
        print(Fore.CYAN + "\n======= ULTIMATE TERMINAL =======")
        print("1. Download Playlist")
        print("2. Download Album")
        print("3. Download Track (Name or URL)")
        print("4. Exit")

        choice = input(Fore.YELLOW + "\nYour command, OverLord: ").strip()

        if choice == "1":
            url = input("Paste Spotify Playlist URL: ").strip()
            engine.download_threaded(url, "playlist")
        elif choice == "2":
            url = input("Paste Spotify Album URL: ").strip()
            engine.download_threaded(url, "album")
        elif choice == "3":
            query = input("Enter Song Name or Spotify Track URL: ").strip()
            engine.download_threaded(query, "track")
        elif choice == "4":
            print(Fore.CYAN + "\nFarewell, Supreme Meme Being.")
            break
        else:
            print(Fore.RED + "Invalid input. Try 1-4. SUS detected.")

if __name__ == "__main__":
    main()
