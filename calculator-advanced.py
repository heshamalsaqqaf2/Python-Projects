# Functions Parser Expression
def parse_expression(expression):
    expression = expression.replace(" ", "")
    tokens = []
    current_number = ""
    for char in expression:
        if char.isdigit() or char == ".":
            current_number += char
        else:
            if current_number:
                tokens.append(float(current_number))
                current_number = ""
            tokens.append(char)
    if current_number:
        tokens.append(float(current_number))
    return tokens


# Functions Apply Operations
def apply_operations(operands, operator):
    right = operands.pop()
    left = operands.pop()
    if operator == "+":
        operands.append(left + right)
    elif operator == "-":
        operands.append(left - right)
    elif operator == "*":
        operands.append(left * right)
    elif operator == "/":
        operands.append(left / right)


# Functions Evaluate Tokens
def evaluate_tokens(tokens):
    operands = []
    operators = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if isinstance(token, float):
            operands.append(token)
        elif token in "+-*/":
            while operators and operators[-1] in "*/" and token in "+-":
                apply_operations(operands, operators.pop())
            operators.append(token)
        elif token == "(":
            operators.append(token)
        elif token == ")":
            while operators and operators[-1] != "(":
                apply_operations(operands, operators.pop())
            operators.pop()
        i += 1
    while operators:
        apply_operations(operands, operators.pop())
    return operands[0]


# Functions Evaluate Expression
def evaluate_expression(expression):
    tokens = parse_expression(expression)
    return evaluate_tokens(tokens)


# Functions Calculator
def calculator():
    print("Welcome to the Calculator App.")
    print("You can enter any mathematical expression, e.g., 2/(5*3)2+5")

    while True:
        expression = input("Enter the expression: ")
        try:
            result = evaluate_expression(expression)
            print(f"Result = {result}")
        except Exception as ex:
            print(f"Error in computing the expression: {ex}")
        next_calculator = input("Do you want to compute another expression? (yes/no) ")
        if next_calculator.lower() != "yes":
            break
    print("Thank you for using the calculator!")


calculator()
