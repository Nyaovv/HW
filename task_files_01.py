n = int(input())
p = int(input())

with open('data.txt') as f:
    s = str(f.read())
    s = s.split(" ")
    g = '' # Делящиеся на n без остатка
    z = '' # Возведенные в степень p

    for i, b in enumerate(s):
        if int(s[i]) % n == 0:
            x = s[i] = int(b)
            g = g + str(x) + ' '

    for i, b in enumerate(s):
            x = s[i] = int(b) ** p
            z =  z + str(x) + ' '

with open('out-1.txt', 'w') as k:
    k.write(str(g))

with open('out-2.txt', 'w') as l:
    l.write(str(z))
