

'''
Some of the code can be found here:
https://github.com/tecladocode/python-refresher

new_list = [1, 2, 3, 4, 4.6, 4, "strings"]  # - list are ordered, mutable - can be changed
new_tuples = (1, 2, 3, 4, 4.6, 4, "strings")  # - tuples are ordered, immutable - they cannot be changed
new_sets = {92, 2, 35, 4, 4.6, 4, "strings"}  # - sets are random, mutable - they can be changed



new_list = [1, 2, 3, 4, 4.6, 4, "strings"]  # - list are ordered, mutable - can be changed
new_tuples = (1, 2, 3, 4, 4.6, 4, "strings")  # - tuples are ordered, immutable - they cannot be changed
new_sets = {92, 2, 35, 4, 4.6, 4, "strings"}  # - sets are randomly ordered, mutable - they can be changed

print(new_list)
print(new_tuples)
print(new_sets)
'''

#Modify the code so that the evens list contains only the even numbers of the numbers list. 
#You do not need to print anything.
'''
# -- Part 1 --
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# this is there, i miss read it and thought it would be more complex.
evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)

for even in evens:
    print(even)
'''

user_input = input("Enter your choice: ")
if user_input == "a":
    print("Add")
elif user_input == "q":
    print("Quit")







