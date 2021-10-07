print("Made by Pd\nWelcome to the Python-lists")
my_list = input("Enter the numbers you want to add in this list :").split()

length_of_my_list = len(my_list)
print(f"Length of list :{length_of_my_list}\n")

my_list.insert(length_of_my_list, "666")
print(f"Insert 666 to the end of list: {my_list}\n")

my_list.remove("666")
print(f"Remove 666 from list: {my_list}\n")

my_list.append("0")
print(f"Append 0 to the end of list: {my_list}\n")

my_list.sort()
print(f"Sorted list : {my_list}\n")

length_of_my_list = len(my_list) - 1
my_pop = my_list.pop(length_of_my_list)
print(f"Pop the last element ({my_pop}) from list: {my_list}\n")

my_list.reverse()
print(f"Reversed list : {my_list}\n")

quit_app = input("Hope to see you again :)\nEnter anything to exit :")
