hrs = input('Enter hours: ')
rate = input('Enter rate: ')
flag = False
try:
	hrs = int(hrs)
	rate = int(rate)
except: 
	flag = True
if flag:
	print('Hours and rate must be integer number')
else:
	print('Payment', hrs*rate)
