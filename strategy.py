# ==========================================
# STRATEGY MODULE
# ==========================================
# Semua aturan strategi untuk generator
# ==========================================

# Jumlah digit dari tiap kategori
HOT_PICK = 1
COLD_PICK = 1
NORMAL_PICK = 2

# Skor ranking
SCORE_HOT = 3
SCORE_NORMAL = 2
SCORE_COLD = 1

# Ganjil/Genap default
ODD_EVEN_RULE = (2,2)  # contoh 2 ganjil 2 genap

# Besar/Kecil default
BIG_SMALL_RULE = (2,2)  # contoh 2 besar 2 kecil

# Mirror digit mapping
MIRROR_MAP = {
    "0":"5", "1":"6", "2":"7", "3":"8", "4":"9",
    "5":"0", "6":"1", "7":"2", "8":"3", "9":"4"
}

# Last draw weight
LAST_DRAW_WEIGHT = 2  # bobot history terakhir
