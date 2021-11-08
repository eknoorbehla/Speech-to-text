import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment
import sounddevice as sd
from scipy.io.wavfile import write

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
    freq = 44100
    duration = 5
    recording = sd.rec(int(duration * freq), 
                   samplerate=freq, channels=2)
    sd.wait()
    write("recording0.wav", freq, recording)
    wf="recording0.wav"
    with sr.AudioFile(wf) as source:
             audio_data = r.record(source)
             text = r.recognize_google(audio_data)
             st.write("Your text")
             st.success(text)
