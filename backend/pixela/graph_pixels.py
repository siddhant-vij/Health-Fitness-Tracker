import time
import requests
from backend.constants import USER_DB_FILE, USER_END_POINT
from database.csv_manager import CSVManager


def get_pixel_value(pixel_url, token):
    pixel_headers = {
        "X-USER-TOKEN": token
    }
    response = requests.get(pixel_url, headers=pixel_headers)
    while response.status_code == 503:
        time.sleep(5)
        response = requests.get(pixel_url, headers=pixel_headers)
    if response.status_code == 200:
        data = response.json()
        return data.get("quantity")
    elif response.status_code == 404:
        return "0"
    else:
        return None


def update_pixel(username, token, graph_id, quantity, date):
    pixel_url = f"{USER_END_POINT}/{username}/graphs/{graph_id}/{date}"
    pixel_headers = {
        "X-USER-TOKEN": token
    }
    current_pixel_value = get_pixel_value(pixel_url, token)
    if current_pixel_value is None:
        return False
    elif current_pixel_value == "0":
        new_value = quantity
    else:
        new_value = int(current_pixel_value) + quantity
    pixel_body = {
        "quantity": str(new_value)
    }
    response = requests.put(pixel_url, json=pixel_body, headers=pixel_headers)
    while response.status_code == 503:
        time.sleep(5)
        response = requests.put(pixel_url, json=pixel_body, headers=pixel_headers)
    return response.status_code == 200


def get_user_token(username):
    users = CSVManager(USER_DB_FILE).read_data()
    for user in users:
        if user['username'] == username:
            return user['token']
    return None


def manage_pixel_entry(username, graph_id, calorie_data, date):
    token = get_user_token(username)
    if token is None:
        print("User token not found.")
        return False

    if not update_pixel(username, token, graph_id, calorie_data, date):
        print("Failed to update pixel.")
        return False
    else:
        print("Pixel updated successfully.")
        return True
