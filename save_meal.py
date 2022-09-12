import glob
import json
import os
from datetime import datetime


class SaveMeal:

    def __init__(self):
        self.choice = "n"
        self.foods = {}
        self.meal_indexes = {}

    def choose(self):
        save_choice = input("do you want to save this meal (Y/N)" + "\n")
        self.choice = save_choice.lower()

    def save_meal(self, foods):
        meal_name = input("what is the meal name:" + "\n")
        print("SAVED")
        with open(f'{meal_name}({datetime.today().date()}).txt', 'w') as file:
            file.write(json.dumps(foods))

    def show_meals(self):
        #os.chdir("/mydir")
        indexes = {}
        for index, file in enumerate(sorted(glob.glob("*.txt"), key=os.path.getmtime, reverse=True)):
            print(f"{index+1}-{file}")
            indexes[index+1]=file
        self.meal_indexes = indexes

    def load_meal(self, meal_number):
        print(f"Loading meal: {self.meal_indexes[meal_number]}")
        with open(f'{self.meal_indexes[meal_number]}', 'r') as file:
            return json.load(file)




if __name__ == "__main__":
    pass