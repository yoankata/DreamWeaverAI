import streamlit as st

st.set_page_config(page_title="DreamWeaver AI", page_icon=":flag-ee:", layout="centered", initial_sidebar_state="auto")

def app():
    # CSS to set the page height to 70vh
    st.markdown("""
        <style>
        html, body {
            height: 70vh;
            margin: 0;
            padding: 0;
        }
        </style>
        """, unsafe_allow_html=True)
    st.title("Welcome to DreamWeaver AI")
    with open("videos/DreamWeaverAILogovideo.mp4", "rb") as video_file:
        video_bytes = video_file.read()
    st.video(video_bytes, format="video/mp4", loop=True, autoplay=True)
