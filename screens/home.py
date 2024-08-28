import streamlit as st

st.set_page_config(page_title="DreamWeaver AI", page_icon=":flag-ee:", layout="centered", initial_sidebar_state="auto")

def app():
    st.title("Welcome to DreamWeaver AI")
    with open("videos/DreamWeaverAILogovideo.mp4", "rb") as video_file:
        video_bytes = video_file.read()
    # CSS to adjust video size
    st.markdown("""
    <style>
    .stVideo {
        width: 100%;
        max-width: 800px;  /* Adjust this value as needed */
        margin: 0 auto;
        display: block;
        max-height: 100vh;  /* Adjusts the max height to fit the viewport height */
    }
    </style>
    """, unsafe_allow_html=True)
    st.video(video_bytes, format="video/mp4", loop=True, autoplay=True)
