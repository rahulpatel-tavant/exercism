def abbreviate(words):
    return ''.join(word.strip('_')[0].upper() for word in words.replace('-', ' ').split(' ') if word)
