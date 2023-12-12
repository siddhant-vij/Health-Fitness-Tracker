# Health & Fitness Tracker

Python-based backend designed to help users monitor and analyze their nutrition and workout routines. Utilizing natural language processing through Nutritionix's APIs, it simplifies the logging of meals and exercises. This app makes health tracking accessible to everyone.

## Table of Contents
1. [Features](#features)
1. [Installation](#installation)
1. [Usage](#usage)
1. [Contributions](#contributions)
1. [Future Improvements](#future-improvements)
1. [License](#license)

## Features
- **Natural Language Meal and Exercise Logging**: Log meals and exercises using natural language, processed through the Nutritionix API for detailed nutritional info and calories burned.
- **Habit Tracking and Visualization**: Track and visualize health and fitness habits using Pixela, enhanced with custom Python visualizations for in-depth data analysis.
- **Speech Recognition**: Audio input capabilities for hands-free data logging.
- **User Authentication**: Securely manage user data and personal health records.
- **CSV-Based Data Management**: Organized and efficient storage of user, nutrition, and workout data.
- **Email Notifications**: Get reminders and alerts to maintain consistent health tracking.

## Installation
- Clone the repository: `git clone https://github.com/siddhant-vij/Health-Fitness-Tracker.git`
- Navigate to the project directory: `cd Health-Fitness-Tracker`
- Install dependencies: `conda create --name fitness --file requirements.txt`
- Activate the environment: `conda activate fitness`
- Create a `.env` file in the project root directory based on the `.env.example` template.
- Run the local tests in the application: `python main.py`

## Usage
After launching the application, create an account or log in. Begin by logging your meals and exercises using simple, natural language. Explore the various visualizations and insights generated based on your data.

## Contributions
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.
1. **Fork the Project**
1. **Create your Feature Branch**: 
    ```bash
    git checkout -b feature/AmazingFeature
    ```
1. **Commit your Changes**: 
    ```bash
    git commit -m 'Add some AmazingFeature'
    ```
1. **Push to the Branch**: 
    ```bash
    git push origin feature/AmazingFeature
    ```
1. **Open a Pull Request**

## Future Improvements
- **Tkinter GUI**: Interactive and straightforward graphical interface.
- **Meal Planner**: Integrate a meal planning feature with recipes and grocery lists based on nutritional goals - refer & use a 3rd party API.
- **Mobile Application**: Develop a mobile version for convenient on-the-go access.
- **Advanced Analytics**: Use machine learning to provide personalized health insights and recommendations.
- **Integration with Fitness Devices**: Sync data from fitness trackers for automated exercise logging.
- **Community Features**: Implement social sharing, challenges, and leaderboards to encourage user engagement.

## License
Distributed under the MIT License. See [`LICENSE`](https://github.com/siddhant-vij/Health-Fitness-Tracker/blob/main/LICENSE) for more information.