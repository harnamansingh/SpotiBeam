#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SpotiBeam_v7Ultra GodMode - V7-Airborne patch (Folder & TXT fixes)
- Tracks (formerly Singles) folder (no per-track folders for yt-dlp)
- Albums -> Albums/<album_name>
- Playlists -> Playlists/<playlist_name>
- Errors folder next to Tracks/Albums/Playlists for single-track failures
- Playlist/Album keep their own failed_tracks.txt & sources_used.txt (one file per playlist)
- Tracks keep centralized tracks/sources_used.txt and Errors/failed_tracks.txt
All previous features preserved: SpotDL fallback, yt-dlp rescue, lyric handling, memes, etc.
"""

import os
import re
import json
import shutil
import subprocess
import random
import time
from datetime import datetime,timezone

# colorama
try:
    from colorama import Fore, Style, init
except Exception:
    subprocess.run(["pip", "install", "colorama"], check=True)
    from colorama import Fore, Style, init

init(autoreset=True)

# -------------------------
# Helpers
# -------------------------
def safe_name(raw: str, maxlen: int = 60) -> str:
    s = re.sub(r"[^\w\s\-]", "", raw or "")
    s = re.sub(r"\s+", "_", s.strip())
    return s[:maxlen] or "untitled"

def rainbow_text(text: str) -> str:
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    return "".join(colors[i % len(colors)] + ch for i, ch in enumerate(text))

def rick_ascii(rainbow=False):
    art = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⣘⣩⣅⣤⣤⣄⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⢈⣻⣿⣿⢷⣾⣭⣯⣯⡳⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠻⠿⡻⢿⠿⡾⣽⣿⣳⣧⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢰⡶⢈⠐⡀⠀⠀⠁⠀⠀⠀⠈⢿⡽⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢫⢅⢠⣥⣐⡀⠀⠀⠀⠀⠀⠀⢸⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠆⠡⠱⠒⠖⣙⠂⠈⠵⣖⡂⠄⢸⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠆⠀⠰⡈⢆⣑⠂⠀⠀⠀⠀⠀⠏⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢗⠀⠱⡈⢆⠙⠉⠃⠀⠀⠀⠀⠃⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⡡⢘⠩⠯⠒⠀⠀⠀⢀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⢔⡢⢡⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⢆⠸⡁⠋⠃⠁⠀⢀⢠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡰⠌⣒⠡⠄⠀⢀⠔⠁⣸⣿⣷⣤⣀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣐⣤⡄⠀⠀⠘⢚⣒⢂⠇⣜⠒⠉⠀⢀⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣦⣔⣀⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡀⢀⢠⣤⣶⣿⣿⣿⡆⠀⠀⠐⡂⠌⠐⠝⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢨⣶⣿⣿⣿⣿⣿⣿⣿⣿⣤⡶⢐⡑⣊⠀⡴⢤⣀⣀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠷⡈⠀⠶⢶⣰⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣉⠑⠚⣙⡒⠒⠲⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀
⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⠶⠀⠀⠤⣬⣍⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀
⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⣙⠀⢠⠲⠖⠶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣭⣰⢘⣙⣛⣲⣿⣿⣿⣿⡿⡻⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀
⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠶⢾⡠⢤⣭⣽⣿⣿⣿⣿⡟⣱⠦⠄⠤⠐⡄⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀⠀
⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡛⣻⡕⠶⠶⣿⣿⣿⣿⣿⣿⣗⣎⠒⣀⠃⡐⢀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀
⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣭⣹⣏⣛⣛⣿⣿⣿⣿⣿⣿⣿⣞⣍⣉⢉⠰⠀⠠⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠅
⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠶⢼⡧⢤⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣣⣡⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣅
⡿⣷⣽⡿⠛⠋⠉⣉⡐⠶⣾⣾⣟⣻⡕⠶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣹⣫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠗
⢸⣿⣟⣥⡶⢘⡻⢶⡹⣛⣼⣿⣯⣽⢯⣙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⣿⣿⣿⣿⣿⣿⡿⠿⠟⠁⠀
⠘⢟⣾⣿⣿⣚⠷⣳⢳⣫⣽⣿⣛⣾⡷⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠁⠀⠈⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠙⢋⣿⣿⣯⣙⣯⣵⣿⣿⣯⣽⣟⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠛⢻⠟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣟⡟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣡⣿⣿⣿⣿⡗⣮⢻⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

Never gonna give you up. Never gonna let you down.
"""
    print(rainbow_text(art) if rainbow else Fore.WHITE + art)

