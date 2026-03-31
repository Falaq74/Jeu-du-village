import streamlit as st

st.set_page_config(page_title="Mon Village Familial", page_icon="🏘️")

# Style pour le rendu final
st.markdown("""
    <style>
    .main { background-color: #fdfcfb; }
    h1 { color: #d35400; text-align: center; }
    .stButton>button { background-color: #d35400; color: white; border-radius: 20px; }
    .village-card { border: 3px dashed #d35400; padding: 15px; border-radius: 15px; background-color: white; }
    </style>
    """, unsafe_allow_index=True)

st.title("🏘️ Crée ton Village !")

# --- ETAPE 1 : L'AMBIANCE ---
st.subheader("🌟 L'ambiance du Village")
nom_v = st.text_input("Nom du Village", placeholder="Ex: La Cité du Rire")
lieu = st.text_input("Où se trouve-t-il ?", placeholder="Ex: Sur un nuage, Dans une forêt...")
slogan = st.text_input("Le Slogan", placeholder="Ex: Ici, on mange, on rit !")
plat = st.text_input("Le Plat Signature", placeholder="Ex: Les crêpes de mamie")
super_pouvoir = st.text_input("Le Super-Pouvoir du Village", placeholder="Ex: Tout le monde fait la sieste à 14h")

# --- ETAPE 2 : L'IMAGE ---
st.subheader("📸 Photo d'ambiance")
image_file = st.file_uploader("Ajoute une image pour illustrer ton village", type=["jpg", "jpeg", "png"])

# --- ETAPE 3 : LES FONDATEURS (SAISIE LIBRE) ---
st.subheader("👥 Tes 5 Fondateurs")
st.info("Tape le nom de qui tu veux (Maman, Grand-père, Ton chat...)")

fondateurs_data = []
for i in range(1, 6):
    col_n, col_r = st.columns([1, 2])
    with col_n:
        nom_f = st.text_input(f"Nom {i}", key=f"n{i}", placeholder="Prénom")
    with col_r:
        raison_f = st.text_input(f"Pourquoi ?", key=f"r{i}", placeholder="Sa qualité principale...")
    fondateurs_data.append((nom_f, raison_f))

# --- GENERATION ---
if st.button("✨ FONDE TON VILLAGE !"):
    if nom_v:
        st.balloons()
        
        # Affichage du résultat
        st.markdown(f"<div class='village-card'>", unsafe_allow_index=True)
        st.header(f"📜 {nom_v}")
        
        # Affichage de l'image si elle existe
        if image_file is not None:
            st.image(image_file, caption=f"Bienvenue à {nom_v} !", use_column_width=True)
            
        st.write(f"📍 **Lieu :** {lieu}")
        st.write(f"📢 **Slogan :** *{slogan}*")
        st.write(f"🍲 **Spécialité :** {plat}")
        st.write(f"⚡ **Super-Pouvoir :** {super_pouvoir}")
        st.write("---")
        st.write("### 👥 Le Conseil des Fondateurs")
        
        for n, r in fondateurs_data:
            if n: # N'affiche que si un nom est rempli
                st.write(f"**{n}** : {r}")
        st.markdown("</div>", unsafe_allow_index=True)
        
        st.success("📸 Fais une capture d'écran et envoie-la sur WhatsApp !")
    else:
        st.error("Il manque le nom de ton village !")
