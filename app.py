import streamlit as st
from analyzer import analyze_history
from generator import generate_numbers
from predictor import pick_best
import random

st.title("LOTTERY HISTORY ANALYZER")

st.markdown("""
Tool ini digunakan untuk **menganalisa history angka**.

Strategi digunakan:

- Digit Frequency  
- Hot Digit  
- Cold Digit  
- Normal Digit  
- Mirror Digit  
- Trend Digit  
- Skip Digit  
- Digit Pair Frequency  
- Ganjil/Genap  
- Besar/Kecil  
- Generate Kombinasi  
- Ranking Score  
- Top 10 Prediksi Angka
""")

st.markdown("""
### Legend Warna
🟥 Merah = Hot Digit  
🟦 Biru = Cold Digit  
⬜ Abu = Normal Digit  
🟢 Hijau terang = Top 10 angka terbaik
""")

history_text = st.text_area("Input History Angka (satu baris per angka)")
digit_count = st.selectbox("Pilih Digit", [2,3,4,5])
generate_count = st.selectbox("Jumlah Generate", [50,100,200,500])

if st.button("ANALYZE"):
    history = history_text.split()
    
    # --------------------------
    # Kotak 1: Tampilkan input user
    # --------------------------
    st.subheader("Input History User")
    cols_input = st.columns(10)
    for i, num in enumerate(history):
        cols_input[i%10].markdown(f"<span style='color:black;font-weight:bold'>{num}</span>", unsafe_allow_html=True)
    
    # --------------------------
    # Analisa history
    # --------------------------
    analysis = analyze_history(history)
    
    # --------------------------
    # Generate angka berbasis analisa
    # --------------------------
    numbers = []
    for _ in range(generate_count):
        combo = []
        pool = analysis["hot"]*3 + analysis["cold"]*2 + analysis["normal"] + analysis["mirror"] + analysis["trend"]
        while len(combo) < digit_count:
            combo.append(random.choice(pool))
        random.shuffle(combo)
        numbers.append("".join(combo))
    
    top10 = pick_best(numbers, analysis)
    
    # --------------------------
    # Kotak 2: Hasil Generator dengan warna Top 10 sinkron
    # --------------------------
    st.subheader("Hasil Generator")
    cols = st.columns(10)
    for i, num in enumerate(numbers):
        colored_num = ""
        for d in num:
            if num in top10:
                colored_num += f"<span style='color:lime;font-weight:bold'>{d}</span>"
            elif d in analysis["hot"]:
                colored_num += f"<span style='color:red;font-weight:bold'>{d}</span>"
            elif d in analysis["cold"]:
                colored_num += f"<span style='color:blue'>{d}</span>"
            else:
                colored_num += f"<span style='color:gray'>{d}</span>"
        cols[i%10].markdown(colored_num, unsafe_allow_html=True)
    
    # --------------------------
    # Kotak 3: Top 10 Terbaik
    # --------------------------
    st.subheader("Top 10 Angka Terbaik")
    top_cols = st.columns(10)
    for i,n in enumerate(top10):
        colored_num = ""
        for d in n:
            colored_num += f"<span style='color:lime;font-weight:bold'>{d}</span>"
        top_cols[i%10].markdown(colored_num, unsafe_allow_html=True)
    
    # --------------------------
    # Kotak 4: Analisa Digit
    # --------------------------
    st.subheader("Analisa Digit")
    st.markdown(f"**Digit Frequency:** {analysis['frequency']}")
    st.markdown(f"**Hot Digit:** {analysis['hot']}")
    st.markdown(f"**Cold Digit:** {analysis['cold']}")
    st.markdown(f"**Normal Digit:** {analysis['normal']}")
    st.markdown(f"**Mirror Digit:** {analysis['mirror']}")
    st.markdown(f"**Trend Digit:** {analysis['trend']}")
    st.markdown(f"**Skip Digit:** {analysis['skip']}")
    st.markdown(f"**Digit Pair Frequency:** {analysis['pairs']}")
    
st.warning("Warning: sistem ini hanya analisa statistik dari history angka dan tidak menjamin hasil pasti keluar.")
