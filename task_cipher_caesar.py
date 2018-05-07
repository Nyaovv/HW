def encode(b, c):

    x = ""
    for i in range(len(b)):
        if  65 <= ord(b[i]) <= 90:            
            if 90 < ord(b[i])+c:
                x = x +chr(ord(b[i]) + c - 26)
            else:
                x = x + chr(ord(b[i]) + c)                
        elif 97 <= ord(b[i]) <= 122:            
            if 122 < ord(b[i])+c:
                x = x +chr(ord(b[i]) + c - 26)
            else:
                x = x + chr(ord(b[i]) + c)                
        else:
            x = x + b[i]
    return(x)

# Декодирование поехало ===================================

def decode(b, c):

    x = ""
    for i in range(len(b)):
        if  65 <= ord(b[i]) <= 90:            
            if 65 > ord(b[i])-c:
                x = x +chr(ord(b[i]) - c + 26)
            else:
                x = x + chr(ord(b[i]) - c)                
        elif 97 <= ord(b[i]) <= 122:            
            if 97 > ord(b[i])-c:
                x = x +chr(ord(b[i]) - c + 26)
            else:
                x = x + chr(ord(b[i]) - c)                
        else:
            x = x + b[i]
    return(x)

