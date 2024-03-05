import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


class ExerciseFetcher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.api-ninjas.com/v1/exercises"
        self.muscles = [
            "abdominals",
            "abductors",
            "adductors",
            "biceps",
            "calves",
            "chest",
            "forearms",
            "glutes",
            "hamstrings",
            "lats",
            "lower_back",
            "middle_back",
            "neck",
            "quadriceps",
            "traps",
            "triceps"
        ]
        self.all_exercises = []

    def fetch_exercises(self):
        for muscle in self.muscles:
            url = f"{self.base_url}?muscle={muscle}"
            response = requests.get(url, headers={"X-Api-Key": self.api_key})

            if response.status_code == 200:
                exercises = response.json()
                self.all_exercises.extend(exercises)
                print(f"Exercises for {muscle} fetched successfully.")
            else:
                print(f"Failed to fetch exercises for {
                      muscle}. Status Code: {response.status_code}")

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            json.dump(self.all_exercises, f, indent=4)
        print(f"All exercises saved to {filename}")


api_key = os.getenv("NINJA_API_KEY")
if api_key:
    exercise_fetcher = ExerciseFetcher(api_key)
    exercise_fetcher.fetch_exercises()
    exercise_fetcher.save_to_file("ninja_exercises.json")
else:
    print("API key not found. Please set your API key.")
