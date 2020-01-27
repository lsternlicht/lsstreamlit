import io
import pathlib
import streamlit as st
import numpy as np


st.title('Audio')

def audio_name(opt):
    return str(opt).split("/")[-1]

def shorten_audio_option(opt):
    return '/'.join(str(opt).split('/')[1:])

def dayradioformat(opt):
    return {"**": "all"}.get(opt, opt)

radio = st.radio('presentation type: ', ['webcasts', 'QA', 'sides'])
dayradio = st.radio('presentation day: ', ['day1', 'day2', 'day3', 'day4', '**'], format_func=dayradioformat)
mp3s = list(set([str(i) for i in list(pathlib.Path().rglob(f'**/{dayradio}/{radio}/*.mp3'))[:]]))
st.header(radio)

st.text(f'total webcasts: {len(mp3s)}')
song = st.selectbox(
    "Pick an MP3 to play",
    mp3s,
    0,
    audio_name
)
_, _, day, presentationtype, presenter = song.split('/')

st.header(f'{day} - {presentationtype} - {presenter.split("_")[-1].split(".")[0]}')
songf = 'http://10.116.159.135:8000/' + shorten_audio_option(song)
# st.text(songf)
st.audio(songf)

