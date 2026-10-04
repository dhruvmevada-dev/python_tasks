def calculate(a, b, op):
    """Perform the operation on a and b. Raises ValueError for bad input."""
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    raise ValueError("Invalid operator. Use +, -, * or /.")


if __name__ == "__main__":
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /): ").strip()
        result = calculate(num1, num2, operator)
        print(f"{num1} {operator} {num2} = {result}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
