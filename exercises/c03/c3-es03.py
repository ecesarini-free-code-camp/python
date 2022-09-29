num = input('Insert number between 0.0 and 1.0: ')
try:
	num = float(num)
	if num < 0 or num > 1:
		print('Error: number must be between 0 and 1!')
	elif num > 0.9:
		grade = 'A'
	elif num >= 0.8:
		grade = 'B'
	elif num >= 0.7:
		grade = 'C'
	elif num >= 0.6:
		grade = 'D'
	else:
		grade = 'F'
	print(grade)
except:
	print('Bad number')
