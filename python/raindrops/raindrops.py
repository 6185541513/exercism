import math


def convert(number):
    result = ""

    if math.isnan(number):
        raise Exception("'number' is NaN")

    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"

    return result or """{}""".format(number)
