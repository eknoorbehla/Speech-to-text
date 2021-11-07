import streamlit as st
import speech_recognition as sr
st.title("Speech to text converter")
st.header("Browse a file or start recording")
col1,col2 = st.columns(2)
rec=col1.button("Record")
browse=col2.button("Browse file")
r = sr.Recognizer()
if browse==True:
    filename = st.file_uploader("Upload Files",type=['wav','mp4'])
    if filename is not None:
        st.write("Done")
        with sr.AudioFile(filename) as source:
             st.write("Done")
             audio_data = r.record(source)
             text = r.recognize_google(audio_data)
             st.write(text)
