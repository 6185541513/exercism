def latest(scores):
    return scores.pop()


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    return sorted(scores, reverse=True)[:3]

# I N T E R E S T I N G   S O L U T I O N   B Y   O T H E R
#    import heapq
#    top3 = heapq.nlargest(3,scores)
#    return top3
# M Y   F I R S T   S O L U T I O N
#    top_three = []
#
#    # sets number of iterations
#    it = 3
#    if len(scores) < 3:
#        it = len(scores)
#
#    # collects top three scores
#    for _ in range(it):
#        best = max(scores)
#        top_three.append(best)
#        scores.remove(best)
#
#    return top_three
