import pandas as pd
import matplotlib.pyplot as plt
from backend.constants import NUTRITION_DB_FILE, EXERCISE_DB_FILE
from database.csv_manager import CSVManager


def plot_calories_consumed(username):
    data = CSVManager(NUTRITION_DB_FILE).read_data()
    df = pd.DataFrame(data)
    df = df[df['username'] == username]
    df['time_of_consumption'] = pd.to_datetime(
        df['time_of_consumption']).dt.date
    df['total_calories'] = pd.to_numeric(df['total_calories'])

    daily_calories = df.groupby('time_of_consumption')['total_calories'].sum()
    daily_calories.plot(kind='line', marker='o', color='blue')
    plt.title('Total Calories Consumed Over Time')
    plt.xlabel('Date')
    plt.ylabel('Calories')
    plt.grid(True)
    plt.show()


def plot_calories_burned(username):
    data = CSVManager(EXERCISE_DB_FILE).read_data()
    df = pd.DataFrame(data)
    df = df[df['username'] == username]
    df['time_of_exercise'] = pd.to_datetime(df['time_of_exercise']).dt.date
    df['total_calories'] = pd.to_numeric(df['total_calories'])

    daily_calories = df.groupby('time_of_exercise')['total_calories'].sum()
    daily_calories.plot(kind='line', marker='o', color='green')
    plt.title('Total Calories Burned Over Time')
    plt.xlabel('Date')
    plt.ylabel('Calories')
    plt.grid(True)
    plt.show()


def plot_calories_comparison(username):
    # Process nutrition data
    nutrition_data = CSVManager(NUTRITION_DB_FILE).read_data()
    nutrition_df = pd.DataFrame(nutrition_data)
    nutrition_df = nutrition_df[nutrition_df['username'] == username]
    nutrition_df['time_of_consumption'] = pd.to_datetime(
        nutrition_df['time_of_consumption']).dt.date
    nutrition_df['total_calories'] = pd.to_numeric(
        nutrition_df['total_calories'])
    daily_nutrition_calories = nutrition_df.groupby('time_of_consumption')[
        'total_calories'].sum()

    # Process exercise data
    exercise_data = CSVManager(EXERCISE_DB_FILE).read_data()
    exercise_df = pd.DataFrame(exercise_data)
    exercise_df = exercise_df[exercise_df['username'] == username]
    exercise_df['time_of_exercise'] = pd.to_datetime(
        exercise_df['time_of_exercise']).dt.date
    exercise_df['total_calories'] = pd.to_numeric(
        exercise_df['total_calories'])
    daily_exercise_calories = exercise_df.groupby(
        'time_of_exercise')['total_calories'].sum()

    # Merge data
    combined_df = pd.merge(daily_nutrition_calories, daily_exercise_calories,
                           left_index=True, right_index=True, how='outer').fillna(0)
    combined_df.columns = ['Calories Consumed', 'Calories Burned']

    # Plotting
    combined_df.plot(kind='line', marker='o')
    plt.title('Comparison of Calories Consumed vs. Calories Burned')
    plt.xlabel('Date')
    plt.ylabel('Calories')
    plt.grid(True)
    plt.show()


def plot_macronutrient_breakdown(username):
    data = CSVManager(NUTRITION_DB_FILE).read_data()
    df = pd.DataFrame(data)
    df = df[df['username'] == username]
    df['time_of_consumption'] = pd.to_datetime(
        df['time_of_consumption']).dt.date
    df[['total_carbs', 'total_protein', 'total_fats']] = df[[
        'total_carbs', 'total_protein', 'total_fats']].apply(pd.to_numeric)

    daily_nutrients = df.groupby('time_of_consumption')[
        ['total_carbs', 'total_protein', 'total_fats']].sum()
    daily_nutrients.plot(kind='bar', stacked=True)
    plt.title('Macronutrient Breakdown Over Time')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.show()
