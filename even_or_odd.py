def check_even_odd(number):
    """Return 'Even' or 'Odd' for the given integer."""
    return "Even" if number % 2 == 0 else "Odd"


if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        print(f"{num} is {check_even_odd(num)}.")
    except ValueError:
        print("Invalid input. Please enter an integer.")
