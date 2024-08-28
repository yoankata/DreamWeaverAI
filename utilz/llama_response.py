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
    
    Based on these habits, please provide exactly five personalized recommendations to improve the user's sleep quality.
    Each recommendation should be concise and focused on a key area.
    """

    response = model.generate_content(f"""
        Analyze the following sleep habits and provide exactly five key personalized sleep improvement recommendations:
        {input_text}
    """)

    recommendations = response.text.split('\n')
    recommendations = [rec.strip() for rec in recommendations if rec.strip() != '']
    
    if len(recommendations) > 5:
        recommendations = recommendations[:5]

    return recommendations

def get_rag_response(query, extracted_text):
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel(MAIN_MODEL)

    response = model.generate_content(f"""
        Based on the following document text, answer the query provided.

        Document Text: {extracted_text}

        Query: {query}
    """)

    return response.text