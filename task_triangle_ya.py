x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
x3=int(input())
y3=int(input())
d1=(x2-x1)**2+(y2-y1)**2
d2=(x3-x2)**2+(y3-y2)**2
d3=(x1-x3)**2+(y1-y3)**2
if d1==d2+d3:
    print('yes')
elif d2==d1+d3:
    print('yes')
elif d3==d1+d2:
    print('yes')
else:
    print('no')
