# Input from the user
start = int(input("Enter the start value: "))
stop = int(input("Enter the stop value: "))


sum_even = lambda start, stop: sum(num for num in range(start, stop + 1) if num % 2 == 0)
sum_odd = lambda start, stop: sum(num for num in range(start, stop + 1) if num % 2 != 0)


even_sum = sum_even(start, stop)
odd_sum = sum_odd(start, stop)

# Display the results
print(f"Sum of even numbers from {start} to {stop}: {even_sum}")
print(f"Sum of odd numbers from {start} to {stop}: {odd_sum}")