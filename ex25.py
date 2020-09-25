def break_words(stuff):
    """Tis function will break up words for us"""
    words = stuff.split(' ')
    return words
#This will sort the words alphabetically
def sort_words(words):
    """Sorts the words"""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words"""
    words = break_words(sentence)
    return sort_words(words)

def print_last_and_first(sentence):
    """Prints the first and the last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and the last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


