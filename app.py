import streamlit as st
import google.generativeai as genai

# Konfiguracija stranice
st.set_page_config(page_title="Pro Sport Analitika", page_icon="⚽")
st.title("Napredna Sportska Analitika")
st.write("Unesi podatke o utakmicama za statističku i energetsku obradu.")

# Povlačenje API ključa iz Streamlit tajni (Secrets)
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# Zadavanje sistemske instrukcije (OVO SPREČAVA BLOKADE!)
sistemska_uputa = """
Ti si vrhunski sportski analitičar i statističar. 
Tvoj isključivi zadatak je obrada sportskih podataka, analiza ofanzivnog potencijala (poput '3+ golova' u fudbalu ili prebacivanja margina poena u košarci). 
Fokusiraj se isključivo na brojeve, formu, taktiku i energetski potencijal meča. Nemoj spominjati klađenje, tikete niti davati finansijske savjete. Budi direktan i precizan u analizi svake unesene utakmice.
"""

# Inicijalizacija modela sa uputama
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=sistemska_uputa
)

# Interfejs za unos podataka
uneseni_podaci = st.text_area("Unesi parove ili sirovu statistiku za analizu (npr. spisak 20 parova, margine za over):", height=200)

if st.button("Analiziraj Podatke"):
    if uneseni_podaci:
        with st.spinner("Obrada podataka u toku..."):
            try:
                # Slanje podataka modelu
                odgovor = model.generate_content(uneseni_podaci)
                st.markdown("### Rezultat Analize:")
                st.write(odgovor.text)
            except Exception as e:
                st.error(f"Došlo je do greške u komunikaciji sa AI modelom: {e}")
    else:
        st.warning("Molim te unesi podatke za analizu u polje iznad.")
