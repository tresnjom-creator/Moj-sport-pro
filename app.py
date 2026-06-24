import streamlit as st

# Postavke stranice
st.set_page_config(page_title="Moja aplikacija", layout="wide")

st.title("Dobrodošli u aplikaciju")

# Ovdje je ispravljen kod za liniju 11
# Koristimo f-string za ispis poruke
modul_naziv = "Analitika"
st.success(f"Sistem spreman za modul: {modul_naziv}")

# Ostatak vašeg koda...
st.write("Ovdje možete dodati dodatni sadržaj.")
