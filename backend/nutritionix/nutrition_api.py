import requests
from backend.config import Config
from datetime import datetime


NUTRITION_END_POINT = "https://trackapi.nutritionix.com/v2/natural/nutrients"


def get_nutritional_info(food_input):
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

        formatted_data = []
        for item in foods:
            food_info = {
                'Food Name': item.get('food_name'),
                'Calories Consumed': item.get('nf_calories'),
                'Carbs (grams)': item.get('nf_total_carbohydrate'),
                'Protein (grams)': item.get('nf_protein'),
                'Fats (grams)': item.get('nf_total_fat'),
                'Time of Consumption': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            formatted_data.append(food_info)
        return formatted_data
    else:
        return f"Error: {response.status_code}, {response.text}"
