"""
Program: Loop Exercises and Simple Billing System
Description:
    This script demonstrates the use of loops, conditionals, list comprehensions,
    and functions in Python through different small problems:
    1. Sum of even numbers up to 50
    2. First 20 numbers and their squares
    3. Sum of first 10 odd numbers
    4. Numbers divisible by 8 and 12 (up to 100)
    5. Simple supermarket billing system
"""

# ---------------------------------------------------------
# 1. Find the sum of even numbers up to 50
# ---------------------------------------------------------

# Using for loop with step size 2
sum_even = 0
for i in range(2, 50, 2):
    sum_even += i
print("The sum of even numbers up to 50 (for loop):", sum_even)
print()

# Using for loop with if condition
sum_even_if = 0
for i in range(1, 50):
    if i % 2 == 0:
        sum_even_if += i
print("The sum of even numbers up to 50 (with if condition):", sum_even_if)
print()


# ---------------------------------------------------------
# 2. First 20 numbers and their squares
# ---------------------------------------------------------

# Using simple for loop
for i in range(1, 21):
    print(f"Number: {i}, Square: {i**2}")
print()

# Using list comprehension
squares = [f"Number: {i}, Square: {i**2}" for i in range(1, 21)]
print("\n".join(squares))
print()


# ---------------------------------------------------------
# 3. Sum of first 10 odd numbers
# ---------------------------------------------------------

# Using while loop
sum_odd = 0
count = 0
num = 1
while count < 10:
    sum_odd += num
    num += 2
    count += 1
print("The sum of first 10 odd numbers (while loop):", sum_odd)
print()

# Using list comprehension
sum_odd_lc = sum([i for i in range(1, 20, 2)])
print("The sum of first 10 odd numbers (list comprehension):", sum_odd_lc)
print()

# Using if condition inside loop
sum_odd_if = 0
for i in range(1, 20):
    if i % 2 != 0:
        sum_odd_if += i
print("The sum of first 10 odd numbers (with if condition):", sum_odd_if)
print()

# Using filter function
sum_odd_filter = sum(filter(lambda x: x % 2 != 0, range(1, 20)))
print("The sum of first 10 odd numbers (filter):", sum_odd_filter)
print()
# ---------------------------------------------------------
# 4. Check numbers divisible by 8 and 12 up to 100
# ---------------------------------------------------------
# Using simple for loop
for i in range(1, 101):
    if i % 8 == 0 and i % 12 == 0:
        print(f"Number {i} is divisible by 8 and 12")
print()

# Using list comprehension
divisible_numbers = [i for i in range(1, 101) if i % 8 == 0 and i % 12 == 0]
print("Divisible numbers (list comprehension):", divisible_numbers)
print()

# Using filter
divisible_numbers_filter = list(filter(lambda x: x % 8 == 0 and x % 12 == 0, range(1, 101)))
print("Divisible numbers (filter):", divisible_numbers_filter)
print()

# Using while loop
i = 1
divisible_numbers_while = []
while i <= 100:
    if i % 8 == 0 and i % 12 == 0:
        divisible_numbers_while.append(i)
    i += 1
print("Divisible numbers (while loop):", divisible_numbers_while)
print()

# ---------------------------------------------------------
# 5. Simple Billing System (Supermarket)
# ---------------------------------------------------------
def billing_system():
    """Function to simulate a simple supermarket billing system."""
    total_amount = 0  # Initialize total bill to zero
    
    while True:
        # Ask for item name or 'done' to finish
        item_name = input("Enter item name (or 'done' to finish): ")
        if item_name.lower() == 'done':
            break  # Exit the loop if user is done
        
        # Get item price and quantity
        item_price = float(input("Enter item price: "))
        item_quantity = int(input("Enter item quantity: "))
        
        # Add cost of current item to total amount
        total_amount += item_price * item_quantity
    
    # Print the total bill
    print(f"Total bill amount is: {total_amount}")

# Run the billing system
billing_system()