def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

try:
    n = int(input("Enter a number to calculate its factorial: "))
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(n)
        print(f"The factorial of {n} is {result}")
except ValueError:
    print("Invalid input. Please enter a non-negative integer.")