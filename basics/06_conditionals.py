# Conditional Statements 

age = 18

if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You just became an adult!")
else:
    print("You are an adult.")

# Checking even or odd number
number = 7

if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# Nested condition
marks = 85

if marks >= 90:
    print("Grade A")
elif 80 <= marks < 90:
    print("Grade B")
elif 70 <= marks < 80:
    print("Grade C")
else:
    print("Grade D")
