import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment
st.title("Speech to text converter")
st.header("Browse a file or start recording")
col1,col2 = st.columns(2)
option1=col1.button("Record")
option2=col2.button("Browse file")
browse=True
r = sr.Recognizer()
if option1==True:
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
             st.write(text)

