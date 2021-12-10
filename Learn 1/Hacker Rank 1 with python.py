a = int(input())
if(a%2==0):
	if a >= 2 and a <= 5:
		print('Not Weird')
	elif a >= 6 and a < 20:
		print('Weird')
	elif a == 20:
		print('Weird')
	else:
		print('Not Weird')
else:
	print('Weird')
