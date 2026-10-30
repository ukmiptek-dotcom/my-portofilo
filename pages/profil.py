import streamlit as st
st.write("ini adalah halaman profil")

st.title("Profil saya")

col1, col2, col3, col4 = st.columns([1, 2, 3, 4])

with col1:
    st.image("pages/beckam.jpg", width=200)

with col2:
    st.write("Nama saya adalah david Beckam. Saya berasal dari inggris. Profesi Saya adalah pemain bola profesional ")

with col3:
    st.video("https://www.youtube.com/watch?v=DQHF8idOXcY")

with col4:
    st.write("kemampuan bahasa inggris")
    st.progress(70)
    st.write("Kemampuan bahasa pemrograman")
    st.progress(90)
    st.write("kemampuan komunikasi")
    st.progress(100)


     