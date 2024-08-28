import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyDZusS0lb_FowVv8ZDTWNqsbJo00g0_oiI"
MAIN_MODEL = 'gemini-pro'

def getLLamaSleepscapeResponse(input_text, no_words, sleepscape_type):
    
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel(MAIN_MODEL)

    response = model.generate_content(f"""
        Write a {sleepscape_type} story for a topic {input_text}
        of around {no_words} words in length. Return story only without wordcount or title.
    """)
    
    return response.text

def get_ai_recommendations_from_api(responses):

    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel(MAIN_MODEL)

    # Construct the input text from the responses
    input_text = f"""
    The user has the following sleep habits:
    - Bedtime consistency: {responses['bedtime_consistency']}
    - Caffeine intake: {responses['caffeine_intake']}
    - Screen time before bed: {responses['screen_time']}
    - Stress level before bed: {responses['stress_level']}
    - Physical activity during the day: {responses['physical_activity']}
    
    Based on these habits, please provide personalized recommendations to improve the user's sleep quality.
    """

    response = model.generate_content(f"""
        Analyze the following sleep habits and provide personalized sleep improvement recommendations:
        {input_text}
    """)

    return response.text