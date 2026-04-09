import streamlit as st

# 1. Configuración de página
st.set_page_config(page_title="Bazán Atelier | Tienda", page_icon="👗", layout="wide")

# 2. CSS de Lujo
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lato:wght@300;400&display=swap');
    .main { background-color: #fdfaf7; }
    h1 { font-family: 'Playfair Display', serif; color: #5d4037; text-align: center; font-size: 3.5rem !important; }
    .stButton>button { width: 100%; border-radius: 12px; font-weight: bold; }
    /* Estilo para los botones de filtro */
    div[data-testid="stHorizontalBlock"] button {
        background-color: white !important;
        color: #5d4037 !important;
        border: 1px solid #d7ccc8 !important;
    }
    div[data-testid="stHorizontalBlock"] button:hover {
        border-color: #5d4037 !important;
        background-color: #f5f5f5 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar con Botón de Mapas
with st.sidebar:
    st.image("logo.jpg", width=220)
    st.title("Bazán Atelier")
    st.write("✨ *Diseño de autor en Lima*")
    
    st.markdown("---")
    st.write("📍 **Ubicación:**")
    # SUSTITUYE este link por la dirección real de Google Maps de tu prima
    st.link_button("📍 Ver en Google Maps", "https://goo.gl/maps/ejemplo_lima")
    
    st.markdown("---")
    st.info("📦 **Envíos:** Lima y todo el Perú vía Olva o Shalom.")

# 4. Títulos
st.markdown("<h1>Bazán Atelier</h1>", unsafe_allow_html=True)
st.write("---")

# 5. LÓGICA DE FILTROS (Toque Tecnológico)
st.markdown("<h3 style='text-align: center;'>Explora nuestra colección</h3>", unsafe_allow_html=True)
categoria = st.radio("", ["Ver Todo", "Tops", "Pantalones", "Vestidos"], horizontal=True)

st.write("") # Espacio

# 6. Base de datos de productos (Simulada para que el filtro funcione)
# Esto es escalable: cuando ella te pase más fotos, solo añadimos líneas aquí
productos = [
    {"nombre": "Top Seda Marfil", "precio": "S/ 95", "cat": "Tops", "img": "https://images.unsplash.com/photo-1434389677669-e08b4cac3105?q=80&w=500", "wa": "Top%20Seda%20Marfil"},
    {"nombre": "Pantalón Sastrero Arena", "precio": "S/ 140", "cat": "Pantalones", "img": "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?q=80&w=500", "wa": "Pantalón%20Sastrero%20Arena"},
]

# Filtrar productos según la elección
productos_filtrados = [p for p in productos if categoria == "Ver Todo" or p["cat"] == categoria]

# 7. Mostrar productos en cuadrícula
if not productos_filtrados:
    st.warning(f"Próximamente más modelos en la categoría: {categoria}")
else:
    cols = st.columns(2)
    for i, p in enumerate(productos_filtrados):
        with cols[i % 2]:
            st.image(p["img"])
            st.subheader(p["nombre"])
            st.markdown(f"**{p['precio']}**")
            link_wa = f"https://wa.me/51937395562?text=Hola!%20Me%20interesa%20el%20{p['wa']}"
            st.link_button(f"Consultar {p['nombre']}", link_wa)

st.write("---")
st.markdown("<p style='text-align: center; color: #bcaaa4;'>© 2026 Bazán Atelier | Lima, Perú</p>", unsafe_allow_html=True)