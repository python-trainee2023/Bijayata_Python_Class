def generate_fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence

try:
    n = int(input("Enter the number of Fibonacci terms to display: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        fibonacci_sequence = generate_fibonacci(n)
        print("Fibonacci Sequence:")
        for term in fibonacci_sequence:
            print(term, end=" ")
except ValueError:
    print("Invalid input. Please enter a positive integer.")