def print_banner():
    banner = r"""
                        ░▒█▀▀▀█░▄▀▀▄░▄▀▀▄░▀█▀░░▀░░▒█▀▀▄░█▀▀░█▀▀▄░█▀▄▀█
                        ░░▀▀▀▄▄░█▄▄█░█░░█░░█░░░█▀░▒█▀▀▄░█▀▀░█▄▄█░█░▀░█
                        ░▒█▄▄▄█░█░░░░░▀▀░░░▀░░▀▀▀░▒█▄▄█░▀▀▀░▀░░▀░▀░░▒▀

                          SpotiBeam V7 Ultra GodMode - V7-Airborne
        
        
    """
    print(Fore.CYAN + Style.BRIGHT + banner)

def random_greeting():
    print(Fore.MAGENTA + random.choice([
        "💡 V7-Airborne: Light & deadly.",
        "🧦 Socks calibrated. Potatoes stabilized.",
        "🚀 Rescue mode online. 4-thread vibes.",
        "🎧 Your commands shall echo through the multiverse."
        "🔊 Booting up SpotiBeam with 9999W of bass...",
        "🎵 Injecting meme-fueled logic cores...",
        "🌀 Summoning @Elon_baby’s secret playlist...",
        "📡 Connecting to Rick Astley’s private server...",
        "🎧 Activating OverLord audio supremacy...",
        "💜 Your vibe is loading... please wait...",
        "🔥 SpotiBeam V7 Airborne engaged! Downloading pure bangers only."
    ]))

# -------------------------
# Dependency check
# -------------------------
def check_dependencies():
    # spotdl and yt-dlp via pip; ffmpeg is system binary
    for tool in ("spotdl", "yt-dlp"):
        try:
            subprocess.run([tool, "--version"], capture_output=True, check=True)
        except Exception:
            print(Fore.YELLOW + f"📦 Installing {tool} via pip...")
            subprocess.run(["pip", "install", tool], check=True)
    # ffmpeg check
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
    except Exception:
        print(Fore.RED + "⚠ ffmpeg not found in PATH. Install ffmpeg for conversions (ffmpeg.org).")

