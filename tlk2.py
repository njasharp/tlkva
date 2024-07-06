import streamlit as st
from gtts import gTTS
import os

# Function to generate and play text-to-speech audio
def generate_audio(audio_text, filename="audio.mp3"):
    try:
        tts = gTTS(text=audio_text, lang='en')
        tts.save(filename)
        return filename
    except Exception as e:
        st.sidebar.error(f"Failed to generate text-to-speech: {e}")
        return None

# Streamlit app
st.title("Text Input Talk")

# Text input for user name
talk1 = st.text_input("Enter your name:")

# Button to trigger speaking the text input
if st.button("Speak!"):
    st.write("Speaking...")
    audio_file = generate_audio(talk1)
    if audio_file:
        st.audio(audio_file)

# Initialize session state variables
if 'analysis_result_text' not in st.session_state:
    st.session_state.analysis_result_text = ""

# Display the analysis result
analysis_result = st.empty()
if st.session_state.analysis_result_text:
    analysis_result.write(f"Analysis Result: {st.session_state.analysis_result_text}")

# Sidebar button to speak the analysis result
if st.sidebar.button("Speak Analysis Result"):
    audio_file = generate_audio(st.session_state.analysis_result_text)
    if audio_file:
        st.audio(audio_file)
