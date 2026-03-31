import streamlit as st

st.set_page_config(page_title="Village Familial", page_icon="🏘️")

# On crée une variable pour savoir si on affiche le formulaire ou le résultat
if 'village_cree' not in st.session_state:
    st.session_state.village_cree = False

# --- SI LE VILLAGE N'EST PAS ENCORE CRÉÉ, ON AFFICHE LE FORMULAIRE ---
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

    st.subheader("👥 Choisis tes 5 Piliers")
    liste_roles = ["🛡️ Le Protecteur", "🍳 Le Chef Cuistot", "📜 Le Sage", "🤝 Le Pacificateur", "🛠️ Le Bâtisseur", "🌿 Gardien de la Nature", "📖 L'Enseignant", "⚖️ Le Sage Arbitre", "🎨 L'Artiste", "🏹 Chasseur de Solutions"]

    fondateurs = []
    for i in range(1, 6):
        c1, c2 = st.columns([1.2, 1.5])
        with c1:
            r = st.selectbox(f"Rôle {i}", ["Choisir..."] + liste_roles, key=f"role{i}")
        with c2:
            n = st.text_input(f"Prénom {i}", key=f"n{i}")
        js = st.text_input(f"Pourquoi ?", key=f"r{i}")
        fondateurs.append((r, n, js))

    if st.button("✨ GÉNÉRER MON VILLAGE"):
        if nom_v:
            # On enregistre les données pour les afficher après
            st.session_state.data = {
                "nom": nom_v, "lieu": lieu, "slogan": slogan, 
                "plat": plat, "pouvoir": pouvoir, "img": image_file, "fondateurs": fondateurs
            }
            st.session_state.village_cree = True
            st.rerun()
        else:
            st.error("Donne un nom à ton village !")

# --- SI LE VILLAGE EST CRÉÉ, ON N'AFFICHE QUE LE RÉSULTAT ---
else:
    d = st.session_state.data
    st.balloons()
    
    # Bouton pour revenir en arrière si on veut modifier
    if st.button("⬅️ Modifier mon village"):
        st.session_state.village_cree = False
        st.rerun()

    st.markdown(f"## 📜 {d['nom']}")
    
    if d['img']:
        st.image(d['img'], width=250)
        
    st.write(f"🌍 **{d['lieu']}** | 📢 *{d['slogan']}*")
    st.write(f"🍲 **Plat :** {d['plat']} | ⚡ **Pouvoir :** {d['pouvoir']}")
    st.write("---")
    
    for r, n, js in d['fondateurs']:
        if r != "Choisir..." and n:
            st.write(f"**{r}** : {n} - {rs}")

    st.info("📸 Prends ta capture d'écran maintenant ! Tout le reste a été masqué pour toi.")
