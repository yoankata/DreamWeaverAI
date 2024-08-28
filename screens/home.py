import streamlit as st

st.set_page_config(page_title=None, page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)

def app():
    st.title("Welcome to DreamWeaver AI")
    with open("videos/DreamWeaverAILogovideo.mp4", "rb") as video_file:
        video_bytes = video_file.read()
    st.video(video_bytes, format="video/mp4", loop=True, autoplay=True, use_container_width=True)
