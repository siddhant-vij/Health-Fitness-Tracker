import requests
from backend.constants import USER_DB_FILE, USER_END_POINT
from backend.pixela.create_graph import create_graph
from database.csv_manager import CSVManager
from backend.pixela.utils import calculate_bmr, generate_token, get_activity_multiplier


def register_user(username, email, graph_id, age, gender, height, weight, activity_level):
    token = generate_token()
    agree_terms = "yes"
    not_minor = "yes"

    user_url = USER_END_POINT
    user_headers = {'Content-Type': 'application/json'}
    user_body = {
        "token": token,
        "username": username,
        "agreeTermsOfService": agree_terms,
        "notMinor": not_minor
    }
    response = requests.post(user_url, json=user_body, headers=user_headers)

    if response.status_code == 200:
        if create_graph(username, token, graph_id):
            bmr = calculate_bmr(age, weight, height, gender)
            activity_multiplier = get_activity_multiplier(activity_level)
            CSVManager(USER_DB_FILE).store_data(
                username=username,
                email=email,
                token=token,
                bmr=bmr,
                activity_multiplier=activity_multiplier
            )
            return "User registered successfully"
        else:
            return "Failed to create graph"
    else:
        return "Failed to register user"
