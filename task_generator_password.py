import random

def password_generator(l):
    par = ''
    for i in range(l):
        r = random.uniform(1, 3)
        r = int(r)
        if r == 2:
            x = random.uniform(97, 122)
        else:
            x = random.uniform(65, 90)
        x = int(x)
        par = par + chr(x)
    while 1:
        yield par
