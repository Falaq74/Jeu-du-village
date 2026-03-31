import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Mon Village Familial", page_icon="🏘️", layout="centered")

# Style pour rendre l'interface plus jolie
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    h1 { color: #2E7D32; text-align: center; font-size: 28px; }
    .stButton>button { background-color: #2E7D32; color: white; width: 100%; border-radius: 10px; }
    .stSelectbox label, .stTextInput label, .stTextArea label { font-weight: bold; color: #1B5E20; }
    </style>
    """, unsafe_allow_index=True)

st.title("🏘️ Construis ton Village")
st.write("Remplissez les informations ci-dessous pour fonder votre communauté.")

# --- SECTION 1 : IDENTITÉ DU VILLAGE ---
st.subheader("📍 Identité et Culture")
with st.container():
    nom_village = st.text_input("Nom du Village", placeholder="Ex: Le Havre de Paix")
    
    col1, col2 = st.columns(2)
    with col1:
        lieu = st.text_input("Lieu Géographique", placeholder="Ex: Une plaine fertile")
        slogan = st.text_input("Slogan / Devise", placeholder="Ex: L'union fait la force")
    with col2:
        plat = st.text_input("Plat de Bienvenue", placeholder="Ex: Le couscous familial")
        valeur = st.text_input("Valeur d'entraide", placeholder="Ex: L'hospitalité")

# --- SECTION 2 : LES FONDATEURS ---
st.markdown("---")
st.subheader("
