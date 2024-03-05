import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


class CaloriesBurnedFetcher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.api-ninjas.com/v1/caloriesburnedactivities"
        self.activities = [
            "skiing",
            "running",
            "swimming",
            "cycling",
            "walking",
            "weight_lifting",
            "yoga",
            "basketball",
            "football",
            "soccer",
            "tennis"
        ]
        self.calories_data = {}

    def fetch_all_calories_data(self):
        for activity in self.activities:
            url = f"{self.base_url}"
            response = requests.get(url, headers={"X-Api-Key": self.api_key})

            if response.status_code == 200:
                data = response.json()
                self.calories_data[activity] = data
                print(f"Calories burned data for {
                      activity} fetched successfully.")
            else:
                print(f"Failed to fetch calories burned data for {
                      activity}. Status Code: {response.status_code}")

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            json.dump(self.calories_data, f, indent=4)
        print(f"All calories burned data saved to {filename}")


# Usage
api_key = os.getenv("NINJA_API_KEY")
if api_key:
    calories_burned_fetcher = CaloriesBurnedFetcher(api_key)
    calories_burned_fetcher.fetch_all_calories_data()
    calories_burned_fetcher.save_to_file("calories_burned_data_2.json")
else:
    print("API key not found. Please set your API key.")
