user_input = input('Enter 3 numbers')
input_list = list(user_input.split(','))

num_list = [int(x) for x in input_list]

max_num = max(num_list)


print(max_num)