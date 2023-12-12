import schedule
import threading
import time
from datetime import datetime
from backend.pixela.graph_pixels import manage_pixel_entry
from database.csv_manager import CSVManager

USER_DB_FILE = "resources/users.csv"


def calculate_reduction(user):
    bmr = float(user.get('bmr'))
    activity_level = float(user.get('activity_level'))
    daily_rest_burn = bmr * activity_level
    return daily_rest_burn / (24 * 60 * 60)


def update_daily_pixel(graph_id):
    users = CSVManager(USER_DB_FILE).read_data()
    for user in users:
        username = user['username']
        reduction_value = calculate_reduction(user)
        date = datetime.now().strftime("%Y%m%d")
        manage_pixel_entry(username, graph_id, -1 * reduction_value, date)


def run_scheduler(graph_id):
    schedule.every(1).second.do(update_daily_pixel, graph_id=graph_id)
    while True:
        schedule.run_pending()
        time.sleep(1)


def start_scheduler(graph_id):
    thread = threading.Thread(target=run_scheduler, args=(graph_id,))
    thread.start()
