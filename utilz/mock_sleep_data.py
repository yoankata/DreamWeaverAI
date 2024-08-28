import numpy as np

def get_mock_sleep_data():
    current_data = {
        "Monday": 7.5,
        "Tuesday": 6.0,
        "Wednesday": 8.0,
        "Thursday": 7.0,
        "Friday": 5.5,
        "Saturday": 8.5,
        "Sunday": 9.0
    }

    # Simple model to project next week's sleep
    improvement_factor = 1.1  # Assuming a 10% improvement with AI recommendations

    projected_data = {day: round(hours * improvement_factor, 1) for day, hours in current_data.items()}

    return current_data, projected_data