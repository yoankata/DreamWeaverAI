import streamlit as st
from screens import home, generate_story, generate_noise, sleep_statistics, ai_recommendations, device_integration

st.set_page_config(page_title="DreamWeaver AI", page_icon='💤', layout='wide')

# Define the routing options
PAGES = {
    "Home": home,
    "Generate Story": generate_story,
    "Generate Noise": generate_noise,
    "Sleep Statistics": sleep_statistics,
    "AI Recommendations": ai_recommendations,
    "Devices": device_integration
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]
page.app()