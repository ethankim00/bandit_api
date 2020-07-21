
import json

def word_to_dict_key(word):
    """Convert word to it's stored form"""
    return "".join(sorted(word))


def search_permutations(word, nodes):
    """ Get all permutations of a word that are valid words """
    key = word_to_dict_key(word)
    try:
        return nodes[key]
    except:
        return False


def get_new_words(word, nodes):
    """Get words that can be played with one additional letter - return as JSON"""
    
    print(word)
    alphabet = 'abdefghijklmnopqrstuvwxyz'
    words = search_permutations(word, nodes)
    # Print word and permutations
    permutations = []
    if words:
        for word in words:
            permutations.append(word)
    
    new_words = []
    base = word
    for next_node in alphabet:
        word = base + next_node
        words = search_permutations(word, nodes)
        if words:
            new_words = words + new_words
    
    return {'permutations': permutations, 'new': new_words}