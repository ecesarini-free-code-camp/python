def computepay(hours, rate):
	try:
		hours = int(hours)
		rate = float(rate)
		extra = hours - 40
		if hours > 40:
			pay = rate * 40 + extra * rate * 1.5
		elif hours <= 40 and hours > 0:
			pay = rate * hours
		else:
			pay = 'Error counting hours.'
	except:
		print('Error in input data')
	return pay

pay = computepay(-2, 10)
print(pay)