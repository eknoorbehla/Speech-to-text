import streamlit as st
import speech_recognition as sr
st.title("Speech to text converter")
st.header("Browse a file or start recording")
col1,col2 = st.columns(2)
rec=col1.button("Record")
browse=col2.button("Browse file")
browse=True
r = sr.Recognizer()
if browse==True:
    filename = st.file_uploader("Upload Files",type=['wav','mp4'])
    st.write(filename)
    if filename is None:
        st.write("Please upload a file")
    else:
        st.write("ghfjhf")
        filename = AudioSegment.from_wav(filename)
        filename.export("extracted.wav",format="wav")
        filename="extracted.wav"
        with sr.AudioFile(filename) as source:
             st.write("Done")
             audio_data = r.record(source)
             text = r.recognize_google(audio_data)
             st.write(text)
st.write("Hello")
