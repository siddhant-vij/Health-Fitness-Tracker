import secrets


def generate_token():
    return secrets.token_urlsafe(24)


def calculate_bmr(age, weight, height, gender):
    if gender.lower() == 'male':
        bmr = 9.99 * weight + 6.25 * height - 4.92 * age + 5
    else:  # female
        bmr = 9.99 * weight + 6.25 * height - 4.92 * age - 161
    return bmr


def get_activity_multiplier(activity_level):
    activity_levels = {
        "sedentary": 1.2,
        "lightly active": 1.375,
        "moderately active": 1.55,
        "very active": 1.725,
        "extra active": 1.9
    }
    return activity_levels.get(activity_level.lower(), 1.2)
