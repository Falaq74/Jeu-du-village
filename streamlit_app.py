import streamlit as st

st.title("🏘️ Crée ton Village !")

# --- INFOS DU VILLAGE ---
nom_v = st.text_input("Nom du Village")
lieu = st.text_input("Où se trouve-t-il ?")
slogan = st.text_input("Le Slogan")
plat = st.text_input("Le Plat Signature")
pouvoir = st.text_input("Le Super-Pouvoir du Village")

# --- L'IMAGE ---
image_file = st.file_uploader("Ajoute une image", type=["jpg", "png", "jpeg"])

# --- LES 5 FONDATEURS ---
st.subheader("👥 Tes 5 Fondateurs")
f1 = st.text_input("Fondateur 1 (Nom)")
r1 = st.text_input("Pourquoi lui/elle ? (1)")

f2 = st.text_input("Fondateur 2 (Nom)")
r2 = st.text_input("Pourquoi lui/elle ? (2)")

f3 = st.text_input("Fondateur 3 (Nom)")
r3 = st.text_input("Pourquoi lui/elle ? (3)")

f4 = st.text_input("Fondateur 4 (Nom)")
r4 = st.text_input("Pourquoi lui/elle ? (4)")

f5 = st.text_input("Fondateur 5 (Nom)")
r5 = st.text_input("Pourquoi lui/elle ? (5)")

# --- BOUTON FINAL ---
if st.button("✨ GÉNÉRER MA FICHE"):
    if nom_v:
        st.header(f"📜 Village : {nom_v}")
        if image_file:
            st.image(image_file)
        st.write(f"📍 Lieu : {lieu}")
        st.write(f"📢 Slogan : {slogan}")
        st.write(f"🍲 Plat : {plat}")
        st.write(f"⚡ Super-Pouvoir : {pouvoir}")
        st.write("---")
        st.write(f"1. **{f1}** : {r1}")
        st.write(f"2. **{f2}** : {r2}")
        st.write(f"3. **{f3}** : {r3}")
        st.write(f"4. **{f4}** : {r4}")
        st.write(f"5. **{f5}** : {r5}")
        st.balloons()
    else:
        st.error("Mets au moins un nom de village !")
