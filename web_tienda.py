import streamlit as st

# Configuración de lujo
st.set_page_config(page_title="Bazán Atelier | Tienda", page_icon="👗", layout="wide")

# Estilo con CSS para que se vea más femenino y profesional
st.markdown("""
    <style>
    .main { background-color: #fdfaf7; }
    h1 { color: #5d4037; font-family: 'Playfair Display', serif; }
    .stButton>button { background-color: #d4a373; color: white; border-radius: 20px; }
    </style>
    """, unsafe_allow_html=True)

# Sidebar de contacto
# Sidebar de contacto con el LOGO REAL
with st.sidebar:
    st.image("logo.jpg", width=200) # Asegúrate de que el nombre coincida aquí
    st.title("Bazán Atelier")
    st.write("📍 Lima, Perú")
    st.write("📸 @bazan_atelier")
    st.write("---")
    st.info("Diseños exclusivos hechos a medida.")
    
# Cuerpo de la página
st.title("✨ Colección Bazán Atelier")
st.write("Explora nuestras prendas únicas diseñadas para resaltar tu esencia.")

col1, col2 = st.columns(2)

with col1:
    # Foto de un top elegante (ejemplo)
    st.image("https://images.unsplash.com/photo-1554520735-0ad6a9965344?q=80&w=500", use_container_width=True)
    st.subheader("Top Seda Marfil")
    st.write("**Precio:** S/ 95.00")
    url_wa = "https://wa.me/51937395562?text=Hola%20Bazán%20Atelier!%20Me%20encanta%20el%20Top%20Seda%20Marfil"
    st.link_button("Solicitar por WhatsApp 💬", url_wa)

with col2:
    # Foto de un pantalón/outfit (ejemplo)
    st.image("https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?q=80&w=500", use_container_width=True)
    st.subheader("Pantalón Sastrero Arena")
    st.write("**Precio:** S/ 140.00")
    url_wa2 = "https://wa.me/51937395562?text=Hola%20Bazán%20Atelier!%20Me%20gustaría%20el%20Pantalón%20Sastrero%20Arena"
    st.link_button("Solicitar por WhatsApp 💬", url_wa2)

st.write("---")
st.caption("© 2026 Bazán Atelier - Desarrollado por Adrián Chávez")