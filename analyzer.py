# analyzer.py
# ---------------------------------------------
# File ini bertugas membaca history angka dari user
# lalu menghitung frekuensi digit 0-9
# dan menentukan kategori:
# HOT  = paling sering muncul
# COLD = paling jarang muncul
# NORMAL = sisanya
# ---------------------------------------------

from collections import Counter

def analyze_history(history_numbers):

    # Menggabungkan semua digit dari history
    digits = []
    for number in history_numbers:
        for d in str(number):
            digits.append(int(d))

    # Hitung frekuensi digit
    freq = Counter(digits)

    # Pastikan digit 0-9 ada semua
    for i in range(10):
        if i not in freq:
            freq[i] = 0

    # Urutkan berdasarkan frekuensi
    sorted_digits = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # HOT = 3 digit teratas
    hot = [d[0] for d in sorted_digits[:3]]

    # COLD = 3 digit terbawah
    cold = [d[0] for d in sorted_digits[-3:]]

    # NORMAL = sisanya
    normal = [d for d in range(10) if d not in hot and d not in cold]

    return {
        "frequency": freq,
        "hot": hot,
        "cold": cold,
        "normal": normal
    }
