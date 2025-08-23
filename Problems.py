"""
Program: Basic Python Exercises
Description:
    This script demonstrates different small Python programs:
    1. Displaying personal information
    2. Swapping two variables
    3. Converting float to integer
    4. Displaying student ID card details
    5. Converting integer to float (and vice versa)
"""

# ---------------------------------------------------------
# 1. Display a person’s name, age, and address in 3 ways
# ---------------------------------------------------------

print("One way to display information:")
print("Name: John Doe")
print("Age: 30")
print("Address: 123 Main St, Anytown, USA\n")

print("Second way to display information:")
print("Name: Aqdas \nAge: 22 \nAddress: 123 Main St, Anytown, USA\n")

print("Third way to display information (using a class):")


class Person:
    """Class to represent a person."""

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_info(self):
        """Method to display person’s details."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")


# Create a Person object and display details
person = Person("Ali Hassan", 28, "123 Main St, Anytown, USA")
person.display_info()
print()


# ---------------------------------------------------------
# 2. Swap two variables
# ---------------------------------------------------------

print("First way to swap two variables (using temporary variable):")
a = 5
b = 10
print("Before swapping: a =", a, ", b =", b)

# Swapping using a temporary variable
temp = a
a = b
b = temp

print("After swapping: a =", a, ", b =", b, "\n")

print("Second way to swap two variables (Python shortcut):")
a, b = 10, 20
print("Before swapping: a =", a, ", b =", b)

# Swapping in one line
a, b = b, a

print("After swapping: a =", a, ", b =", b, "\n")


# ---------------------------------------------------------
# 3. Convert float to integer
# ---------------------------------------------------------

float_num = 5.7
int_num = int(float_num)  # Explicit type conversion
print("Float number:", float_num)
print("Converted Integer number:", int_num, "\n")


# ---------------------------------------------------------
# 4. Student ID Card Details
# ---------------------------------------------------------

print("Student ID Card (Simple Way)")
print("---------------------------")
print("Name: John Doe")
print("Age: 20")
print("Major: Computer Science")
print("University: XYZ University\n")


class Student:
    """Class to represent a Student with ID Card details."""

    def __init__(self, name, age, major, university):
        self.name = name
        self.age = age
        self.major = major
        self.university = university

    def display_id_card(self):
        """Method to display the Student’s ID card."""
        print("Student ID Card")
        print("----------------")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Major: {self.major}")
        print(f"University: {self.university}")


# Create a Student object and display ID Card
student = Student("Ammar", 18, "Computer Science", "XYZ University")
student.display_id_card()
print()


# ---------------------------------------------------------
# 5. User input for personal details
# ---------------------------------------------------------

print("Enter your personal details:")
name = input("Enter your name: ")
age = input("Enter your age: ")
address = input("Enter your address: ")
major = input("Enter your major: ")

print("\nYour Details are:")
print("Name:", name)
print("Age:", age)
print("Address:", address)
print("Major:", major, "\n")


# ---------------------------------------------------------
# 6. Integer and Float Conversion
# ---------------------------------------------------------

# Convert integer to float
int_num = int(input("Enter an integer: "))
float_num = float(int_num)
print("Integer number:", int_num)
print("Converted Float number:", float_num, "\n")

# Convert float to integer
float_num = float(input("Enter a float number: "))
print("Original Float number:", float_num)
print("Converted Integer number:", int(float_num))
