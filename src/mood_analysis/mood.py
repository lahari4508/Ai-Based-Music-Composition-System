def get_mood(text):
    text = text.lower()

    # 😊 Happy / Positive
    if any(word in text for word in ["happy", "joy", "excited", "fun", "good", "great"]):
        return "pop"

    # 😢 Sad / Emotional
    elif any(word in text for word in ["sad", "cry", "depressed", "alone", "upset"]):
        return "blues"

    # 😌 Calm / Relax
    elif any(word in text for word in ["calm", "relax", "peace", "sleep", "soft"]):
        return "classical"

    # ⚡ Energetic / Workout
    elif any(word in text for word in ["energy", "gym", "workout", "fast", "party"]):
        return "rock"

    # ❤️ Love / Romantic
    elif any(word in text for word in ["love", "romantic", "date"]):
        return "jazz"

    # Default fallback
    else:
        return "pop"