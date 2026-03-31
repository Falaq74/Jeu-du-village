import streamlit as st

st.set_page_config(page_title="Village Familial", page_icon="🏘️")

# Gestion de l'affichage (Formulaire ou Résultat)
if 'village_cree' not in st.session_state:
    st.session_state.village_cree = False

# --- 1. FORMULAIRE DE SAISIE ---
if not st.session_state.village_cree:
    st.title("🏘️ Crée ton Village !")
    
    nom_v = st.text_input("Nom du Village")
    col_a, col_b = st.columns(2)
    with col_a:
        lieu = st.text_input("Lieu")
        slogan = st.text_input("Slogan")
    with col_b:
        plat = st.text_input("Plat Signature")
        pouvoir = st.text_input("Super-Pouvoir")

    image_file = st.file_uploader("Ajoute une photo", type=["jpg", "png", "jpeg"])

    st.subheader("👥 Ton Conseil (5 Piliers)")
    liste_roles = ["🛡️ Le Protecteur", "🍳 Le Chef Cuistot", "📜 Le Sage", "🤝 Le Pacificateur", "🛠️ Le Bâtisseur", "🌿 Gardien de la Nature", "📖 L'Enseignant", "⚖️ Le Sage Arbitre", "🎨 L'Artiste", "🏹 Chasseur de Solutions"]

    fondateurs = []
    for i in range(1, 6):
        c1, col_vide = st.columns([1, 1])
        r = c1.selectbox(f"Rôle {i}", ["Choisir..."] + liste_roles, key=f"role{i}")
        n = st.text_input(f"Prénom {i}", key=f"n{i}")
        js = st.text_input(f"Pourquoi lui/elle ? ({i})", key=f"r{i}")
        fondateurs.append((r, n, js))

    if st.button("✨ GÉNÉRER MON VILLAGE"):
        if nom_v:
            st.session_state.data = {
                "nom": nom_v, "lieu": lieu, "slogan": slogan, 
                "plat": plat, "pouvoir": pouvoir, "img": image_file, "fondateurs": fondateurs
            }
            st.session_state.village_cree = True
            st.rerun()
        else:
            st.error("Donne un nom à ton village !")

# --- 2. AFFICHAGE FINAL (POUR CAPTURE) ---
else:
    d = st.session_state.data
    
    # Bouton discret pour revenir si besoin
    if st.button("⬅️ Modifier"):
        st.session_state.village_cree = False
        st.rerun()

    st.markdown(f"## 📜 {d['nom']}")
    
    if d['img']:
        st.image(d['img'], width=200) # Image petite pour tout faire tenir
        
    st.write(f"🌍 **{d['lieu']}** | 📢 *{d['slogan']}*")
    st.write(f"🍲 **Plat :** {d['plat']} | ⚡ **Pouvoir :** {d['pouvoir']}")
    st.write("---")
    
    # Affichage des rôles sans erreur
    for r, n, js in d['fondateurs']:
        if r != "Choisir..." and n:
            st.write(f"**{r}** : {n} - {js}")

    st.balloons()
    st.info("📸 Prends ta capture d'écran ! Le formulaire a été masqué pour plus de clarté.")
