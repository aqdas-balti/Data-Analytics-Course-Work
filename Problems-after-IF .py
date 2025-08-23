#Write a program to check number is positive?
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num == 0:
    print("The number is zero.")
else:
    print("The number is negative.")
print()
#Short hand if statement
num1= float(input("Enter a number: "))

if (num1 > 0): print("The number is positive.")
print()

#Short hand of if else steatement
num3= float(input("Enter a number: "))
print("The no is positive.") if (num3 > 0) else print("The no is negative.")

#Write a program to check weather a number is even or odd
num4 = float(input("Enter a number: "))
print("The number is even.") if (num4 % 2 == 0) else print("The number is odd.")

#Without using shorthand
if (num4 % 2 == 0):
    print("The number is even.")
else:
    print("The number is odd.")