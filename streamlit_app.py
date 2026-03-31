import streamlit as st

st.set_page_config(page_title="Village Familial", page_icon="🏘️")

st.title("🏘️ Crée ton Village !")

# --- INFOS DU VILLAGE ---
nom_v = st.text_input("Nom du Village")
col_a, col_b = st.columns(2)
with col_a:
    lieu = st.text_input("Lieu")
    slogan = st.text_input("Slogan")
with col_b:
    plat = st.text_input("Plat Signature")
    pouvoir = st.text_input("Super-Pouvoir")

# --- L'IMAGE ---
image_file = st.file_uploader("Ajoute une photo", type=["jpg", "png", "jpeg"])

# --- LES 10 RÔLES ---
st.subheader("👥 Choisis tes 5 Piliers")
st.info("Sélectionne un rôle différent pour chaque personne.")

liste_roles = [
    "🛡️ Le Protecteur", 
    "🍳 Le Chef Cuistot", 
    "📜 Le Sage (Conseils)", 
    "🤝 Le Pacificateur", 
    "🛠️ Le Bâtisseur",
    "🌿 Gardien de la Nature",
    "📖 L'Enseignant",
    "⚖️ Le Sage Arbitre",
    "🎨 L'Artiste",
    "🏹 Chasseur de Solutions"
]

choix_final = []
for i in range(1, 6):
    col1, col2 = st.columns([1.2, 1.5])
    with col1:
        role_choisi = st.selectbox(f"Rôle {i}", ["Choisir..."] + liste_roles, key=f"role{i}")
    with col2:
        nom_f = st.text_input(f"Prénom {i}", key=f"n{i}")
    raison_f = st.text_input(f"Pourquoi lui/elle ?", key=f"r{i}")
    choix_final.append((role_choisi, nom_f, raison_f))

# --- BOUTON GÉNÉRATION ---
if st.button("✨ GÉNÉRER MA FICHE"):
    if nom_v:
        st.markdown(f"### 📜 {nom_v}")
        
        if image_file:
            st.image(image_file, width=180) # Encore plus compact pour la capture
            
        st.write(f"🌍 **{lieu}** | 📢 *{slogan}*")
        st.write(f"🍲 **Plat :** {plat} | ⚡ **Pouvoir :** {pouvoir}")
        st.write("---")
        
        # Affichage très serré pour tout faire tenir
        for r, n, rs in choix_final:
            if r != "Choisir..." and n:
                st.write(f"**{r}** : {n} - {rs}")
        
        st.balloons()
    else:
        st.error("Donne un nom à ton village !")
