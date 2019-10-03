def count_words(sentence):
    bad_chars = ["!", "&", "@", "$", "%", "^", "&", ",", ":", "\n", "_", ".", "\t"]
    for bad_char in bad_chars:
    	sentence = sentence.replace(bad_char, ' ')
    words = [str.lower().strip("'") for str in sentence.split(' ') if str]
    words_count = {}
    for word in words:
        if word in words_count:
            words_count[word] = words_count[word] + 1
        else:
            words_count[word] = 1
    return words_count    			 
