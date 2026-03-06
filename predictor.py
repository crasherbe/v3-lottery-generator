# predictor.py
# ---------------------------------------------------
# File ini memberi skor pada setiap kombinasi angka
# berdasarkan digit hot / normal / cold
# lalu menentukan 10 angka terbaik
# ---------------------------------------------------

def score_number(number, hot, cold):

    score = 0

    for d in number:

        digit = int(d)

        if digit in hot:
            score += 3

        elif digit in cold:
            score += 1

        else:
            score += 2

    return score


def get_top_numbers(numbers, hot, cold, top=10):

    scored = []

    for n in numbers:

        s = score_number(n, hot, cold)

        scored.append((n, s))

    scored.sort(key=lambda x: x[1], reverse=True)

    return scored[:top]
