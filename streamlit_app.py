import streamlit as st

st.set_page_config(page_title="Village Familial", page_icon="🏘️")

st.title("🏘️ Construis ton Village")
st.write("Créez l'identité de votre village et choisissez vos 5 fondateurs.")

# Identité
st.subheader("📍 Identité")
nom_v = st.text_input("Nom du Village")
lieu = st.text_input("Lieu")
slogan = st.text_input("Slogan")
plat = st.text_input("Plat typique")
valeur = st.text_input("Valeur d'entraide")

# Fondateurs
st.subheader("👥 Les 5 Fondateurs")
famille = ["Choisir...", "Maman", "Papa", "Youssef", "Sami", "Leila", "Inès", "Oncle Ali", "Tante Nora"]

choix_fondateurs = []
for i in range(1, 6):
    c = st.selectbox(f"Membre {i}", famille, key=f"m{i}")
    r = st.text_area(f"Pourquoi {c} ?", key=f"r{i}", height=70)
    choix_fondateurs.append((c, r))

# Bouton
if st.button("🌟 GÉNÉRER MA FICHE"):
    if nom_v:
        st.markdown(f"### 📜 Village : {nom_v}")
        st.write(f"**Lieu :** {lieu} | **Slogan :** {slogan}")
        st.write(f"**Plat :** {plat} | **Valeur :** {valeur}")
        st.write("---")
        for f, res in choix_fondateurs:
            if f != "Choisir...":
                st.write(f"**{f}** : {res}")
        st.balloons()
    else:
        st.error("Donnez un nom au village !")
