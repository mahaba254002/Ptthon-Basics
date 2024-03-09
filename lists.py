# List
# Used to store multible items in a single variable
# Indexed,Allow duplicates,Changeable
list1 = ["banana,orange"]
print(list1)
print(type(list1))  # 'list'
"""
l
List Methods
append() add item at the end
extend() Extend the list by appending all the items from the iterable.
insert() insert element at specified index
remove() removes element
pop() removes element at specified index
clear() removes all elements
count() return the number of items
reverse() reverse elemnts in the list
"""

fruits = ["orange", "apple", "pear", "banana"]
print(fruits.count("apple"))  # 1
print(fruits.index("banana"))  # 3
print(fruits.index("banana", 3))
fruits.reverse() # ["banana", "pear", "apple", "orange"]
print(fruits)
print(fruits.append("grape"))
z=fruits.sort()
print(z)
fruits.pop()
cars = ["Ford", "BMW", "Volvo"]

fruits.extend(cars)
print(fruits)
