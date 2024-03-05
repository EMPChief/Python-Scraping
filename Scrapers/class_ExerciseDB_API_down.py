import json
import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()


class ExerciseDownloader:
    def __init__(self, api_key):
        self.url = "https://exercisedb.p.rapidapi.com/exercises"
        self.querystring = {"limit": "2000"}
        self.headers = {
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
        }

    def download_exercises(self):
        try:
            response = requests.get(
                self.url, headers=self.headers, params=self.querystring)
            if response.status_code == 200:
                data = response.json()
                if not os.path.exists('gif'):
                    os.makedirs('gif')

                existing_exercises = []
                if os.path.exists('exercises_with_gifs.json'):
                    with open('exercises_with_gifs.json', 'r') as f:
                        existing_exercises = json.load(f)

                exercises_with_gifs = []

                for index, exercise in enumerate(data):
                    gif_url = exercise.get('gifUrl')
                    if gif_url:
                        exercise_exists = any(
                            ex['name'] == exercise['name'] and
                            ex['instructions'] == exercise['instructions'] and
                            ex['bodyPart'] == exercise['bodyPart']
                            for ex in existing_exercises
                        )

                        if exercise_exists:
                            print(f"Skipping: {
                                  exercise['name']} - Exercise already exists")
                        else:
                            filename = f"gif/{exercise['id']}.gif"
                            gif_response = requests.get(gif_url)
                            if gif_response.status_code == 200:
                                with open(filename, 'wb') as f:
                                    f.write(gif_response.content)
                                print(f"Downloaded: {exercise['name']}")

                                exercise_with_gif = {
                                    'name': exercise['name'],
                                    'bodyPart': exercise['bodyPart'],
                                    'equipment': exercise['equipment'],
                                    'target': exercise['target'],
                                    'secondaryMuscles': exercise['secondaryMuscles'],
                                    'instructions': exercise['instructions'],
                                    'gifPath': filename
                                }
                                exercises_with_gifs.append(exercise_with_gif)
                            else:
                                print(f"Failed to download GIF for exercise: {
                                      exercise['name']}")

                            if index < len(data) - 1:
                                print("Waiting 3 seconds before next download...")
                                time.sleep(3)

                existing_exercises.extend(exercises_with_gifs)

                with open('exercises_with_gifs.json', 'w') as f:
                    json.dump(existing_exercises, f, indent=4)

                print(
                    "Data with GIF links and local paths saved to exercises_with_gifs.json")
            else:
                print("Failed to fetch data from the API")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


# Usage
api_key = os.getenv('api_key_rapid_exercise')
exercise_downloader = ExerciseDownloader(api_key)
exercise_downloader.download_exercises()
