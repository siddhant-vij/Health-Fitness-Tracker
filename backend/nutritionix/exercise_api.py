import requests
from backend.config import Config
from datetime import datetime


EXERCISE_END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"


def get_exercise_info(exercise_input):
    headers = {
        'Content-Type': 'application/json',
        'x-app-id': Config.NUTRITIONIX_APP_ID,
        'x-app-key': Config.NUTRITIONIX_API_KEY,
    }
    body = {
        "query": exercise_input
    }
    response = requests.post(EXERCISE_END_POINT, headers=headers, json=body)
    if response.status_code == 200:
        data = response.json()
        exercises = data.get('exercises', [])
        if not exercises:
            return "No data found for the input."

        formatted_data = []
        for item in exercises:
            exercise_info = {
                'Exercise Name': item.get('name'),
                'Calories Burned': item.get('nf_calories'),
                'Time of Exercise': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            formatted_data.append(exercise_info)
        return formatted_data
    else:
        return f"Error: {response.status_code}, {response.text}"
