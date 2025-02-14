#exercise 1
print("Hello, World!")
# Exercise 2: Simple Arithmetic
print("5 + 10 =", 5 + 10)
print("20 - 7 =", 20 - 7)
print("3 * 8 =", 3 * 8)
print("25 / 5 =", 25 / 5)

# Exercise 3: Age Calculator
age = 25  # Replace with your age
print(f"I am {age} years old.")

# Exercise 4: Temperature Converter
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"The temperature in Fahrenheit is: {fahrenheit}")

# Exercise 5: Odd or Even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

# Exercise 6: Check if a Number is Positive, Negative, or Zero
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Exercise 7: List Operations
numbers = [5, 2, 8, 1]
numbers.append(10)
numbers.remove(2)
print(len(numbers))
numbers.sort()
print(numbers)

# Exercise 8: Factorial of a Number
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"The factorial of {num} is: {factorial}")

# Exercise 9: Multiplication Table
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Exercise 10: Sum of Numbers in a List
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print("The sum of the numbers is:", total)

# Exercise 11: Guess the Number Game
import random
target = random.randint(1, 20)
print("I'm thinking of a number between 1 and 20. Try to guess it!")
while True:
    guess = int(input("Your guess: "))
    if guess < target:
        print("Too low. Try again.")
    elif guess > target:
        print("Too high. Try again.")
    else:
        print(f"Correct! The number was {target}.")
        break

# Exercise 12: Count Vowels in a String
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in string if char in vowels)
print("Number of vowels:", count)

# Exercise 13: FizzBuzz
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Exercise 14: Reverse a String
string = input("Enter a string: ")
print("Reversed string:", string[::-1])
