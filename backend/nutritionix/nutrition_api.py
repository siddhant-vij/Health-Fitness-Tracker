import requests
from backend.config import Config
from datetime import datetime
from backend.constants import NUTRITION_DB_FILE, NUTRITION_END_POINT
from backend.pixela.graph_pixels import manage_pixel_entry
from database.csv_manager import CSVManager


def get_nutritional_info(food_input, username, graph_id):
    headers = {
        'Content-Type': 'application/json',
        'x-app-id': Config.NUTRITIONIX_APP_ID,
        'x-app-key': Config.NUTRITIONIX_API_KEY,
    }
    body = {
        "query": food_input
    }
    response = requests.post(NUTRITION_END_POINT, headers=headers, json=body)
    if response.status_code == 200:
        data = response.json()
        foods = data.get('foods', [])
        if not foods:
            return "No data found for the input."

        total_calories = 0
        total_carbs = 0
        total_protein = 0
        total_fats = 0
        for item in foods:
            total_calories += item.get('nf_calories')
            total_carbs += item.get('nf_total_carbohydrate')
            total_protein += item.get('nf_protein')
            total_fats += item.get('nf_total_fat')
        time_of_consumption = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        date = datetime.now().strftime("%Y%m%d")
        total_calories = int(total_calories)
        CSVManager(NUTRITION_DB_FILE).store_data(
            time_of_consumption=time_of_consumption,
            username=username,
            food_input=food_input,
            total_calories=total_calories,
            total_carbs=total_carbs,
            total_protein=total_protein,
            total_fats=total_fats
        )
        if manage_pixel_entry(username, graph_id, total_calories, date):
            return "Nutritional Data stored successfully."
    else:
        return f"Error: {response.status_code}, {response.text}"
