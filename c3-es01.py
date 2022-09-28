hrs = int(input('Enter hours: '))
rate = int(input('Enter rate: '))
srhr = hrs - 40

if srhr > 0:
	pay = 40 * rate + 1.5 * srhr * rate
else:
	pay = hrs * rate
print('Retribution', pay)