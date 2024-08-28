import streamlit as st

st.set_page_config(page_title="DreamWeaver AI", page_icon=":flag-ee:", layout="centered", initial_sidebar_state="auto")

def app():
    st.markdown("<center>Welcome to DreamWeaver AI</center>", unsafe_allow_html=True)
    with open("videos/DreamWeaverAILogovideo.mp4", "rb") as video_file:
        video_bytes = video_file.read()
    
    # CSS to adjust video size
    st.markdown("""
        <style>
        .stVideo {
            margin: 0 auto;
            display: block;
            max-height: 70vh;  /* Adjusts the max height to fit the viewport height */
        }
        </style>
        """, unsafe_allow_html=True)
    st.video(video_bytes, format="video/mp4", loop=True, autoplay=True)
