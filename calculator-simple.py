"""
    -> Create Simple Calculators Applications.
        - BY | Hesham ALsaqqaf.
        - Data | 27-7-2024.
"""

# Define the calculator functions


# * Function Sumation
def add(number1, number2):
    return number1 + number2


# * Function Subtraction
def substract(number1, number2):
    return number1 - number2


# * Function Multiplication
def multiply(number1, number2):
    return number1 * number2


# * Function Divide
def divide(number1, number2):
    if number2 == 0:
        return "Can't divide by zero"
    else:
        return number1 / number2


print("\n ------ Wellcome For You The Calculator Apps ❤️ : ------ \n")
# Start Get Input 2 Number From Users
num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))
# Start Choise Operators
print("----------------------")
print("Select Operations: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("----------------------")

choice = input("Enter Choice (1/2/3/4): ")


# Start Perform Calculation And Print Results
if choice == "1":
    print("Result = ", num1, "+", num2, "=", add(num1, num2))
elif choice == "2":
    print("Result = ", num1, "-", num2, "=", substract(num1, num2))
elif choice == "3":
    print("Result = ", num1, "*", num2, "=", multiply(num1, num2))
elif choice == "4":
    print("Result = ", num1, "/", num2, "=", float(divide(num1, num2)))

else:
    print("Invalid Input Choice.")

print("\n ------ Thanks For Using Calculator🖐️: ------ \n")
