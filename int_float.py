original_list = [1, 2.0, 3.5, 4, 5.6, 6]

integers_only = [x for x in original_list if isinstance(x, int)]

print(integers_only)