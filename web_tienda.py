import streamlit as st

# 1. Configuración de pestaña y página
st.set_page_config(
    page_title="Bazán Atelier | Tienda Oficial", 
    page_icon="👗", 
    layout="wide"
)

# 2. CSS de Lujo (Diseño Premium y Minimalista)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lato:wght@300;400&display=swap');
    
    .main { background-color: #fdfaf7; }
    
    /* Títulos con fuente de diseñador */
    h1 { 
        font-family: 'Playfair Display', serif; 
        color: #5d4037; 
        text-align: center; 
        font-size: 3.5rem !important; 
        margin-bottom: 0px;
    }
    
    /* Tarjetas de productos */
    div[data-testid="stColumn"] {
        background-color: white;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.02);
        border: 1px solid #f1ece7;
        transition: transform 0.3s ease;
    }
    div[data-testid="stColumn"]:hover { transform: translateY(-5px); }

    /* Botones de WhatsApp */
    .stButton>button { 
        width: 100%; 
        border-radius: 12px; 
        font-weight: bold; 
        background-color: #25D366 !important; 
        color: white !important; 
        border: none;
        padding: 10px;
    }
    
    /* Estilo para los radio buttons de categorías */
    div[role="radiogroup"] {
        display: flex;
        justify-content: center;
        gap: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar (Información de la Marca)
with st.sidebar:
    st.image("logo.jpg", width=220)
    st.title("Bazán Atelier")
    st.write("✨ *Diseño de autor en Lima*")
    
    st.markdown("---")
    # Link de Instagram Recuperado
    st.write("📸 **Siguenos en:**")
    st.markdown("[@bazan_atelier](https://www.instagram.com/bazan_atelier/)")
    
    st.markdown("---")
    st.write("📍 **Punto de Entrega:**")
    # Aquí puedes cambiar el link por la ubicación exacta luego
    st.link_button("📍 Ver en Google Maps", "https://maps.google.com")
    
    st.markdown("---")
    st.info("📦 **Envíos:** Lima y provincias vía Olva Courier o Shalom.")

# 4. Cuerpo Principal (Catálogo)
st.markdown("<h1>Bazán Atelier</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic; color: #8d7b6d;'>Prendas exclusivas hechas a medida</p>", unsafe_allow_html=True)
st.write("---")

# Banner Verde de Promoción Recuperado
st.success("✨ **LANZAMIENTO WEB:** Usa el código **BAZAN10** y obtén un descuento especial en tu primer pedido.")

# 5. Filtros Interactivos
st.markdown("<h3 style='text-align: center;'>Nuestra Colección</h3>", unsafe_allow_html=True)
categoria = st.radio("", ["Ver Todo", "Tops", "Pantalones", "Vestidos"], horizontal=True)
st.write("")

# 6. Base de Datos de Productos
productos = [
    {
        "nombre": "Top Seda Marfil", 
        "precio": "S/ 95", 
        "cat": "Tops", 
        "img": "https://images.unsplash.com/photo-1434389677669-e08b4cac3105?q=80&w=500", 
        "wa": "Top%20Seda%20Marfil"
    },
    {
        "nombre": "Pantalón Sastrero Arena", 
        "precio": "S/ 140", 
        "cat": "Pantalones", 
        "img": "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?q=80&w=500", 
        "wa": "Pantalón%20Sastrero%20Arena"
    },
]

# Lógica de filtrado dinámico
productos_filtrados = [p for p in productos if categoria == "Ver Todo" or p["cat"] == categoria]

# 7. Despliegue de Productos
if not productos_filtrados:
    st.warning(f"Estamos preparando nuevos modelos para la categoría: {categoria}")
else:
    cols = st.columns(2, gap="large")
    for i, p in enumerate(productos_filtrados):
        with cols[i % 2]:
            st.image(p["img"], use_container_width=True)
            st.subheader(p["nombre"])
            st.markdown(f"<h4 style='color: #5d4037;'>{p['precio']}</h4>", unsafe_allow_html=True)
            link_wa = f"https://wa.me/51937395562?text=Hola%20Bazán%20Atelier!%20Me%20interesa%20el%20{p['wa']}"
            st.link_button(f"Pedir por WhatsApp 💬", link_wa)

# 8. PIE DE PÁGINA REFACTORIZADO (El toque profesional)
st.write("---")
cols_footer = st.columns([2, 1])

with cols_footer[0]:
    st.markdown("""
        <p style='color: #8d7b6d; font-size: 0.9rem; margin-bottom: 0;'>
            © 2026 <b>Bazán Atelier</b> | Diseño y Confección de Autor.<br>
            Hecho con ❤️ en Lima, Perú.
        </p>
    """, unsafe_allow_html=True)

with cols_footer[1]:
    st.markdown("""
        <p style='color: #bcaaa4; font-size: 0.8rem; text-align: right; margin-bottom: 0;'>
            Soporte Técnico:<br>
            A. Chávez • Systems Engineering
        </p>
    """, unsafe_allow_html=True)