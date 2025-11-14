# Python Strings Example

text = "Hello Yeshwanth, welcome to Python!"

# Printing the string
print("Text:", text)

# Accessing characters
print("First character:", text[0])
print("Last character:", text[-1])

# String slicing
print("First 5 letters:", text[:5])
print("From index 6 to 15:", text[6:16])

# String length
print("Length of text:", len(text))

# Changing case
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

# Replacing words
print("Replace Python:", text.replace("Python", "AI"))

# Splitting string
words = text.split(" ")
print("Split into words:", words)

# String concatenation
greet = "Hello"
name = "Yash"
message = greet + " " + name
print("Concatenated string:", message)
