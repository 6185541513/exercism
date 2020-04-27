import re


def abbreviate(words):
    return "".join(re.findall(r"([A-Z])[A-Z']*", words.upper()))

# F I R S T   S O L U T I O N
# return "".join(list(map(lambda word: str(word[0]), re.findall("[A-Z]+'?[A-Z]*", words.upper()))))
