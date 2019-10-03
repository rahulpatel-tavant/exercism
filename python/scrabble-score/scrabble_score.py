def score(word):
	score = 0
	letter_values = {
					 ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T') : 1,
					 ('D', 'G') : 2,
					 ('B', 'C', 'M', 'P') : 3,
					 ('F', 'H', 'V', 'W', 'Y'): 4,
					 ('K') : 5,
					 ('J', 'X') : 8,
					 ('Q', 'Z') : 10
					}
	for letter in word.upper():				
		for letters, value in letter_values.items():
			if letter in letters:
				score = score + value
	return score			
