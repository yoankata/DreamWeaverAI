import streamlit as st

def app():
    st.title("Welcome to DreamWeaver AI")
    st.write("Navigate through the app using the sidebar to generate sleepscapes and white noise.")
    video_file = open("videos/DreamWeaverAILogovideo.mp4", "rb")
    video_bytes = video_file.read()
    st.video(video_bytes, format="video/mp4", start_time=0, loop=True, autoplay=True)