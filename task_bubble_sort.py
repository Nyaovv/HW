def bubble_sort(lst): # Теперь всё работает ЧЁТКО
    for y in range(len(lst)): # Сделал два цикла, чтоб второй цикл несколько раз прошелся
        for i in range(len(lst)):# по всем числам в кортеже.
            g = len(lst)

            if i+1 in range(len(lst)):# Вот тут он проходится по числам
                if lst[i] > lst[i+1]:
                    c = lst.pop(i)# Вытащил элемент
                    lst.insert(i+1, c)# Вставил элемент
            else:
                c = lst.pop(i)
                lst.insert(g, c)
    return lst
