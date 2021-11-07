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
    if filename is None:
        st.write("Please upload a file")
    else:
        st.write("ghfjhf")
        filename = AudioSegment.from_wav(filename)
        wav.export("extracted.wav",format="wav")
        audio_bytes = open("extracted.wav",'rb').read()
        st.write("#### input sound:")
        st.audio(audio_bytes,format = f'audio/sav',start_time=0)
        with sr.AudioFile(audio_bytes) as source:
             st.write("Done")
             audio_data = r.record(source)
             text = r.recognize_google(audio_data)
             st.write(text)
st.write("Hello")
