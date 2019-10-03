def is_isogram(string):
	string = ''.join(char for char in string.lower() if not char in [' ', '-'])
	return len(string) == len(set(string))