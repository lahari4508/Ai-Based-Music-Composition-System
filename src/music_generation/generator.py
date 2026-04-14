import os
import random
from playsound import playsound   # 🔥 important

# 🎵 Get random song based on genre
def get_random_song(genre):
    base_path = "Data/genres_original"

    genre_path = os.path.join(base_path, genre)

    if not os.path.exists(genre_path):
        print("Genre folder not found:", genre_path)
        return None

    songs = os.listdir(genre_path)

    if len(songs) == 0:
        print("No songs in folder")
        return None

    song = random.choice(songs)

    return os.path.join(genre_path, song)


# 🔊 PLAY FUNCTION (THIS WAS MISSING ❗)
def play_music(path):
    try:
        print("Playing:", path)
        playsound(path)
    except Exception as e:
        print("Error playing audio:", e)