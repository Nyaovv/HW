a = [14, 8, 3, 1, 89, 2, 45]
b = [0.14, 0.8, 0.3, 0.1, 0.89, 0.2, 0.45]
def average(lst):
    lel = len(lst)
    sm = sum(lst)
    arf = sm / lel
    print(round(arf, 3))
