import sys
import os
import streamlit as st
import time

# Fix path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.mood_analysis.mood import get_mood
from src.music_generation.generator import get_random_song

# Page config
st.set_page_config(page_title="AI-Based Music Composition System", page_icon="🎶", layout="wide")

# 🎨 UI STYLE
st.markdown("""
<style>
.stApp {
    background-color: #eef2f7;
    color: #1e293b;
}

/* Title */
h1 {
    font-size: 42px !important;
    font-weight: 700;
}

/* Label text */
label {
    color: black !important;
    font-size: 18px !important;
    font-weight: 500;
}

/* Input */
.stTextInput input {
    background-color: #ffffff !important;
    color: black !important;
    border: 2px solid #3b82f6 !important;
    border-radius: 10px !important;
    height: 50px !important;
    font-size: 18px !important;
}

/* Buttons */
.stButton>button, .stDownloadButton>button {
    background: transparent;
    border: 2px solid #3b82f6;
    color: #3b82f6;
    border-radius: 12px;
    height: 50px;
    font-size: 18px;
    font-weight: 600;
}
.stButton>button:hover, .stDownloadButton>button:hover {
    background-color: #3b82f6;
    color: white;
}

/* Remove alert box background */
.stAlert {
    background-color: transparent !important;
    border: none !important;
}

/* Align nav right */
div[data-testid="column"] {
    display: flex;
    justify-content: flex-end;
}
</style>
""", unsafe_allow_html=True)

# 🎯 STATE
if "page" not in st.session_state:
    st.session_state.page = "Home"

if "history" not in st.session_state:
    st.session_state.history = []

if "playlist" not in st.session_state:
    st.session_state.playlist = []

if "downloads" not in st.session_state:
    st.session_state.downloads = []

# 🔝 NAV
col1, col2, col3, col4, col5 = st.columns([6,1,1,1,1])

with col2:
    if st.button("Home"):
        st.session_state.page = "Home"

with col3:
    if st.button("History"):
        st.session_state.page = "History"

with col4:
    if st.button("Playlist"):
        st.session_state.page = "Playlist"

with col5:
    if st.button("Downloads"):
        st.session_state.page = "Downloads"

# ---------------- HOME ----------------
if st.session_state.page == "Home":

    st.title("🎶 AI-Based Music Composition System")

    text = "Generate music from your feelings..."
    placeholder = st.empty()
    for i in range(len(text)+1):
        placeholder.markdown(f"### {text[:i]}")
        time.sleep(0.02)

    user_input = st.text_input("Describe your mood or situation:")

    if st.button("🎵 Generate Music", use_container_width=True):

        if user_input:

            with st.spinner("Analyzing mood & generating music..."):
                time.sleep(2)

            mood_genre = get_mood(user_input)
            song_path = get_random_song(mood_genre)

            # 🎧 GENRE TEXT + AUDIOWAVE STYLE
            st.markdown(f"""
<div style="display:flex; flex-direction:column; align-items:center; margin-top:10px;">

<h4 style="color:#16a34a; font-weight:600;">
🎧 Detected Genre: {mood_genre}
</h4>

<style>
.wave-container {{
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 20px;
}}

.wave {{
    display: flex;
    align-items: center;
    gap: 4px;
}}

.wave span {{
    width: 6px;
    border-radius: 5px;
    background: linear-gradient(to top, #8a2be2, #ff416c);
    animation: bounce 1.2s infinite ease-in-out;
}}

/* 🔥 PERFECT SYMMETRY HEIGHTS */
.wave span:nth-child(1) {{ height: 10px; animation-delay: 0s; }}
.wave span:nth-child(2) {{ height: 20px; animation-delay: 0.1s; }}
.wave span:nth-child(3) {{ height: 35px; animation-delay: 0.2s; }}
.wave span:nth-child(4) {{ height: 55px; animation-delay: 0.3s; }}
.wave span:nth-child(5) {{ height: 80px; animation-delay: 0.4s; }}
.wave span:nth-child(6) {{ height: 55px; animation-delay: 0.3s; }}
.wave span:nth-child(7) {{ height: 35px; animation-delay: 0.2s; }}
.wave span:nth-child(8) {{ height: 20px; animation-delay: 0.1s; }}
.wave span:nth-child(9) {{ height: 10px; animation-delay: 0s; }}

/* 🔥 SMOOTH MOTION */
@keyframes bounce {{
    0%, 100% {{
        transform: scaleY(0.8);
        opacity: 0.6;
    }}
    50% {{
        transform: scaleY(1.3);
        opacity: 1;
    }}
}}
</style>

<div class="wave-container">
    <div class="wave">
        <span></span><span></span><span></span><span></span><span></span>
        <span></span><span></span><span></span><span></span>
    </div>
</div>

</div>
""", unsafe_allow_html=True)
            if song_path:
                st.audio(song_path)
                st.session_state.current_song = song_path
                st.session_state.history.append(song_path)

        else:
            st.warning("Please enter your mood")

    # Buttons
    colA, colB = st.columns(2)

    with colA:
        if st.button("❤️ Add to Playlist", use_container_width=True):
            if "current_song" in st.session_state:
                st.session_state.playlist.append(st.session_state.current_song)
                st.success("Added to playlist")

    with colB:
        if "current_song" in st.session_state:
            with open(st.session_state.current_song, "rb") as f:
                if st.download_button("⬇ Download Music", f, file_name="music.wav"):
                    st.session_state.downloads.append(st.session_state.current_song)

# ---------------- HISTORY ----------------
elif st.session_state.page == "History":
    st.title("📜 History")
    for song in st.session_state.history[::-1]:
        st.audio(song)

# ---------------- PLAYLIST ----------------
elif st.session_state.page == "Playlist":
    st.title("❤️ Playlist")
    for i, song in enumerate(st.session_state.playlist):
        if st.button(f"▶ Play {i+1}", key=f"p{i}"):
            st.audio(song)

# ---------------- DOWNLOADS ----------------
elif st.session_state.page == "Downloads":
    st.title("⬇ Downloads")
    for song in st.session_state.downloads:
        st.audio(song)

# Footer
st.markdown("---")
st.caption("AI-Based Music Composition System • Final UI")