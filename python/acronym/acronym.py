import re


def abbreviate(words):
    return "".join(list(map(lambda word: str(word[0].upper()), re.findall("[A-Z]+'?[A-Z]*", words.upper()))))
