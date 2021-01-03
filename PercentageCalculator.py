import re


dictionary = {}

NumOfItems= int(input("How many items do you have?: "))


for i in range(NumOfItems):
    item = input("please input the name of your item: ")
    value = input("please input the value of your item: ")
    while not re.match(r'^([\s\d]+)$', value):
        print("value is not valid format, please use integers")
        value = input("please input the value of your item: ")

    dictionary[item] = value



Total_amount = 0

for i in dictionary:
    Total_amount += int(dictionary[i])

print("\n\n\nThe percentage of each item is: ")

for i in dictionary:
    print(f"{i} = {round(int(dictionary[i])/Total_amount*100)}%")

input("\n\n\nPress enter to exit")