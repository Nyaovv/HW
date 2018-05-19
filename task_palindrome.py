def is_palindrome(b):
    b = str(b)
    b = b.lower()
    b = b.replace('.', '')
    b = b.replace(',', '')
    b = b.replace('!', '')
    b = b.replace(' ', '')

    if b == b[::-1]:
        return True
    else:
        return False
