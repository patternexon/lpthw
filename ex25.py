
def break_words(stuff):
    """ This breaks words """
    words = stuff.split(' ')
    return words

def sort_words(words):
    """ Sorts the words. """
    return sorted(words)

def print_first_word(words):
    """ Prints the first word after popping it off """
    word = words.pop(0)
    return word

def print_last_word(words):
    """ Prints the last word after popping it off """
    word = words.pop(-1)
    return word

