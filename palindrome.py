def is_palindrome(s):

    s = s.replace(" ", "").lower()

    return s == s[::-1]



input_string = "hi bijj"
result = is_palindrome(input_string)
if result:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")