# -------------------------
# Engine
# -------------------------
class SpotiBeam:
    def __init__(self):
        self.base = "SpotiBeam_Downloads"
        # parent folders now: Tracks, Albums, Playlists, Errors
        self.tracks_folder = os.path.join(self.base, "Tracks")
        self.albums_folder = os.path.join(self.base, "Albums")
        self.playlists_folder = os.path.join(self.base, "Playlists")
        self.errors_folder = os.path.join(self.base, "Errors")
        for p in (self.tracks_folder, self.albums_folder, self.playlists_folder, self.errors_folder,
                  os.path.join(self.tracks_folder, "Lyrics")):
            os.makedirs(p, exist_ok=True)

    # get spotify name (meta)
    def get_spotify_name(self, link):
        try:
            out = subprocess.run(["spotdl", "meta", link], capture_output=True, text=True, check=True)
            meta = json.loads(out.stdout.strip())
            return safe_name(meta.get("name", link))
        except Exception:
            return safe_name(link)

    # route folder: Tracks (single-track) -> central Tracks folder
    # album/playlist -> Album/<album_name> or Playlists/<playlist_name>
    def route_folder(self, mode, link_or_query):
        if mode == "track":
            return self.tracks_folder
        elif mode == "album":
            if link_or_query.startswith("http") and "spotify" in link_or_query:
                name = self.get_spotify_name(link_or_query)
            else:
                name = safe_name(link_or_query)
            return os.path.join(self.albums_folder, name)
        elif mode == "playlist":
            if link_or_query.startswith("http") and "spotify" in link_or_query:
                name = self.get_spotify_name(link_or_query)
            else:
                name = safe_name(link_or_query)
            return os.path.join(self.playlists_folder, name)
        else:
            return self.tracks_folder

    # move lyrics to folder/Lyrics (for playlist/album) or Tracks/Lyrics for tracks
    def handle_lyrics(self, folder, mode):
        if mode == "track":
            lyrics_target = os.path.join(self.tracks_folder, "Lyrics")
        else:
            lyrics_target = os.path.join(folder, "Lyrics")
        os.makedirs(lyrics_target, exist_ok=True)
        for f in os.listdir(folder):
            if f.endswith(".lrc"):
                try:
                    shutil.move(os.path.join(folder, f), os.path.join(lyrics_target, f))
                except Exception:
                    pass

    # expected filename using spotdl meta (for skip-check)
    def expected_filename_for(self, track):
        try:
            out = subprocess.run(["spotdl", "meta", track], capture_output=True, text=True, check=True)
            meta = json.loads(out.stdout.strip())
            if meta.get("name") and meta.get("artists"):
                return safe_name(f"{meta['artists'][0]} - {meta['name']}.mp3")
        except Exception:
            return None

    # yt-dlp rescue - always writes into folder (no per-track folder)
    def ytdlp_rescue(self, query, folder, site_hint=None):
        """
        site_hint: 'youtube' or 'soundcloud' (influences search prefix)
        Returns: filename if success else None
        """
        out_template = os.path.join(folder, "%(title)s.%(ext)s")
        if site_hint == "soundcloud":
            prefix = "scsearch1:"
        else:
            prefix = "ytsearch1:"

        full_query = query
        if not (query.startswith("ytsearch") or query.startswith("scsearch")):
            full_query = f"{prefix}{query}"

        cmd = [
            "yt-dlp", full_query,
            "-x", "--audio-format", "mp3", "--audio-quality", "0",
            "-o", out_template,
            "--no-playlist", "--retries", "2", "--ignore-errors"
        ]
        try:
            subprocess.run(cmd, check=True)
            mp3s = [f for f in os.listdir(folder) if f.lower().endswith(".mp3")]
            if not mp3s:
                return None
            newest = max((os.path.join(folder, f) for f in mp3s), key=os.path.getmtime)
            if os.path.getsize(newest) > 100 * 1024:
                return os.path.basename(newest)
            else:
                try:
                    os.remove(newest)
                except Exception:
                    pass
                return None
        except Exception:
            return None

    # main download (synchronous)
    def download(self, link_or_query, mode):
        folder = self.route_folder(mode, link_or_query)
        os.makedirs(folder, exist_ok=True)
        print(Fore.CYAN + f"\n🎯 Target folder: {folder}")

        # fallback order
        sources = ["youtube-music", "bandcamp", "youtube", "soundcloud"]

        # define where to store failed file & sources log
        if mode == "track":
            failed_file = os.path.join(self.errors_folder, "failed_tracks.txt")
            sources_log = os.path.join(self.tracks_folder, "sources_used.txt")
        else:
            failed_file = os.path.join(folder, "failed_tracks.txt")
            sources_log = os.path.join(folder, "sources_used.txt")

        # build track list (playlist/album meta) or single-item list
        if mode in ("playlist", "album") and link_or_query.startswith("http") and "spotify" in link_or_query:
            try:
                out = subprocess.run(["spotdl", "meta", link_or_query], capture_output=True, text=True, check=True)
                meta = json.loads(out.stdout.strip())
                track_list = [t.get("url") for t in meta.get("tracks", []) if t.get("url")]
                if not track_list:
                    track_list = [link_or_query]
            except Exception:
                track_list = [link_or_query]
        else:
            # If failed_tracks.txt exists (retry), prefer it for this folder/mode
            if os.path.exists(failed_file):
                with open(failed_file, "r", encoding="utf-8") as fh:
                    retry_items = [line.strip() for line in fh if line.strip()]
                if retry_items:
                    print(Fore.YELLOW + f"📜 Retrying {len(retry_items)} items from {failed_file}")
                    track_list = retry_items
                else:
                    track_list = [link_or_query]
            else:
                track_list = [link_or_query]

        failed_tracks, skipped, downloaded = [], [], []

        def log_source(track, source, note=""):
            try:
                with open(sources_log, "a", encoding="utf-8") as s:
                    ts = datetime.now(timezone.utc).isoformat()
                    s.write(f"{ts} || {track} || {source} {('|| ' + note) if note else ''}\n")
            except Exception:
                pass

        # iterate synchronously
        for idx, track in enumerate(track_list, start=1):
            print(Fore.MAGENTA + f"\n🎵 Searching [{idx}/{len(track_list)}] {track}")

            expected_name = self.expected_filename_for(track)

            # skip check: expected_name located in folder OR any matching mp3 exists that likely belongs
            if expected_name:
                expected_path = os.path.join(folder, expected_name)
                if os.path.exists(expected_path) and os.path.getsize(expected_path) > 100 * 1024:
                    print(Fore.GREEN + "   ✅ Already downloaded, skipping.")
                    skipped.append(track)
                    log_source(track, "skipped")
                    continue

            # Try fallback sources
            track_success = False
            # If user typed a query like "Artist - Title", create stripped query for rescue attempts
            stripped_query = None
            if " - " in track and not track.startswith("http"):
                stripped_query = track.split(" - ", 1)[1].strip()

            for src in sources:
                print(Fore.YELLOW + f"   → Trying source: {src}")

                for attempt in (1, 2):  # 2 attempts per source
                    print(Fore.CYAN + f"     Attempt {attempt}...")
                    # cleanup incomplete files small files before attempt
                    for f in os.listdir(folder):
                        try:
                            pathf = os.path.join(folder, f)
                            if f.endswith(".part") or (f.lower().endswith(".mp3") and os.path.getsize(pathf) < 100 * 1024):
                                os.remove(pathf)
                        except Exception:
                            pass

                    try:
                        # call spotdl for this source (we capture return code)
                        cmd = [
                            "spotdl", "download", track,
                            "--output", folder,
                            "--format", "mp3",
                            "--audio", src,
                            "--threads", "4",
                            "--generate-lrc"
                        ]
                        proc = subprocess.run(cmd, capture_output=True, text=True)

                        # If spotdl returned non-zero, treat as fail for spotdl step
                        if proc.returncode != 0:
                            # Bandcamp sometimes produces JSON decode noise; handle gracefully
                            if src == "bandcamp":
                                print(Fore.RED + "     ⚠ Bandcamp: no results or provider error (handled).")
                            else:
                                err = (proc.stderr or proc.stdout or "")[:180].strip()
                                if err:
                                    print(Fore.RED + f"     ⚠ SpotDL: {err}")
                        # Validate produced files
                        valid = False
                        actual_filename = None
                        if expected_name:
                            expath = os.path.join(folder, expected_name)
                            if os.path.exists(expath) and os.path.getsize(expath) > 100 * 1024:
                                valid = True
                                actual_filename = expected_name
                        if not valid:
                            mp3s = [f for f in os.listdir(folder) if f.lower().endswith(".mp3")]
                            if mp3s:
                                newest = max((os.path.join(folder, f) for f in mp3s), key=os.path.getmtime)
                                if os.path.getsize(newest) > 100 * 1024:
                                    valid = True
                                    actual_filename = os.path.basename(newest)
                                else:
                                    try:
                                        os.remove(newest)
                                    except Exception:
                                        pass

                        if valid:
                            print(Fore.GREEN + f"   ✅ Success via {src}")
                            downloaded.append(track)
                            log_source(track, src)
                            self.handle_lyrics(folder, mode)
                            track_success = True
                            break  # break attempts loop

                        # If spotdl didn't give valid file AND src is youtube/soundcloud -> try yt-dlp rescue
                        if src in ("youtube", "soundcloud"):
                            # try direct full query first via yt-dlp
                            rescue = self.ytdlp_rescue(track, folder, site_hint=src if src == "soundcloud" else "youtube")
                            if rescue:
                                print(Fore.GREEN + f"   ✅ Success via yt-dlp rescue ({src}) -> {rescue}")
                                downloaded.append(track)
                                log_source(track, f"yt-dlp({src})")
                                self.handle_lyrics(folder, mode)
                                track_success = True
                                break  # got it
                            # if rescue failed and stripped_query exists, try that
                            if stripped_query:
                                rescue2 = self.ytdlp_rescue(stripped_query, folder, site_hint=src if src == "soundcloud" else "youtube")
                                if rescue2:
                                    print(Fore.GREEN + f"   ✅ Success via yt-dlp rescue ({src}) stripped -> {rescue2}")
                                    downloaded.append(track)
                                    log_source(track, f"yt-dlp({src})")
                                    self.handle_lyrics(folder, mode)
                                    track_success = True
                                    break

                        # no valid result this attempt
                        print(Fore.RED + f"   ⚠ No valid MP3 after {src} attempt {attempt}")
                        time.sleep(0.6)

                    except Exception as e:
                        print(Fore.RED + f"   ❌ Exception during {src} attempt: {e}")
                        time.sleep(0.6)

                if track_success:
                    break  # go to next track
                else:
                    # try next src
                    continue

            if not track_success:
                print(Fore.RED + f"   ❌ All sources failed for track: {track}")
                failed_tracks.append(track)
                log_source(track, "failed")

        # done iterating tracks

        # write failed file (playlist/album) or append to Errors/failed_tracks.txt (tracks)
        if mode == "track":
            if failed_tracks:
                try:
                    with open(failed_file, "a", encoding="utf-8") as fh:
                        for t in failed_tracks:
                            fh.write(f"{datetime.now(timezone.utc).isoformat()} || {t}\n")
                except Exception:
                    pass
        else:
            if failed_tracks:
                try:
                    with open(failed_file, "w", encoding="utf-8") as fh:
                        fh.write("\n".join(failed_tracks))
                except Exception:
                    pass
            else:
                # remove old failed file if no failures now
                if os.path.exists(failed_file):
                    try:
                        os.remove(failed_file)
                    except Exception:
                        pass

        # print final summary
        print(Fore.CYAN + "\n📊 Summary:")
        print(Fore.GREEN + f"  ✅ Downloaded: {len(downloaded)}")
        print(Fore.YELLOW + f"  ⏭ Skipped: {len(skipped)}")
        print(Fore.RED + f"  ❌ Failed: {len(failed_tracks)}")

        if not downloaded and not skipped:
            rick_ascii(rainbow=True)
        elif failed_tracks:
            # tell user where they are stored
            if mode == "track":
                print(Fore.YELLOW + f"⚠ {len(failed_tracks)} failed. Stored in {failed_file}")
            else:
                print(Fore.YELLOW + f"⚠ {len(failed_tracks)} failed. Playlist/Album failed list saved in the folder: {failed_file}")
        else:
            print(Fore.GREEN + "🎉 All tracks complete — OverLord approves.")

# -------------------------
# CLI (synchronous)
# -------------------------
def main():
    print_banner()
    random_greeting()
    check_dependencies()
    engine = SpotiBeam()
    while True:
        print(Fore.CYAN + "\n======= ULTIMATE TERMINAL =======")
        print("1. Download Playlist")
        print("2. Download Album")
        print("3. Download Track (Name or URL)")
        print("4. Exit")
        choice = input(Fore.YELLOW + "\nYour command, OverLord: ").strip()
        if choice == "1":
            url = input("Paste Spotify Playlist URL: ").strip()
            engine.download(url, "playlist")
        elif choice == "2":
            url = input("Paste Spotify Album URL: ").strip()
            engine.download(url, "album")
        elif choice == "3":
            q = input("Enter Song Name or Spotify Track URL: ").strip()
            engine.download(q, "track")
        elif choice == "4":
            print(Fore.CYAN + "\nFarewell, Supreme Meme Being.")
            break
        else:
            rick_ascii(rainbow=True)
            print(Fore.RED + "Invalid input. Try 1-4. SUS detected.")

if __name__ == "__main__":
    main()
