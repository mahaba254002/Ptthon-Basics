# List
# Used to store multiple items in a single variable
# Indexed, Allow duplicates, Changeable
list1 = ["banana", "orange"]
print(list1)
print(type(list1))  # 'list'

"""
List Methods
append() - add an item at the end
extend() - extend the list by appending all the items from the iterable
insert() - insert an element at a specified index
remove() - remove an element
pop() - remove an element at a specified index
clear() - remove all elements
count() - return the number of items
reverse() - reverse elements in the list
"""

fruits = ["orange", "apple", "pear", "banana"]
print(fruits.count("apple"))  # Output: 1
print(fruits.index("banana"))  # Output: 3
print(fruits.index("banana", 1))  # Output: 3

rev_fruits=list(reversed(fruits))
print(rev_fruits) 

cars = ["Ford", "BMW", "Volvo"]
rev_fruits.extend(cars)
print(rev_fruits) 

x=list("67")
print(x)

