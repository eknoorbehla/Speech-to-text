import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment

st.title("SPEECH TO TEXT CONVERTER")
st.header("Browse an audio file to convert")
r = sr.Recognizer()
filename = st.file_uploader("Upload Files",type=['wav','mp4'])
if filename is None:
    st.write("Please upload a file")
else:
    filename = AudioSegment.from_wav(filename)
    filename.export("extracted.wav",format="wav")
    filename="extracted.wav"
    with sr.AudioFile(filename) as source:
         audio_data = r.record(source)
         text = r.recognize_google(audio_data)
         st.write("Your text")
         st.success(text)
