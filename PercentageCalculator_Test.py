import re


dictionary = {}

NumOfItems= int(input("How many items do you have?: "))


for i in range(NumOfItems):
    item = input("please input item NAME: ")
    value = input("please input the VALUE of your item: ")
    while not re.match(r'^([\s\d]+)$', value):
        print("value is not valid format, please use integers")
        value = input("please input the value of your item: ")

    dictionary[item] = value



def percentages(dictionary):
    Total_amount = 0

    for i in dictionary:
        Total_amount += int(dictionary[i])

    print("\n\n\nThe percentage of each item is: ")



    for i in dictionary:
        print(f"{i} = {round(int(dictionary[i])/Total_amount*100)}%")




    num = input("\n\n\nEnter total food eaten:")

    for i in dictionary:
        print(f"{i} = {round(int(dictionary[i]) / Total_amount * int(num))}")



    input("\n\n\nPress enter to exit")

percentages(dictionary)


