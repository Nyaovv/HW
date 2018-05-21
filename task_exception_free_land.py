def get_free_land(tup1, tup2):
    # tup1 = [100, '1:1'] площадь садового участка в сотках и соотношение сторон
    # tup2 = [15, 25]     ширину и длину одной грядки в метрах.
    tup1 = int(tup1[0])
    if tup1 <= 0:
        raise ValueError('Не задана площадь участка')
    elif tup2[0] * tup2[1] == 0:
        raise ValueError('Не задана площадь грядки')
    elif tup1 * 100 < tup2[0] * tup2[1]:
        raise ValueError('Размер грядки больше размера участка')
    else:
        n1 = tup1
        n1 = n1 * 100
        n2 =tup2[0] * tup2[1]
        res = n1 % n2
    return res
