def fibonacci(n):
    chislo = 0
    second = [0, 1] # Я сначала делал через цикл фор, и о боги, как же я долго думал, что не так
    while n: # потом замутил божественный вайл, и свершилось чудо!!!!
        n -= 1
        chislo = second[0] + second[1]
        second = [second[1], chislo]
        res = second[0]
        yield res
