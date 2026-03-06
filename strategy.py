# strategy.py
# ---------------------------------------------
# File ini berisi aturan strategi analisa
# Digunakan untuk filter kombinasi angka
# ---------------------------------------------

def odd_even_filter(number):

    digits = [int(d) for d in number]

    odd = sum(d % 2 for d in digits)
    even = len(digits) - odd

    return odd, even


def big_small_filter(number):

    digits = [int(d) for d in number]

    small = sum(d <= 4 for d in digits)
    big = len(digits) - small

    return big, small
