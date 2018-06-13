"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents = open('green-eggs.txt').read()
    print(contents)
    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    text_list = text_string.split()#saving a copy into a new var(text_list) while replacing content of text_strings into separate strings
    #loop over every two word pair
    for i in range(len(text_list)-2):#for every 'index' in the range of the len of text_list except for the last two
        key = (text_list[i],text_list[i+1])#index of 0 then +1(until the len of text_list ends) saves as a tuple in the key var
        chains[key] = chains.get(key,[])#saves keys into chains[key](dict) that aren't already in [key], if already in key from chain, will return an empty list 
        print("This is text_list[i] and text_list[i+1} "+text_list[i],text_list[i+1])
        chains[key].append(text_list[i+2])#

    print(chains)
    return chains


def make_text(chains):
    """Return text from chains."""

    # your code goes here
    key = choice(list(chains.keys()))
    words = list(key)

    while key in chains:
        words.append(choice(chains[key]))
        key = (words[-2], words[-1])

    print(words)

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
