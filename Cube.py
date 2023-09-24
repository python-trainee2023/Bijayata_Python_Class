def cube_number(number):
    return number ** 3


num = int(input("Enter a number: "))
result = cube_number(num)
print(f"The cube of {num} is {result}")