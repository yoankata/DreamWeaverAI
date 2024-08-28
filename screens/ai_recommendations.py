import streamlit as st
from utilz.llama_response import get_ai_recommendations_from_api

def app():
    st.title("AI-Powered Sleep Recommendations")

    st.write("Please answer the following questions to help us understand your sleep habits better. Based on your responses, we'll provide personalized recommendations to improve your sleep.")

    with st.form(key='questionnaire'):
        bedtime_consistency = st.selectbox(
            "How consistent is your bedtime?",
            ("Consistent", "Inconsistent")
        )
        
        caffeine_intake = st.selectbox(
            "How would you describe your daily caffeine intake?",
            ("Low", "Moderate", "High")
        )
        
        screen_time = st.selectbox(
            "How much time do you spend on screens (phone, TV, computer) before bed?",
            ("Low", "Moderate", "High")
        )

        stress_level = st.selectbox(
            "How would you rate your stress level before bed?",
            ("Low", "Moderate", "High")
        )

        physical_activity = st.selectbox(
            "How would you describe your physical activity during the day?",
            ("Low", "Moderate", "High")
        )

        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        responses = {
            'bedtime_consistency': bedtime_consistency,
            'caffeine_intake': caffeine_intake,
            'screen_time': screen_time,
            'stress_level': stress_level,
            'physical_activity': physical_activity,
        }

        with st.spinner("Generating your personalized sleep recommendations..."):
            recommendations = get_ai_recommendations_from_api(responses)

        st.write("### Based on your answers, here are some recommendations:")
        st.write(recommendations)