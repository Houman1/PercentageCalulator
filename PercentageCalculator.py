import re
import save_meal


class PercentageCalculator:

    def __init__(self):
        self.save = save_meal.SaveMeal()
        self.dictionary = {}
        self.load_meal_choice = "n"

    def new_meal(self):
        load_meal_choice = input("Do you want to load a meal? (Y/N)\n")
        self.load_meal_choice = load_meal_choice

        if load_meal_choice.lower() == "y":
            self.save.show_meals()
            load_meal_number = int(input("which meal number would you like?\n"))
            loaded_meal = self.save.load_meal(load_meal_number)
            print(loaded_meal)
            self.dictionary = loaded_meal

        else:
            NumOfItems = int(input("How many items do you have?: "))

            for i in range(NumOfItems):
                item = input("please input item NAME: ")
                value = input("please input the VALUE of your item: ")
                while not re.match(r'^([\s\d]+)$', value):
                    print("value is not valid format, please use integers")
                    value = input("please input the value of your item: ")

                self.dictionary[item] = value

    def percentages(self):
        total_amount = 0

        for i in self.dictionary:
            total_amount += int(self.dictionary[i])

        print("\n\n\nThe percentage of each item is: ")

        for i in self.dictionary:
            print(f"{i} = {round(int(self.dictionary[i]) / total_amount * 100)}%")

        num = int(input("\n\n\nEnter total food eaten:"))

        while type(num) != int:
            print("That is not a valid integer value, please enter an integer value")
            num = input("\n\n\nEnter total food eaten:")

        for i in self.dictionary:
            print(f"{i} = {round(int(self.dictionary[i]) / total_amount * int(num))}")

        print("*" * 50 + "\n")

    def replay_or_save(self):
        replay = input("do you want to do another quantity of this meal (Y/N)?" + "\n")

        while replay.lower() == "y":
            self.percentages()
            replay = input("do you want to do another quantity of this meal (Y/N)?" + "\n")

        if self.load_meal_choice == "n":
            self.save.choose()

            if self.save.choice == "y":
                self.save.save_meal(foods=self.dictionary)

        input("\nPress enter to exit")
