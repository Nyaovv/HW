def snake_to_camel(name):
    name = name.title()
    name = name.replace('_', '')

    return(name)

def camel_to_snake(name):
    x = 0

    for i in range(len(name)):
        if 65 <= ord(name[0 + x]) <= 90:
            name = name[:0 + x] + "_" + chr(ord(name[0 + x])+32) + name[x + 1:]
        x += 1
    name = name.lstrip("_")
    return(name)
