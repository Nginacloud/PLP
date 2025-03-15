def math_operation(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error, Can't divide by zero"
        else:
            return num1 / num2
    else:
        return "invalid operation"
    
def main():
    try:
        num1 = float(input("Enter number: "))
        num2 = float(input("Enter number: "))
        operation = input("Enter operation sign (+, -, *, /): ")

        result = math_operation(num1, num2, operation)
        if ("Error") in str(result):
            print(result)
        else:
            print(f"{num1} {operation} {num2} = {result}")
    except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()