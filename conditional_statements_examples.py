"""
Program: Conditional Statements and Checks
Description:
    This script contains several Python programs demonstrating:
    1. Checking if a number is positive, negative, or zero
    2. Shorthand if/else statements
    3. Checking if a number is even or odd
    4. Area calculator for different shapes
    5. Checking vowels and consonants
    6. Checking number of digits (1 to 5 digits)
"""

# ---------------------------------------------------------
# 1. Check if a number is positive, negative, or zero
# ---------------------------------------------------------

num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num == 0:
    print("The number is zero.")
else:
    print("The number is negative.")
print()

# Shorthand if
num1 = float(input("Enter a number: "))
if num1 > 0: 
    print("The number is positive.")
print()

# Shorthand if-else
num2 = float(input("Enter a number: "))
print("The number is positive.") if num2 > 0 else print("The number is negative.")
print()

# ---------------------------------------------------------
# 2. Check if a number is even or odd
# ---------------------------------------------------------

num3 = int(input("Enter a number: "))

# Shorthand if-else
print("The number is even.") if num3 % 2 == 0 else print("The number is odd.")

# Normal if-else
if num3 % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
print()

# ---------------------------------------------------------
# 3. Area Calculator
# ---------------------------------------------------------

print("Area Calculator")
print("""This program calculates the area of different shapes.
1. Square
2. Triangle
3. Rectangle
4. Circle
""")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    side = float(input("Enter the side length of the square: "))
    area = side ** 2
    print(f"The area of the square is: {area}")
elif choice == 2:
    base = float(input("Enter the base length of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is: {area}")
elif choice == 3:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle is: {area}")
elif choice == 4:
    radius = float(input("Enter the radius of the circle: "))
    area = 3.14159 * radius ** 2
    print(f"The area of the circle is: {area}")
else:
    print("Invalid choice. Please select a valid option.")
print()

# Area calculator using a function
def calculate_area(shape, dimensions):
    """Function to calculate area based on shape choice."""
    if shape == 1:  # Square
        side = dimensions[0]
        return side ** 2
    elif shape == 2:  # Triangle
        base, height = dimensions
        return 0.5 * base * height
    elif shape == 3:  # Rectangle
        length, width = dimensions
        return length * width
    elif shape == 4:  # Circle
        radius = dimensions[0]
        return 3.14159 * radius ** 2
    else:
        return None

print(f"The area (example with circle radius=2) is: {calculate_area(4, [2])}\n")

# ---------------------------------------------------------
# 4. Check if a letter is vowel or consonant
# ---------------------------------------------------------

letter = input("Enter a letter: ")
vowels = "aeiouAEIOU"

# Using function
def check_vowel_consonant(letter):
    return "Vowel" if letter in vowels else "Consonant"

print(f"The letter '{letter}' is a {check_vowel_consonant(letter)}.\n")

# Using class
class VowelConsonantChecker:
    """Class to check if a letter is vowel or consonant."""

    def __init__(self, letter):
        self.letter = letter

    def check(self):
        return "Vowel" if self.letter in vowels else "Consonant"

checker = VowelConsonantChecker(letter)
print(f"The letter '{letter}' is a {checker.check()}.\n")

# ---------------------------------------------------------
# 5. Check number of digits (1 to 5 digits)
# ---------------------------------------------------------

def check_number_digits(number):
    """Function to check the number of digits (up to 5)."""
    if 0 <= number < 10:
        return "Single digit"
    elif 10 <= number < 100:
        return "Double digit"
    elif 100 <= number < 1000:
        return "Triple digit"
    elif 1000 <= number < 10000:
        return "Four digit"
    elif 10000 <= number < 100000:
        return "Five digit"
    else:
        return "Out of range"

num = int(input("Enter a number: "))
print(f"The number {num} is a {check_number_digits(num)}.\n")

# Without function
if 0 <= num < 10:
    print(f"The number {num} is a Single digit.")
elif 10 <= num < 100:
    print(f"The number {num} is a Double digit.")
elif 100 <= num < 1000:
    print(f"The number {num} is a Triple digit.")
elif 1000 <= num < 10000:
    print(f"The number {num} is a Four digit.")
elif 10000 <= num < 100000:
    print(f"The number {num} is a Five digit.")
else:
    print(f"The number {num} is Out of range.")
print()

# Using class
class NumberDigitChecker:
    """Class to check number of digits."""

    def __init__(self, number):
        self.number = number

    def check(self):
        if 0 <= self.number < 10:
            return "Single digit"
        elif 10 <= self.number < 100:
            return "Double digit"
        elif 100 <= self.number < 1000:
            return "Triple digit"
        elif 1000 <= self.number < 10000:
            return "Four digit"
        elif 10000 <= self.number < 100000:
            return "Five digit"
        else:
            return "Out of range"

checker = NumberDigitChecker(num)
print(f"The number {num} is a {checker.check()}.\n")
