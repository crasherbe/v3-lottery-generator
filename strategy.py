# STRATEGY MODULE
# Semua aturan strategi untuk generator
HOT_PICK = 1
COLD_PICK = 1
NORMAL_PICK = 2

SCORE_HOT = 3
SCORE_NORMAL = 2
SCORE_COLD = 1

ODD_EVEN_RULE = (2,2)  # 2 ganjil 2 genap
BIG_SMALL_RULE = (2,2)  # 2 besar 2 kecil

# Mirror mapping
MIRROR_MAP = {
    "0":"5","1":"6","2":"7","3":"8","4":"9",
    "5":"0","6":"1","7":"2","8":"3","9":"4"
}

LAST_DRAW_WEIGHT = 2  # bobot history terakhir
