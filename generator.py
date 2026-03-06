import random
from strategy import HOT_PICK,COLD_PICK,NORMAL_PICK

def generate_numbers(analysis, digit_count, total_count):
    hot = analysis["hot"]
    cold = analysis["cold"]
    normal = analysis["normal"]
    mirror = analysis["mirror"]
    trend = analysis["trend"]
    
    numbers = []
    for _ in range(total_count):
        combo = []
        if len(hot) >= HOT_PICK:
            combo += random.sample(hot,HOT_PICK)
        if len(cold) >= COLD_PICK:
            combo += random.sample(cold,COLD_PICK)
        if len(normal) >= NORMAL_PICK:
            combo += random.sample(normal,NORMAL_PICK)
        while len(combo) < digit_count:
            options = normal + trend + mirror
            combo.append(random.choice(options))
        random.shuffle(combo)
        numbers.append("".join(combo))
    return numbers
