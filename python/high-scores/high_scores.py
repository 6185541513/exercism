def latest(scores):
    return scores.pop()


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    top_three = []

    # sets number of iterations
    it = 3
    if len(scores) < 3:
        it = len(scores)

    # collects top three scores
    for _ in range(it):
        best = max(scores)
        top_three.append(best)
        scores.remove(best)

    return top_three
