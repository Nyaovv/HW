b = int(input())
if b%100==0 and b%400!=0 or b%4!=0:
	print('no')
else:
	print('yes')
input()