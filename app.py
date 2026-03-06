# app.py
# -------------------------------------------------
# Web interface menggunakan Streamlit
# Menampilkan:
# - input history
# - analisa hot cold
# - generator kombinasi
# - top 10 angka terkuat
# -------------------------------------------------

import streamlit as st

from analyzer import analyze_history
from generator import generate_numbers
from predictor import get_top_numbers


st.title("Lottery Number Analyzer")

st.write("""
Strategi yang digunakan:

Hot Number → angka paling sering muncul
Cold Number → angka paling jarang muncul
Genap/Ganjil filter
Besar/Kecil filter
Generate kombinasi dari hasil analisa
Ranking kombinasi
""")

history_input = st.text_area("Masukkan history angka (pisahkan dengan enter)")

digits_length = st.selectbox(
    "Pilih tipe angka",
    [2,3,4,5]
)

generate_total = st.slider(
    "Jumlah angka generator",
    10,
    500,
    100
)

if st.button("Analisa dan Generate"):

    history_numbers = history_input.split()

    result = analyze_history(history_numbers)

    hot = result["hot"]
    cold = result["cold"]
    normal = result["normal"]

    st.write("Hot digits:", hot)
    st.write("Cold digits:", cold)

    numbers = generate_numbers(
        generate_total,
        digits_length,
        hot,
        cold,
        normal
    )

    st.subheader("Hasil Generator")

    cols = st.columns(5)

    for i, num in enumerate(numbers):
        cols[i % 5].write(num)

    st.subheader("Top 10 Angka Terkuat")

    top = get_top_numbers(numbers, hot, cold)

    for n, s in top:
        st.write(n, "score:", s)
