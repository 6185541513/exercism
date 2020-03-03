def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("The strands differ in length")

    return sum(a != b for a, b in zip(strand_a, strand_b))

# F I R S T   S O L U T I O N
#    count = 0
#    for i in range(len(strand_a)):
#        if strand_a[i] != strand_b[i]:
#            count = count + 1
#    return count
