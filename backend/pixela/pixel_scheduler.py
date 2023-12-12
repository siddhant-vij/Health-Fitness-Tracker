import schedule
import threading
import time
from datetime import datetime
from backend.constants import USER_DB_FILE
from backend.pixela.graph_pixels import manage_pixel_entry
from database.csv_manager import CSVManager


def calculate_reduction(user):
    bmr = float(user.get('bmr'))
    activity_level = float(user.get('activity_multiplier'))
    daily_rest_burn = bmr * activity_level
    return daily_rest_burn / (24 * 60)


def update_daily_pixel(username, graph_id):
    users = CSVManager(USER_DB_FILE).read_data()
    user = next((u for u in users if u['username'] == username), None)
    if not user:
        print(f"User '{username}' not found.")
        return

    reduction_value = calculate_reduction(user)
    date = datetime.now().strftime("%Y%m%d")
    reduction_value = int(reduction_value)
    manage_pixel_entry(username, graph_id, -1 * reduction_value, date)


def run_scheduler(username, graph_id):
    schedule.every(60).seconds.do(update_daily_pixel, username, graph_id)
    while True:
        schedule.run_pending()
        time.sleep(60)


def start_pixel_scheduler(username, graph_id):
    thread = threading.Thread(target=run_scheduler, args=(username, graph_id))
    thread.start()
