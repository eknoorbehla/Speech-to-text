import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment
import pyaudio
import wave
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
    filename = "recorded.wav"
    chunk = 1024
    FORMAT = pyaudio.paInt16
    channels = 1
    sample_rate = 44100
    record_seconds = 5
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,channels=channels,rate=sample_rate,input=True,output=True,frames_per_buffer=chunk)
    frames = []
    print("Recording...")
    for i in range(int(44100 / chunk * record_seconds)):
        data = stream.read(chunk)
    # if you want to hear your voice while recording
    # stream.write(data)
        frames.append(data)
    print("Finished recording.")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(filename, "wb")
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(sample_rate)
    wf.writeframes(b"".join(frames))
    wf.close()
    with sr.AudioFile(wf) as source:
             audio_data = r.record(source)
             text = r.recognize_google(audio_data)
             st.write("Your text")
             st.success(text)
