import re


def is_isogram(string):
    str_alpha = re.sub('[^a-z$]*', '', string.lower())
    return len(str_alpha) == len(set(str_alpha))
