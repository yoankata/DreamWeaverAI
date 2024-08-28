import streamlit as st

def app():
    st.title("Welcome to DreamWeaver AI")
    st.set_page_config(page_title="DreamWeaver AI" ,page_icon=None, layout="wide", initial_sidebar_state="expanded", menu_items=None)
    video_file = open("videos/DreamWeaverAILogovideo.mp4", "rb")
    video_bytes = video_file.read()
    st.video(video_bytes, format="video/mp4", loop=True, autoplay=True)
