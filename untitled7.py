import streamlit as st
import speech_recognition as sr
st.title("Speech to text converter")
st.header("Browse a file or start recordingcbgfnn")
col1,col2 = st.columns(2)
record1 = col1.button("Record")
browse1 = col2.button("Browse file")
r = sr.Recognizer()
filename="Welcome.wav"
record = st.button("Record")
with sr.AudioFile(filename) as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data)
    st.write(text)
