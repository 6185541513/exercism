import re


def score(word):
    return sum(map(letter_point, word.upper()))


def letter_point(letter):
    for letter_points in list(filter(None, point_system.splitlines())):
        if letter in letter_points:
            return int(re.search("[0-9]+", letter_points).group())

    raise ValueError(f'Letter \'{letter}\' not included in point system')


point_system = """
A, E, I, O, U, L, N, R, S, T       1
D, G                               2
B, C, M, P                         3
F, H, V, W, Y                      4
K                                  5
J, X                               8
Q, Z                               10
"""
