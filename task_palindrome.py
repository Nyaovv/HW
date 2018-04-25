def is_palindrome(s):
    s = str(s)
    b = s[::-1]
    if s == b:
        print('True')
    else:
        print('False')
