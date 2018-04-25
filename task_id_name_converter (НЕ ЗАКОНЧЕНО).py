name = 'CamelCase' # => 'camel_case'
j = 'getUserId'

def snake_to_camel(name):
    name = name.title()
    name = name.replace('_', '')
    print(name)

def camel_to_snake(name):
    name = name.replace('Q', '_Q') # Сейчас три ночи, я её оставил на потом, если что
    name = name.replace('W', '_W')# Совсем не лезет в голову что с кемел ту снейк придумать что-то
    name = name.replace('E', '_E')
    name = name.replace('R', '_R')
    name = name.replace('T', '_T')
    name = name.replace('Y', '_Y')
    name = name.replace('U', '_U')
    name = name.replace('I', '_I')
    name = name.replace('O', '_O')
    name = name.replace('P', '_P')
    name = name.replace('A', '_A')
    name = name.replace('S', '_S')
    name = name.replace('D', '_D')
    name = name.replace('F', '_F')
    name = name.replace('G', '_G')
    name = name.replace('H', '_H')
    name = name.replace('J', '_J')
    name = name.replace('K', '_K')
    name = name.replace('L', '_L')
    name = name.replace('Z', '_Z')
    name = name.replace('X', '_X')
    name = name.replace('C', '_C')
    name = name.replace('V', '_V')
    name = name.replace('B', '_B')
    name = name.replace('N', '_N')
    name = name.replace('M', '_M')
    name = name.lower()
    name.strip("_")
    print(name)
