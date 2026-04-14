from src.data_pipeline.load_data import load_data
from src.data_pipeline.preprocess import preprocess_data
from src.music_generation.model import train_model
from src.mood_analysis.mood import get_mood
from src.music_generation.generator import get_random_song, play_music

# Load data
df = load_data()

# Preprocess
X_train, X_test, y_train, y_test, le = preprocess_data(df)

# Train model
model = train_model(X_train, y_train)

# 🎯 User input
user_input = input("Enter your mood: ")

# Convert mood → genre
mood_genre = get_mood(user_input)

print("Predicted Genre based on mood:", mood_genre)

# 🎵 Get song and play
song_path = get_random_song(mood_genre)

if song_path:
    print("Playing song:", song_path)
    play_music(song_path)   # 🔊 plays here
else:
    print("No song found")