import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment
import sounddevice as sd
st.title("Speech to text converter")
st.header("Browse a file or start recording")
col1,col2 = st.columns(2)
option=st.selectbox("Choose",['Choose an option','Record','Browse file'])
r = sr.Recognizer()
if option=="Browse file":
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
elif option=="Record":
    fs = 44100  # Sample rate
    seconds = 10  # Duration of recording
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('output.wav', fs, myrecording)
    filename = 'output.wav'
    with sr.AudioFile(filename) as source:
             audio_data = r.record(source)
             text = r.recognize_google(audio_data)
             st.write("Your text")
             st.success(text)
