# Hello there everyone, I will teach you some main python scripts that will help you in your journey
# of learning this language:


# 1. Hello World

# def print_hello_world():
#     print("Hello World!")
#
# if __name__ == "__main__":
#     print_hello_world()

# 2. Calculate the TIP at a table, depending on the value and percentage

# def calculate_tip(value, percentage):
#     return value * (percentage / 100)
#
# if __name__ == "__main__":
#     value = 50
#     tip_percentage = 20
#     tip = calculate_tip(value, tip_percentage)
#     print(f'Tip value is {tip} for {tip_percentage}% of {value}')

# 3. Guess the number easy game
# this game will work for any number between 1 and 10

# import random
# def guess_the_number():
#     number = random.randint(1, 10) # we define the value to be between 1 and 10
#     number_of_guesses = 3
#     print(f'Guess the correct number between 1 and 10, number of guesses left: {number_of_guesses}')
#     for i in range(0, number_of_guesses):
#         input_value = int(input("Enter the value you think is correct: "))
#         if input_value == number:
#             print("CORRECT")
#             exit()
#         else:
#             print(f'WRONG, TRY AGAIN, NUMBER OF GUESSES LEFT: {number_of_guesses - i - 1}')
#     print('TASK FAILED! PLAY AGAIN')
#
# if __name__ == "__main__":
#     guess_the_number()

# 4. Simple Calculator
#
# def add(x, y):
#     return x + y
#
# def subtract(x, y):
#     return x - y
#
# def multiply(x, y):
#     return x * y
#
# def power(x, y):
#     return x ** y
#
# def divide(x, y):
#     if y == 0:
#         return 'Error! Division by zero.'
#     else:
#         return x / y
#
# def calculator():
#     print("Select Option:\n1. Addition\n2. Subtraction\n3. Power\n4. Multiplication\n5. Division")
#     choice = int(input("Enter choice number: "))
#     number1 = float(input("Enter first number: "))
#     number2 = float(input("Enter second number: "))
#     if choice == 1:
#         result = add(number1, number2)
#         print(f'Result of {number1} + {number2} is {result}')
#     elif choice == 2:
#         result = subtract(number1, number2)
#         print(f'Result of {number1} - {number2} is {result}')
#     elif choice == 3:
#         result = power(number1, number2)
#         print(f'Result of {number1} ** {number2} is {result}')
#     elif choice == 4:
#         result = multiply(number1, number2)
#         print(f'Result of {number1} * {number2} is {result}')
#     elif choice == 5:
#         result = divide(number1, number2)
#         print(f'Result of {number1} / {number2} is {result}')
#     else:
#         print("Invalid choice")
#
#
# if __name__ == "__main__":
#     while True:
#         calculator()

# 5. Simple Celsius to Fahrenheit and back conversion

# def celsius_to_fahrenheit(temperature):
#     return (temperature * 9/5) + 32
#
# def fahrenheit_to_celsius(temperature):
#     return (temperature - 32) * 5/9
#
# def temperature_converter():
#     print("Temperature converter\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius")
#     choice = int(input("Enter choice number:"))
#     if choice == 1:
#         temperature = float(input("Enter temperature in Celsius: "))
#         fahrenheit = celsius_to_fahrenheit(temperature)
#         print(f'{temperature} degrees Celsius is {fahrenheit} degrees Fahrenheit')
#     elif choice == 2:
#         temperature = float(input("Enter temperature in Fahrenheit: "))
#         celsius = fahrenheit_to_celsius(temperature)
#         print(f'{temperature} degrees Fahrenheit is {celsius} degrees Celsius')
#     else:
#         print("Invalid choice")
#
# if __name__ == "__main__":
#     while True:
#         temperature_converter()
