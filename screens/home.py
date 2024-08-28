import streamlit as st

st.set_page_config(page_title="DreamWeaver AI", page_icon=":flag-ee", layout="centered", initial_sidebar_state="auto")

def app():
    st.title("Welcome to DreamWeaver AI")
    with open("videos/DreamWeaverAILogovideo.mp4", "rb") as video_file:
        video_bytes = video_file.read()
    st.video(video_bytes, format="video/mp4", loop=True, autoplay=True)
