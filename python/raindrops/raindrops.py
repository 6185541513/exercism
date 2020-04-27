import math


def convert(number):
    FACTOR_SOUNDS = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
    sound = ''

    # exclude NaN
    if math.isnan(number):
        raise Exception("'number' is NaN")

    # build sound
    for factor in FACTOR_SOUNDS.keys():
        if number % factor == 0:
            sound += FACTOR_SOUNDS.get(factor)

    return sound or str(number)

# F I R S T   S O L U T I O N
#    result = ""
#
#    if math.isnan(number):
#        raise Exception("'number' is NaN")
#
#    if number % 3 == 0:
#        result += "Pling"
#    if number % 5 == 0:
#        result += "Plang"
#    if number % 7 == 0:
#        result += "Plong"
#
#    return result or """{}""".format(number)
