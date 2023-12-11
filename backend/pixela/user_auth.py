import requests
from backend.pixela.create_graph import create_graph
from database.csv_manager import CSVManager
from .utils import generate_token


USER_ENDPOINT = "https://pixe.la/v1/users"
USER_DB_FILE = "resources/users.csv"


def register_user(username, goal):
    token = generate_token()
    agree_terms = "yes"
    not_minor = "yes"

    user_url = USER_ENDPOINT
    user_headers = {'Content-Type': 'application/json'}
    user_body = {
        "token": token,
        "username": username,
        "agreeTermsOfService": agree_terms,
        "notMinor": not_minor
    }
    response = requests.post(user_url, json=user_body, headers=user_headers)

    if response.status_code == 200:
        if create_graph(username, token, goal):
            CSVManager(USER_DB_FILE).store_data(
                username=username,
                token=token
            )
            return "User registered successfully"
        else:
            return "Failed to create graph"
    else:
        return "Failed to register user"
