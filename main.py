from backend.authentication.login_user import login_user
from backend.authentication.register_user import register_user
from backend.authentication.update_user import update_user
from backend.email_alerts.reminder_scheduler import start_reminder_scheduler
from backend.nutritionix.exercise_api import get_exercise_info
from backend.nutritionix.nutrition_api import get_nutritional_info
from backend.pixela.graph_pixels import manage_pixel_entry
from backend.pixela.pixel_scheduler import start_pixel_scheduler
from backend.speech_recognition.speech_input import get_speech_input


# Create User & Graph Example Usage
# user_info = register_user("health-fitness-235", "siddhantvij201@gmail.com", "weight-gain", 30, "male", 170, 70, "sedentary")
# print(user_info)
# Confirm at https://pixe.la/v1/users/health-fitness-235/graphs/weight-gain.html

# Nutrition Example Usage
# food_info = get_nutritional_info("1 apple", "health-fitness-235", "weight-gain")
# print(food_info)
# food_info = get_nutritional_info("3 large eggs", "health-fitness-235", "weight-gain")
# print(food_info)
# food_info = get_nutritional_info("1 small egg", "health-fitness-235", "weight-gain")
# print(food_info)

# Exercise Example Usage
# exercise_info = get_exercise_info("swam for 1 hour", "health-fitness-235", "weight-gain")
# print(exercise_info)
# exercise_info = get_exercise_info("cardio for 1.5 hour", "health-fitness-235", "weight-gain")
# print(exercise_info)
# exercise_info = get_exercise_info("weight-lifting for 1 hour", "health-fitness-235", "weight-gain")
# print(exercise_info)

# Integrating Both APIs Example Usage
# food_info = get_nutritional_info("1 cup mashed potatoes and 2 tbsp gravy", "health-fitness-235", "weight-gain")
# print(food_info)
# exercise_info = get_exercise_info("30 minutes of yoga and 45-minutes weightlifting", "health-fitness-235", "weight-gain")
# print(exercise_info)

# Update User Example Usage
# user_info = update_user("health-fitness-235", 30, "male", 170, 80, "lightly active")
# print(user_info)

# Pixel Scheduler Example Usage
# start_pixel_scheduler("health-fitness-235", "weight-gain")

# Speech Input Example Usage
# spoken_food_input = get_speech_input()  # User speaks about their meal
# if spoken_food_input:
#     get_nutritional_info(spoken_food_input, "health-fitness-235", "weight-gain")

# spoken_exercise_input = get_speech_input()  # User speaks about their exercise
# if spoken_exercise_input:
#     get_exercise_info(spoken_exercise_input, "health-fitness-235", "weight-gain")

# Email Remainder Scheduler Example Usage
# start_reminder_scheduler()
