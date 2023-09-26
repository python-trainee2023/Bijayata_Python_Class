def sum_even_odd_numbers(start, stop):
    even_sum = sum(num for num in range(start, stop + 1) if num % 2 == 0)
    odd_sum = sum(num for num in range(start, stop + 1) if num % 2 != 0)
    return even_sum, odd_sum

# Input from the user
start = int(input("Enter the start value: "))
stop = int(input("Enter the stop value: "))


even_sum, odd_sum = sum_even_odd_numbers(start, stop)

print(f"Sum of even numbers from {start} to {stop}: {even_sum}")
print(f"Sum of odd numbers from {start} to {stop}: {odd_sum}")