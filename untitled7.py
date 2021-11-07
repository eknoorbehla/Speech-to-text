# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12QBrFOXsoIxC-zt1xl2pWxecQGRKqjyC
"""

import streamlit as st

import speech_recognition as sr
r = sr.Recognizer()
filename="Welcome.wav"
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)

