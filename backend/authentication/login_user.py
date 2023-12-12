from backend.constants import USER_DB_FILE
from database.csv_manager import CSVManager


def login_user(username):
    users = CSVManager(USER_DB_FILE).read_data()
    for user in users:
        if user['username'] == username:
            return "Login successful."

    return "Login failed. Username not found."
