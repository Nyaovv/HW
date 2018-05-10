from datetime import datetime, date, time, timedelta

def counter():
    dt = datetime.now()

    ng = datetime(dt.year + 1, 1, 1)

    delta = ng - dt

    xhour = delta.seconds // 3600 # посчитанные часы
    xminute = (delta.seconds % 3600 ) // 60 # минуты

    if delta.days % 100 % 10 == 1:
        day = ' день '
    elif delta.days % 100 % 10 in range(2, 5) and delta.days % 100 not in range(10, 20):
        day = ' дня '
    else:
        day = ' дней '
        
    if xhour % 10 == 1:
        hour = ' час '
    elif xhour % 10 in range(2, 5) and xhour % 100 not in range(10, 20):
        hour = ' часа '
    else:
        hour = ' часов '

    if xminute % 10 == 1:
        minute = ' минута '
    elif xminute % 10 in range(2, 5) and xminute % 100 not in range(10, 20):
        minute = ' минуты '
    else:
        minute = ' минут '

    x = str(delta.days) + day + str(xhour) + hour + str(xminute) + minute
    print(x)
