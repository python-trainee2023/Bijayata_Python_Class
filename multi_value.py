user_values = []
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

while True:
    user_input = input("Enter a value (or 'done' to finish): ")

    if user_input.lower() == 'done':
        break

    user_values.append(user_input)

# Use list comprehensions to separate strings and numbers
strings = [value for value in user_values if not value.isdigit()]
numbers = [int(value) for value in user_values if value.isdigit()]
floats = [value for value in user_values if is_float(value)]
print("Strings:", strings)
print("Numbers:", numbers)
print("Floats:", floats)
