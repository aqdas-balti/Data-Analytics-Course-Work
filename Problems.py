#Write a program to display's a person name, age and address in three different lines
print("One way to do this is:")
print("Name: John Doe")
print("Age: 30")
print("Address: 123 Main St, Anytown, USA \n")

print("Second way to do this is:")
print("Name: Aqdas \nAge: 22 \nAddress: 123 Main St, Anytown, USA")

print("Third way to do this is:")
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")

person = Person("Ali Hassan", 28, "123 Main St, Anytown, USA")
person.display_info()
print()

#Write a program to swap two variables
print("First way to swap two variables:")
a = 5
b = 10
print("Before swapping:")
print("a =", a)
print("b =", b)

# Swapping
temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)
print()

#left int right and right value into left
print("Second way to swap two variables:")
a=10
b=20
a,b=b,a
print("After swapping:")
print("a =", a)
print("b =", b)
print()

#Write a program to convert float to integer
float_num = 5.7
int_num = int(float_num)
print("Float number:", float_num)
print("Integer number:", int_num)
print()

#Write a program to take detail of a student for id card and print it into different lines
print("Student ID Card")
print("----------------")
print("Name: John Doe")
print("Age: 20")
print("Major: Computer Science")
print("University: XYZ University")

#Write a program to take detail of a student for id card and print it into different lines
class Student:
    def __init__(self, name, age, major, university):
        self.name = name
        self.age = age
        self.major = major
        self.university = university

    def display_id_card(self):
        print("Student ID Card")
        print("----------------")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Major: {self.major}")
        print(f"University: {self.university}")

student = Student("Ammar", 18, "Computer Science", "XYZ University")
student.display_id_card()
print()
print(bin(15))
name=input("Enter your name: ")
age=input("Enter your age: ")
address=input("Enter your address: ")
major=input("Enter Your Major: ")
print("Name:",name)
print("Age:",age)
print("Address:",address)
print("Major:",major)

#Write a program to take as input int and convert to float
int_num = int(input("Enter an integer: "))
float_num = float(int_num)
print("Integer number:", int_num)
print("Float number:", float_num)

float_num = float(input("Enter a float number:"))
print("The integer form is:", int(float_num))
print("The float number is:", float_num)

