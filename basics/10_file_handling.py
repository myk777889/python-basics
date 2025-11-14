# File Handling in Python

# Writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, this is a sample file.\n")
    file.write("Python file handling is easy!")

print("File created and written successfully.")

# Reading from a file
with open("sample.txt", "r") as file:
    content = file.read()
    print("\nFile content:")
    print(content)

# Appending to a file
with open("sample.txt", "a") as file:
    file.write("\nThis line is appended.")

print("\nNew line appended successfully.")

# Reading again
with open("sample.txt", "r") as file:
    updated_content = file.read()
    print("\nUpdated content:")
    print(updated_content)
