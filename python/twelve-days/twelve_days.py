from collections import OrderedDict

def recite(start_verse, end_verse):
    common_phrase = "On the {} day of Christmas my true love gave to me: "
    first_row = [common_phrase.format('first'), "a Partridge in a Pear Tree."]
    second_row = [common_phrase.format('second'), "two Turtle Doves, ", "and a Partridge in a Pear Tree."]
    twelve_days = [first_row, second_row]

    mapping = OrderedDict([
    					   ('third', 'three French Hens, '),
    					   ('fourth', 'four Calling Birds, '),
    					   ('fifth', 'five Gold Rings, '),
    					   ('sixth', 'six Geese-a-Laying, '),
    					   ('seventh', 'seven Swans-a-Swimming, '),
    					   ('eighth', 'eight Maids-a-Milking, '),
    					   ('ninth', 'nine Ladies Dancing, '),
    					   ('tenth', 'ten Lords-a-Leaping, '),
    					   ('eleventh', 'eleven Pipers Piping, '),
    					   ('twelfth', 'twelve Drummers Drumming, '),
    					  ])

    for k, v in mapping.items():
    	row = [common_phrase.format(k), v] + twelve_days[-1][1:len(twelve_days[-1])]
    	twelve_days.append(row)

    result = []
    for verse in range(start_verse, end_verse + 1):
    	result.append(''.join(twelve_days[verse - 1]))
    return result
