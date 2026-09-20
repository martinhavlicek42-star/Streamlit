from datetime import datetime
import pandas as pd
import streamlit as st

# Nastavení stránky
st.set_page_config(
    page_title="Můj Webový Kalendář", page_icon="📅", layout="centered"
)

st.title("📅 Osobní plánovač a kalendář")
st.write("Jednoduchá webová aplikace napsaná v čistém Pythonu.")

# Uložení událostí do paměti (Session State)
if "udalosti" not in st.session_state:
    st.session_state.udalosti = []

st.divider()

# --- FORMULÁŘ PRO PŘIDÁNÍ UDÁLOSTI ---
st.subheader("➕ Přidat novou událost")

with st.form("kalendar_form", clear_on_submit=True):
    col1, col2 = st.columns(2)

    with col1:
        datum = st.date_input("Vyberte datum", datetime.now())
        cas = st.time_input("Vyberte čas", datetime.now().time())

    with col2:
        nazev = st.text_input("Název události", placeholder="např. Porada")
        priorita = st.selectbox(
            "Priorita", ["Nízká 🟢", "Střední 🟡", "Vysoká 🔴"]
        )

    odeslano = st.form_submit_button("Uložit do kalendáře")

    if odeslano:
        if nazev.strip() == "":
            st.error("Vyplňte prosím název události!")
        else:
            # Uložení nové události do seznamu
            nova_udalost = {
                "Datum": datum.strftime("%d.%m.%Y"),
                "Čas": cas.strftime("%H:%M"),
                "Událost": nazev,
                "Priorita": priorita,
            }
            st.session_state.udalosti.append(nova_udalost)
            st.success(f"Událost **'{nazev}'** byla úspěšně přidána!")

st.divider()

# --- ZOBRAZENÍ PLÁNOVANÝCH UDÁLOSTÍ ---
st.subheader("📋 Vaše plánované události")

if len(st.session_state.udalosti) == 0:
    st.info("Zatím nemáte naplánované žádné události.")
else:
    # Převod dat na tabulku přes Pandas
    df = pd.DataFrame(st.session_state.udalosti)
    st.dataframe(df, use_container_width=True)

    # Tlačítko pro vymazání paměti
    if st.button("🗑️ Smazat všechny události"):
        st.session_state.udalosti = []
        st.rerun()
