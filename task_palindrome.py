s = 'lols'

def is_palindrome(s):
    s = str(s)
    b = s[::-1]
    if b == s:
        return True
    else:
        return False
