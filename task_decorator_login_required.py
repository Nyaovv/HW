import hashlib

valid = 0

def login_required(func):
    def wrapper(*args, **kwargs):
        global valid
        if not valid:
            count = 0
            while count < 3:
                if valid == 1:
                    return func(*args, **kwargs)
                username = input()
                password = input()
                s = username + password
                entered = str(hashlib.md5(s.encode()).hexdigest())

                with open('token.txt') as f:
                    x = str(f.read())

                if entered == x:
                    valid = 1
                count += 1
            else:
                return None
        if valid:
            return func(*args, **kwargs)
    return wrapper
