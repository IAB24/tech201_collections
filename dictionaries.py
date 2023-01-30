# Dictionaries

# Dictionaries use key/value pairs

# key = a reference to a particular object
# value = data storage mechanism you want to use

# Create a dictionary

student_1 = {
    "name": "Susan",
    "stream": "DevOps",
    "completed lessons": ["variables", "data_types", "set-up"]
}
# Access data within a dictionary

print(student_1["stream"]) # DevOps

# how to access particular parts of dictionary

print(student_1["completed_lesson_names"][2])

# Changing a value in a dictionary

student_1["completed lessons"] = 3
print(student_1["completed lessons"])

# Removing items from a dictionary
student_1["completed lessons"].remove("data_types")
print(student_1.get("name"))

# get the values of a dictionary
print(student_1.items())

print(student_1.items())

# outputs array of tuples with key values
print(student_1.items())