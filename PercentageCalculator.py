import re
import save_meal

save = save_meal.SaveMeal()
dictionary = {}

def new_meal():
    load_meal_choice = input("Do you want to load a meal? (Y/N)\n")

    if load_meal_choice.lower() == "y":
        save.show_meals()
        load_meal_number = int(input("which meal number would you like?\n"))
        loaded_meal = save.load_meal(load_meal_number)
        print(loaded_meal)
        dictionary=loaded_meal

    else:
        NumOfItems = int(input("How many items do you have?: "))

        for i in range(NumOfItems):
            item = input("please input item NAME: ")
            value = input("please input the VALUE of your item: ")
            while not re.match(r'^([\s\d]+)$', value):
                print("value is not valid format, please use integers")
                value = input("please input the value of your item: ")

            dictionary[item] = value


def percentages(dictionary):
    total_amount = 0

    for i in dictionary:
        total_amount += int(dictionary[i])

    print("\n\n\nThe percentage of each item is: ")

    for i in dictionary:
        print(f"{i} = {round(int(dictionary[i]) / total_amount * 100)}%")

    num = int(input("\n\n\nEnter total food eaten:"))

    while type(num) != int:
        print("That is not a valid integer value, please enter an integer value")
        num = input("\n\n\nEnter total food eaten:")

    for i in dictionary:
        print(f"{i} = {round(int(dictionary[i]) / total_amount * int(num))}")

    print("*"*50 + "\n")

new_meal()
percentages(dictionary)

def replay_or_save():
    replay = input("do you want to do another quantity of this meal (Y/N)?" + "\n")

    while replay.lower() == "y":
        percentages(dictionary)
        replay = input("do you want to do another quantity of this meal (Y/N)?" + "\n")

    save.choose()
    2
    if save.choice == "y":
        save.save_meal(foods=dictionary)

    input("\nPress enter to exit")