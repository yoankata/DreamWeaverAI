import numpy as np
import streamlit as st
import google.generativeai as genai
import soundfile as sf
from gtts import gTTS
import streamlit_scrollable_textbox as stx
import pyttsx3
import os
import random
from difflib import get_close_matches


## Function To get response from LLAma 2 model
def getLLamaSleepscapeResponse(input_text, no_words, sleepscape_type):
    GOOGLE_API_KEY="AIzaSyDZusS0lb_FowVv8ZDTWNqsbJo00g0_oiI"
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    

    response = model.generate_content("""
        Write a {sleepscape_type} story for a topic {input_text}
        of around {no_words} words in length. Return story only without wordcount or title.
        """)
    
    print(response.text)
    return response.text

def text_to_speech(text, filename='bedtime_story.mp3'):
    # tts = gTTS(text=text, lang='en', tld='com', slow=True)
    # tts.save(filename)

    engine = pyttsx3.init()  # object creation
    engine.setProperty('rate', 125)  # setting up new voice rate
    engine.setProperty('volume', 1)  # setting up volume level  between 0 and 1
    voices = engine.getProperty('voices')  # getting details of current voice
    engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male, 1 for female
    #engine.say(text=text)
    engine.save_to_file(text=text, filename=filename)
    engine.runAndWait()
    engine.stop()


def generate_white_noise(duration, file, sample_rate=44100):
    samples = np.random.normal(0, 0.1, size=int(duration * sample_rate))
    sf.write(file, samples, sample_rate)
    return True

def generate_natural_noise(duration, file, sample_rate=44100):
    samples = np.random.normal(0, 0.1, size=int(duration * sample_rate))
    sf.write(file, samples, sample_rate)
    return True

def find_sound(query):
    sound_folder = "sounds"
    sound_files = [f for f in os.listdir(sound_folder) if f.endswith('.wav')]

    # Convert filenames to simple names (without extension)
    simple_names = [os.path.splitext(f)[0].lower() for f in sound_files]

    # Try to find a close match
    matches = get_close_matches(query.lower(), simple_names, n=1, cutoff=0.6)
    
    if matches:
        # Return the matched sound file
        return os.path.join(sound_folder, sound_files[simple_names.index(matches[0])])
    else:
        # Return a random sound file if no match found
        return os.path.join(sound_folder, random.choice(sound_files))

st.set_page_config(page_title="DreamWeaver AI POC!",
                    page_icon='💤',
                    layout='wide',
                    initial_sidebar_state='collapsed')

## creating to more columns for additonal 2 fields
col01, col02=st.columns([5,5])

with col01:
    # logo=st.image('images/Leonardo_Phoenix_create_a_logo_for_a_an_AI_sleep_assistant_app_3.jpg', use_column_width='always')
    video_file = open("videos/DreamWeaverAILogovideo.mp4", "rb")
    video_bytes = video_file.read()
    st.video(video_bytes, format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=True, autoplay=True, muted=False)

with col02:

    input_text=st.text_input("Enter the Sleepscape topic 😴")

    ## creating to more columns for additonal 2 fields
    col1, col2=st.columns([3,5])

    with col1:
        no_words=st.text_input('No of Words')
    with col2:
        sleepscape_type=st.selectbox('Sleepscape type', ('Bedtime story','Meditation','Natural noise','White noise'),index=0)

    submit=st.button("Generate")

## Final response
if submit:
    if sleepscape_type == "Bedtime story":
        with col02:
            with st.status(f'\nGenerating a Story...\n'):
                story = getLLamaSleepscapeResponse(input_text, no_words, sleepscape_type)
                stx.scrollableTextbox(f' {story}', height = 200)
            with st.status(f'\nGenerating Audio...\n'):
                text_to_speech(story, "bedtime_story.mp3")
                st.audio("bedtime_story.mp3", format="audio/mpeg", loop=True, autoplay = True)
                
    elif sleepscape_type == "Meditation":
        with col02:
            with st.status(f'\nGenerating Meditation...\n'):
                story = getLLamaSleepscapeResponse(input_text, no_words, sleepscape_type)
                stx.scrollableTextbox(f' {story}', height = 200)
            with st.status(f'\nGenerating Audio...\n'):
                text_to_speech(story, "meditation.mp3")
                st.audio("meditation.mp3", format="audio/mpeg", loop=True, autoplay = True)
    
    elif sleepscape_type == "White noise":        
        with col02:
            with st.status("\nGenerating White Noise Audio...\n"):
                generate_white_noise(15, "white_noise.wav")
                st.audio("white_noise.wav", format="audio/wav", loop=True, autoplay = True)

    else: # Natural noise
        with col02:
            with st.status("\nGenerating Natural Noise Audio...\n"):
                natural_sound = find_sound(input_text)
                st.audio(natural_sound, format="audio/wav", loop=True, autoplay = True)

