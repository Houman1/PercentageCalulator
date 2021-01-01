
dictionary = {}

NumOfItems= int(input("How many items do you have?: "))


for i in range(NumOfItems):
    item = input("please input the name of your item: ")
    value = input("please input the value of your item: ")
    dictionary[item] = value




Total_amount = 0

for i in dictionary:
    Total_amount += int(dictionary[i])

print("\nThe percentage of each item is: ")

for i in dictionary:
    print(f"{i} = {round(int(dictionary[i])/Total_amount*100)}%")