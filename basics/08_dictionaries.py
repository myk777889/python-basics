# Python Dictionaries Example

# Creating a dictionary
student = {
    "name": "Yeshwanth",
    "age": 20,
    "course": "AIML",
    "cgpa": 8.7
}

print("Student Dictionary:", student)

# Accessing values
print("Name:", student["name"])
print("Age:", student["age"])

# Adding a new key-value pair
student["city"] = "Hyderabad"
print("After adding city:", student)

# Updating a value
student["cgpa"] = 9.1
print("After CGPA update:", student)

# Removing a key-value pair
del student["age"]
print("After removing age:", student)

# Looping through dictionary keys and values
print("\nLooping through dictionary:")
for key, value in student.items():
    print(key, ":", value)
