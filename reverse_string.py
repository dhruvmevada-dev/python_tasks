def reverse_string(text):
    """Reverse a string without slicing, reversed() or .reverse()."""
    result = ""
    for char in text:
        result = char + result
    return result


if __name__ == "__main__":
    s = input("Enter a string: ")
    print("Reversed:", reverse_string(s))
