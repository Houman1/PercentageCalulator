import json

class Save_meal:

    def __init__(self):
        self.choice = "n"
        self.foods = {}




    def choose(self):
        save_choice = input("do you want to save this meal (Y/N)" + "\n")
        self.choice = save_choice.lower()

    def save_meal(self, foods):

        print("SAVED")
        # with open('file.txt', 'w') as file:
        #     file.write(json.dumps(foods))
