from collections import Counter
from strategy import LAST_DRAW_WEIGHT, MIRROR_MAP

def analyze_history(history):
    """
    history: list of strings, setiap angka satu baris
    """
    digits = []
    pairs = []
    trend_counter = Counter()
    
    for i,num in enumerate(history):
        weight = 1
        if i == len(history)-1:
            weight = LAST_DRAW_WEIGHT
        for d in num:
            digits.extend([d]*weight)
            trend_counter[d] += weight
        # digit pair
        for j in range(len(num)-1):
            pairs.append((num[j], num[j+1]))
    
    freq = Counter(digits)
    sorted_digits = sorted(freq.items(), key=lambda x:x[1], reverse=True)
    
    hot = [x[0] for x in sorted_digits[:3]]
    cold = [x[0] for x in sorted_digits[-3:]]
    normal = [x[0] for x,_ in sorted_digits[3:-3]]
    mirror_digits = [MIRROR_MAP[d] for d in hot]
    trend = [d for d,count in trend_counter.items() if count>=2]  # threshold 2
    skip = [str(d) for d in range(10) if str(d) not in freq.keys()]
    
    return {
        "frequency": freq,
        "hot": hot,
        "cold": cold,
        "normal": normal,
        "mirror": mirror_digits,
        "trend": trend,
        "skip": skip,
        "pairs": pairs
    }
