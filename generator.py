# generator.py
# ----------------------------------------------------
# File ini membuat kombinasi angka berdasarkan hasil
# analisa history (hot / cold / normal)
# BUKAN random dari 0-9
# ----------------------------------------------------

import random


def generate_number(digits_length, hot, cold, normal):

    digits = []

    # Strategi kombinasi
    # 1 HOT
    # 1 COLD
    # sisanya NORMAL

    digits.append(random.choice(hot))
    digits.append(random.choice(cold))

    while len(digits) < digits_length:
        digits.append(random.choice(normal))

    random.shuffle(digits)

    return "".join(map(str, digits))


def generate_numbers(total, digits_length, hot, cold, normal):

    numbers = []

    for _ in range(total):

        num = generate_number(
            digits_length,
            hot,
            cold,
            normal
        )

        numbers.append(num)

    return numbers
