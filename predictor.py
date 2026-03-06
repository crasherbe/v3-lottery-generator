from strategy import SCORE_HOT, SCORE_NORMAL, SCORE_COLD

def score_number(num,analysis):
    score = 0
    for d in num:
        if d in analysis["hot"]:
            score += SCORE_HOT
        elif d in analysis["normal"]:
            score += SCORE_NORMAL
        else:
            score += SCORE_COLD
    return score

def pick_best(numbers,analysis,top=10):
    scored = [(n,score_number(n,analysis)) for n in numbers]
    scored.sort(key=lambda x:x[1], reverse=True)
    return [x[0] for x in scored[:top]]
