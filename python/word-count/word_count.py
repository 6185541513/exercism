import re
from collections import Counter


def count_words(sentence):
    return Counter(re.findall(r"[a-z0-9]+'?[a-z]*(?<!')", sentence.casefold()))

# F I R S T   S O L U T I O N
# (╯°□°）╯︵ ┻━┻
