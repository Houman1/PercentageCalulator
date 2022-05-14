import re

dictionary = {}


def new_meal():
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

    print( "*"*100 + "\n\n\n")

new_meal()
percentages(dictionary)

replay = input("do you want to do another quantity of this meal (Y/N)"+ "\n\n\n")

while replay.lower() == "y":
    percentages(dictionary)
    replay = input("do you want to do another quantity of this meal (Y/N)"+ "\n\n\n")

input("\n\n\nPress enter to exit")