import threading
import schedule
import time
from datetime import datetime, timedelta
from backend.constants import USER_DB_FILE
from .email_manager import send_email
from database.csv_manager import CSVManager


def send_reminder(subject, message):
    users = CSVManager(USER_DB_FILE).read_data()
    for user in users:
        send_email(user['email'], subject, message)


def reminder_scheduler():
    # Schedule for meal reminders
    schedule.every().day.at("08:00").do(send_reminder, "Breakfast Time",
                                        "Don't forget to log your breakfast!")
    schedule.every().day.at("13:00").do(
        send_reminder, "Lunch Time", "Time to log your lunch!")
    schedule.every().day.at("16:00").do(
        send_reminder, "Snack Time", "Remember to log your snacks!")
    schedule.every().day.at("22:00").do(
        send_reminder, "Dinner Time", "Don't forget to log your dinner!")

    # Alternate day scheduling for exercise reminder
    exercise_day = datetime.now()
    while True:
        if datetime.now() >= exercise_day:
            schedule.every().day.at("18:00").do(
                send_reminder, "Exercise Time", "Time for your exercise session!")
            exercise_day += timedelta(days=2)
        schedule.run_pending()
        time.sleep(60)


def start_reminder_scheduler():
    thread = threading.Thread(target=reminder_scheduler)
    thread.start()
