def get_quadrant_number(x, y):
    z = 0

    if x > 0 and y > 0:
        z = 1
    elif x < 0 and y > 0:
        z = 2
    elif x < 0 and y < 0:
        z = 3
    elif x > 0 and y < 0:
        z = 4
    else:
        raise ValueError

    return(z)
