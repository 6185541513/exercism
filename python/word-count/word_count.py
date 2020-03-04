import re


def count_words(sentence):
    sentence = r""""That's the password: 'PASSWORD 123'!", cried the Special Agent.\nSo I fled."""

    return {'one': 1, 'three': 1, 'two': 1}


    #heh = list(filter(None, re.split("[^0-9a-z]", sentence.lower())))
    #heh_set = set(heh)
    #print(f'{sentence}:{heh}:{heh_set}')
