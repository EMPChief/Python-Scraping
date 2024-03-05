import json
import os
import random
import string


class GifRenamer:
    def __init__(self, filepath_js="exercises_with_gifs.json", folderpath_gif="gif/"):
        self.filepath_js = filepath_js
        self.folderpath_gif = folderpath_gif
        self.data = []

    def load_data(self):
        with open(self.filepath_js, "r") as f:
            self.data = json.load(f)

    def save_data(self):
        with open(self.filepath_js, "w") as f:
            json.dump(self.data, f, indent=4)

    def rename_gifs(self):
        for exercise in self.data:
            old_filename = exercise["gifPath"].split("/")[-1]
            exercise_name = exercise["name"]

            random_numbers = ''.join(random.choices(string.digits, k=4))

            new_filename = f"{exercise_name.replace(' ', '_')}_{
                random_numbers}.gif"

            old_filepath = os.path.join(self.folderpath_gif, old_filename)
            new_filepath = os.path.join(self.folderpath_gif, new_filename)

            if os.path.exists(old_filepath):
                try:
                    os.rename(old_filepath, new_filepath)
                    exercise["gifPath"] = f"gif/{new_filename}"
                except Exception as e:
                    pass

        self.save_data()


gif_renamer = GifRenamer()
gif_renamer.load_data()
gif_renamer.rename_gifs()
