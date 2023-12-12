import requests
from backend.config import Config
from datetime import datetime
from backend.constants import EXERCISE_DB_FILE, EXERCISE_END_POINT
from backend.pixela.graph_pixels import manage_pixel_entry

from database.csv_manager import CSVManager


def get_exercise_info(exercise_input, username, graph_id):
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
        date = datetime.now().strftime("%Y%m%d")
        total_calories = int(total_calories)
        CSVManager(EXERCISE_DB_FILE).store_data(
            time_of_exercise=time_of_exercise,
            username=username,
            exercise_input=exercise_input,
            total_calories=total_calories
        )
        if manage_pixel_entry(username, graph_id, -1 * total_calories, date):
            return "Exercise Data stored successfully."
    else:
        return f"Error: {response.status_code}, {response.text}"
