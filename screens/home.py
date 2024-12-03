import streamlit as st


def app():
    st.write("<h1 style='text-align: center;'>Welcome to DreamWeaver AI</h1>", unsafe_allow_html=True)
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
