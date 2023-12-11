import requests
from backend.config import Config
from datetime import datetime

from database.csv_manager import CSVManager


EXERCISE_END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
EXERCISE_DB_FILE = "resources/exercise_data.csv"


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

        total_calories = 0
        for item in exercises:
            total_calories += item.get('nf_calories')
        time_of_exercise = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        CSVManager(EXERCISE_DB_FILE).store_data(
            time_of_exercise=time_of_exercise,
            exercise_input=exercise_input,
            total_calories=total_calories
        )
    else:
        return f"Error: {response.status_code}, {response.text}"
