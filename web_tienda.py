import streamlit as st

# 1. Configuración de página de alto nivel
st.set_page_config(
    page_title="Bazán Atelier | Tienda Oficial", 
    page_icon="👗", 
    layout="wide"
)

# 2. Estilo CSS Avanzado (Diseño "Premium")
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lato:wght@300;400&display=swap');

    /* Fondo y fuentes globales */
    .main { background-color: #fdfaf7; }
    html, body, [class*="css"]  {
        font-family: 'Lato', sans-serif;
        color: #4a3728;
    }

    /* Título principal con estilo de revista */
    h1 { 
        font-family: 'Playfair Display', serif;
        color: #5d4037; 
        font-size: 3.5rem !important;
        text-align: center;
        margin-bottom: 0px;
    }

    /* Tarjetas de productos con sombra suave */
    div[data-testid="stColumn"] {
        background-color: white;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.03);
        border: 1px solid #f1ece7;
        transition: transform 0.3s ease;
    }
    
    div[data-testid="stColumn"]:hover {
        transform: translateY(-5px);
    }

    /* Botón de WhatsApp elegante */
    .stButton>button {
        width: 100%;
        background-color: #25D366 !important;
        color: white !important;
        border: none;
        padding: 10px;
        font-weight: bold;
        border-radius: 12px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Quitar el menú de arriba de Streamlit para más limpieza */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar (Barra Lateral) con información de confianza
with st.sidebar:
    st.image("logo.jpg", width=220)
    st.markdown("---")
    st.title("Bazán Atelier")
    st.write("✨ *Diseño de autor en Lima*")
    
    st.markdown("### 🛍️ Proceso de Compra")
    st.write("1. Selecciona tu modelo favorito.")
    st.write("2. Consulta disponibilidad vía WhatsApp.")
    st.write("3. ¡Coordinamos tu talla y envío!")
    
    st.markdown("---")
    st.write("📍 **Showroom:** Lima, Perú")
    st.write("📸 **IG:** [@bazan_atelier](https://www.instagram.com/bazan_atelier/)")
    
    st.info("💡 Cada prenda es confeccionada con telas de alta calidad para asegurar un calce perfecto.")

# 4. Cuerpo Principal
st.markdown("<h1>Bazán Atelier</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic; font-size: 1.2rem; color: #8d7b6d;'>Prendas únicas para mujeres reales</p>", unsafe_allow_html=True)
st.write("---")

# Banner de promoción
st.success("✨ **LANZAMIENTO WEB:** Usa el código **BAZAN10** y obtén un descuento especial en tu primer pedido.")

# 5. Galería de Productos (2 columnas)
col1, col2 = st.columns(2, gap="large")

with col1:
    # Cuando tengas la foto real, cámbiame por: st.image("nombre_archivo.jpg")
    st.image("https://images.unsplash.com/photo-1434389677669-e08b4cac3105?q=80&w=500", caption="Nueva Colección")
    st.subheader("Top Seda Marfil")
    st.write("Un diseño ligero y elegante, ideal para eventos especiales o salidas casuales de lujo.")
    st.markdown("#### **S/ 95.00**")
    
    btn_link = "https://wa.me/51937395562?text=Hola%20Bazán%20Atelier!%20Me%20interesa%20el%20Top%20Seda%20Marfil"
    st.link_button("Pedir por WhatsApp 💬", btn_link)

with col2:
    st.image("https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?q=80&w=500", caption="Favoritos")
    st.subheader("Pantalón Sastrero Arena")
    st.write("Corte clásico de tiro alto con tela fresca, diseñado para estilizar la figura.")
    st.markdown("#### **S/ 140.00**")
    
    btn_link2 = "https://wa.me/51937395562?text=Hola%20Bazán%20Atelier!%20Me%20gustaría%20el%20Pantalón%20Sastrero%20Arena"
    st.link_button("Pedir por WhatsApp 💬", btn_link2)

# 6. Pie de página
st.write("---")
st.markdown("<p style='text-align: center; color: #bcaaa4;'>© 2026 Bazán Atelier | Desarrollado por Adrián Chávez - Ing. de Sistemas</p>", unsafe_allow_html=True)