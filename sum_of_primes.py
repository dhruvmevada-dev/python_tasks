def is_prime(num):
    """Return True if num is a prime number."""
    if num < 2:
        return False
    if num % 2 == 0:
        return num == 2
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True


def sum_of_first_n_primes(n):
    """Return the sum of the first n prime numbers."""
    total = 0
    count = 0
    candidate = 2
    while count < n:
        if is_prime(candidate):
            total += candidate
            count += 1
        candidate += 1
    return total


if __name__ == "__main__":
    try:
        n = int(input("Enter N: "))
        if n < 1:
            print("Please enter a positive integer.")
        else:
            print(f"Sum of the first {n} prime numbers: {sum_of_first_n_primes(n)}")
    except ValueError:
        print("Invalid input. Please enter an integer.")
