import streamlit as st
from analyzer import analyze_history
from generator import generate_numbers
from predictor import pick_best

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
🟩 Hijau = Hot Digit  
🟦 Biru = Cold Digit  
⬜ Abu = Normal Digit  
🟢 Hijau terang = Top 10 angka terbaik
""")

history_text = st.text_area("Input History Angka (satu baris per angka)")
digit_count = st.selectbox("Pilih Digit", [2,3,4,5])
generate_count = st.selectbox("Jumlah Generate", [50,100,200,500])

if st.button("ANALYZE"):
    history = history_text.split()
    analysis = analyze_history(history)
    numbers = generate_numbers(analysis, digit_count, generate_count)
    top10 = pick_best(numbers, analysis)
    
    st.subheader("Digit Frequency")
    st.write(analysis["frequency"])
    st.subheader("Hot Digit")
    st.write(analysis["hot"])
    st.subheader("Cold Digit")
    st.write(analysis["cold"])
    st.subheader("Normal Digit")
    st.write(analysis["normal"])
    st.subheader("Mirror Digit")
    st.write(analysis["mirror"])
    st.subheader("Trend Digit")
    st.write(analysis["trend"])
    st.subheader("Skip Digit")
    st.write(analysis["skip"])
    st.subheader("Digit Pair Frequency")
    st.write(analysis["pairs"])
    
    st.subheader("Top 10 Prediksi")
    st.write(top10)
    
    st.subheader("Hasil Generator (Grid)")
    cols = st.columns(10)
    for i,num in enumerate(numbers):
        cols[i%10].write(num)

st.warning("Warning: sistem ini hanya analisa statistik dari history angka dan tidak menjamin hasil pasti keluar.")
