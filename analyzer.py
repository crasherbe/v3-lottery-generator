from collections import Counter

# ==========================================
# ANALYZER
# ==========================================
# menghitung digit frequency, hot/cold/normal
# dan strategi tambahan:
# Last Draw Weight, Trend, Skip, Digit Pair, Mirror
# ==========================================

from strategy import LAST_DRAW_WEIGHT, MIRROR_MAP

def analyze_history(history):
    """
    history: list of strings, setiap angka satu baris
    """
    digits = []
    pairs = []
    trend_counter = Counter()
    
    # hitung frequency dengan bobot last draw
    for i,num in enumerate(history):
        weight = 1
        if i == len(history)-1:
            weight = LAST_DRAW_WEIGHT
        for d in num:
            digits.extend([d]*weight)
            trend_counter[d] += weight
        # hitung digit pair frequency
        for j in range(len(num)-1):
            pair = (num[j], num[j+1])
            pairs.append(pair)
    
    freq = Counter(digits)
    sorted_digits = sorted(freq.items(), key=lambda x:x[1], reverse=True)
    
    # Hot / Cold / Normal
    hot = [x[0] for x in sorted_digits[:3]]
    cold = [x[0] for x in sorted_digits[-3:]]
    normal = [x[0] for x,_ in sorted_digits[3:-3]]
    
    # Mirror digit
    mirror_digits = [MIRROR_MAP[d] for d in hot]
    
    # Trend digit
    trend = [d for d,count in trend_counter.items() if count >= 2]  # contoh threshold
    
    # Skip digit
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
