import streamlit as st
import speech_recognition as sr
r = sr.Recognizer()
filename="Welcome.wav"
with sr.AudioFile(filename) as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data)
    st.write(text)
