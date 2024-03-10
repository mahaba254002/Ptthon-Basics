# Unordered collection of key value pair

dict = {"Name": "Bakari", "Age": 77, "Origin": "Canada"}
print(dict)  # {'Name': 'Bakari', 'Age': 77, 'Origin': 'Canada'}
print(dict["Name"])  # Bakari


my_dict = {"name": "John", "age": 30,"Marital Status":"Single"}
my_dict["country"] = "USA"  # Adding a new key-value pair
my_dict["age"] = 31  # Modifying the value of an existing key
del my_dict["age"]  # Removes
keys = my_dict.keys()  # Get all keys
values = my_dict.values()  # Get all values

for key, value in my_dict.items():
    print(key, value)