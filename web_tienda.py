import streamlit as st

# 1. Configuración de página
st.set_page_config(page_title="Bazán Atelier | Tienda", page_icon="👗", layout="wide")

# 2. CSS de Lujo (Diseño Premium)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lato:wght@300;400&display=swap');
    .main { background-color: #fdfaf7; }
    h1 { font-family: 'Playfair Display', serif; color: #5d4037; text-align: center; font-size: 3.5rem !important; }
    
    /* Botones de producto */
    .stButton>button { width: 100%; border-radius: 12px; font-weight: bold; background-color: #25D366 !important; color: white !important; border: none; }
    
    /* Botones de filtro */
    div[data-testid="stHorizontalBlock"] button {
        background-color: white !important;
        color: #5d4037 !important;
        border: 1px solid #d7ccc8 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar (Barra Lateral) RECOMPUESTA
with st.sidebar:
    st.image("logo.jpg", width=220)
    st.title("Bazán Atelier")
    st.write("✨ *Diseño de autor en Lima*")
    
    st.markdown("---")
    # RECUPERADO: Link de Instagram
    st.write("📸 **IG:** [@bazan_atelier](https://www.instagram.com/bazan_atelier/)")
    
    st.markdown("---")
    st.write("📍 **Ubicación:**")
    st.link_button("📍 Ver en Google Maps", "https://goo.gl/maps/ejemplo_lima")
    
    st.markdown("---")
    st.info("📦 **Envíos:** Lima y todo el Perú vía Olva o Shalom.")
    st.write("---")
    st.write("© 2026 Bazán Atelier")

# 4. Cuerpo Principal
st.markdown("<h1>Bazán Atelier</h1>", unsafe_allow_html=True)
st.write("---")

# RECUPERADO: Frase verde de promoción
st.success("✨ **LANZAMIENTO WEB:** Usa el código **BAZAN10** y obtén un descuento especial en tu primer pedido.")

# 5. Filtros Interactivos
st.markdown("<h3 style='text-align: center;'>Explora nuestra colección</h3>", unsafe_allow_html=True)
categoria = st.radio("", ["Ver Todo", "Tops", "Pantalones", "Vestidos"], horizontal=True)

st.write("") 

# 6. Catálogo (Base de datos)
productos = [
    {"nombre": "Top Seda Marfil", "precio": "S/ 95", "cat": "Tops", "img": "https://images.unsplash.com/photo-1434389677669-e08b4cac3105?q=80&w=500", "wa": "Top%20Seda%20Marfil"},
    {"nombre": "Pantalón Sastrero Arena", "precio": "S/ 140", "cat": "Pantalones", "img": "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?q=80&w=500", "wa": "Pantalón%20Sastrero%20Arena"},
]

# Lógica de filtrado
productos_filtrados = [p for p in productos if categoria == "Ver Todo" or p["cat"] == categoria]

# 7. Mostrar productos
if not productos_filtrados:
    st.warning(f"Próximamente más modelos en la categoría: {categoria}")
else:
    cols = st.columns(2, gap="large")
    for i, p in enumerate(productos_filtrados):
        with cols[i % 2]:
            st.image(p["img"], use_container_width=True)
            st.subheader(p["nombre"])
            st.markdown(f"**{p['precio']}**")
            link_wa = f"https://wa.me/51937395562?text=Hola!%20Me%20interesa%20el%20{p['wa']}"
            st.link_button(f"Pedir {p['nombre']} 💬", link_wa)

st.write("---")
st.markdown("<p style='text-align: center; color: #bcaaa4;'>Desarrollado por Adrián Chávez - Ing. de Sistemas</p>", unsafe_allow_html=True)