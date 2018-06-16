"""
Hex - 16 система счисления
Oct - 8 система счисления
Dec - 10 система счисления
"""

def dec2bin(number): # str || 10 => 2
    number = int(number)
    result = ''
    while number > 0:
        pre = number % 2
        number = number // 2
        pre = str(pre)
        result = result + pre
    result = result[::-1]
    return str(result)


def dec2oct(number): # str | 10 => 8
    number = int(number)
    result = ''
    while number > 0:
        pre = number % 8
        number = number // 8
        pre = str(pre)
        result = result + pre
    result = result[::-1]
    return str(result)


def dec2hex(number): # str | 10 => 16
    number = int(number)
    result = ''
    while number > 0:
        pre = number % 16
        number = number // 16
        if pre == 15:
            pre = 'F'
        elif pre == 14:
            pre = 'E'
        elif pre == 13:
            pre = 'D'
        elif pre == 12:
            pre = 'C'
        elif pre == 11:
            pre = 'B'
        elif pre == 10:
            pre = 'A'
        pre = str(pre)
        result = result + pre
    result = result[::-1]
    return str(result)


def bin2dec(number): # int | 2  => 10
    result = 0
    number = str(number)
    step = len(number) - 1
    for i in range(len(number)):
        pre = int(number[i]) * 2 ** step
        result = result + int(pre)
        step = step - 1
    result = int(result)
    return int(result)


def oct2dec(number): # int | 8  => 10
    number = str(number)
    result = 0
    step = len(number) - 1
    for i in range(len(number)):
        pre = int(number[i]) * 8 ** step
        result = result + int(pre)
        step = step - 1
    result = int(result)
    return int(result)


def hex2dec(number): # int | 16 => 10
    number = str(number)
    result = 0
    step = len(number) - 1
    number = number.upper()
    for i in range(len(number)):
        if number[i] == 'F':
            opa = 15
        elif number[i] == 'E':
            opa = 14
        elif number[i] == 'D':
            opa = 13
        elif number[i] == 'C':
            opa = 12
        elif number[i] == 'B':
            opa = 11
        elif number[i] == 'A':
            opa = 10
        else:
            opa = int(number[i])
        pre = opa * 16 ** step
        result = result + int(pre)
        step = step - 1
    return int(result)
