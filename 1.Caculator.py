

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("Enter the first number: "))
    for key in operations:
        print(key)
    run_operation = True
    while run_operation:

        operation_symbol = input("Pick an operation : ")
        num2 = float(input("Enter the next number: "))
        claculation = operations[operation_symbol]
        answer = claculation(num1, num2)
        print(f"{num1} {operation_symbol} {num2} is {answer}")

        continue_operation = input(
            f"Type 'y' to continue the calculation with {answer}, or type 'q' to exit or'n' to new calculation: ")
        if continue_operation == 'y':
            run_operation = True
            num1 = answer
        if continue_operation == 'n':
            calculator()
        if continue_operation == 'q':
            run_operation = False
            print("operation exited!")


calculator()














