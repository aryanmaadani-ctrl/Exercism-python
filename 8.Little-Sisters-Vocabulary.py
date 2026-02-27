def add_prefix_un(word)  :
    return 'un' + word

def make_word_groups(vocab_words,  ):
    vocab_words = list(vocab_words)
    seperator = ' :: ' + vocab_words[0]
    return seperator.join(vocab_words)

def remove_suffix_ness(word):
    root = word.removesuffix('ness')
    if root.endswith('i'):
        return root.replace('i', 'y')
    else:
        return word.removesuffix('ness')

def adjective_to_verb(sentence,index):
    split_sentence =  str.split(sentence)
    adjective = split_sentence[index] + 'en'
    if "." in adjective:
        return adjective.replace('.', '')
    else:
        return adjective
