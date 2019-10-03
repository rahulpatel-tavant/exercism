def convert(number):
    sound_mapping = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
    sound = ''
    for k, v in sound_mapping.items():
    	if number % k == 0:
    		sound = sound + v
    if not sound:
    	sound = str(number)
    return sound
