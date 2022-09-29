def computegrade(score):
	try:
		score = float(score)
		if score < 0 or score > 1:
			grade = 'Errore, input must be between 0 and 1'
		elif score >= 0.9:
			grade = 'A'
		elif score >= 0.8:
			grade = 'B'
		elif score >= 0.7:
			grade = 'C'
		elif score >= 0.6:
			grade = 'D'
		elif score < 0.6:
			grade = 'F'
		return grade
	except:
		print('Bad data')

print(computegrade(0.9))
