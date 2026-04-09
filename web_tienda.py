import streamlit as st

# 1. Configuración de pestaña y página
st.set_page_config(
    page_title="Bazán Atelier | Tienda Oficial", 
    page_icon="👗", 
    layout="wide"
)

# --- LÓGICA DEL CARRITO (Persistencia de datos) ---
if 'carrito' not in st.session_state:
    st.session_state.carrito = []

def agregar_al_carrito(producto, precio, talla):
    st.session_state.carrito.append({"nombre": producto, "precio": precio, "talla": talla})
    st.toast(f"✅ {producto} (Talla {talla}) añadido al carrito")

# 2. CSS DE LUJO (Diseño Premium Stark)
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
    
    /* Tarjetas de productos con efecto hover */
    div[data-testid="stColumn"] {
        background-color: white;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.02);
        border: 1px solid #f1ece7;
        margin-bottom: 25px;
        transition: transform 0.3s ease;
    }
    div[data-testid="stColumn"]:hover { transform: translateY(-5px); }

    /* Botones de acción */
    .stButton>button { 
        width: 100%; 
        border-radius: 12px; 
        font-weight: bold; 
        background-color: #25D366 !important; 
        color: white !important; 
        border: none;
        height: 3.5em;
    }
    
    /* Radio buttons centrados */
    div[role="radiogroup"] {
        display: flex;
        justify-content: center;
        gap: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar (CARRITO + INFO DE MARCA)
with st.sidebar:
    st.image("logo.jpg", width=200)
    st.title("🛒 Tu Carrito")
    
    if not st.session_state.carrito:
        st.write("Tu carrito está vacío.")
    else:
        total = 0
        resumen_wa = "Hola Bazán Atelier! Quiero realizar este pedido: %0A"
        for i, item in enumerate(st.session_state.carrito):
            st.write(f"- {item['nombre']} [Talla {item['talla']}] ({item['precio']})")
            precio_num = int(item['precio'].replace('S/ ', ''))
            total += precio_num
            resumen_wa += f"- {item['nombre']} (Talla: {item['talla']}) - {item['precio']}%0A"
        
        st.write("---")
        st.subheader(f"Total: S/ {total}")
        resumen_wa += f"%0ATotal a pagar: S/ {total}"
        
        # Botón para finalizar en WhatsApp
        link_final = f"https://wa.me/51937395562?text={resumen_wa}"
        st.link_button("🚀 Finalizar Pedido WhatsApp", link_final)
        
        if st.button("Vaciar Carrito"):
            st.session_state.carrito = []
            st.rerun()

    st.markdown("---")
    st.write("📸 **IG:** [@bazan_atelier](https://www.instagram.com/bazan_atelier/)")
    st.write("📍 **Ubicación:**")
    st.link_button("📍 Ver en Google Maps", "https://goo.gl/maps/ejemplo_lima")
    st.info("📦 **Envíos:** Lima y provincias vía Olva o Shalom.")

# 4. Cuerpo Principal
st.markdown("<h1>Bazán Atelier</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic; color: #8d7b6d;'>Diseños exclusivos hechos a medida</p>", unsafe_allow_html=True)
st.write("---")

# BANNER VERDE RECUPERADO
st.success("✨ **LANZAMIENTO WEB:** Usa el código **BAZAN10** y obtén un descuento especial en tu primer pedido.")

# 5. Filtros Interactivos
st.markdown("<h3 style='text-align: center;'>Nuestra Colección</h3>", unsafe_allow_html=True)
categoria = st.radio("", ["Ver Todo", "Tops", "Pantalones", "Vestidos"], horizontal=True)
st.write("")

# 6. Base de Datos de Productos (Con Tallas y Fotos Estables)
productos = [
    {
        "nombre": "Top Seda Marfil", 
        "precio": "S/ 95", 
        "cat": "Tops", 
        "img": "https://images.unsplash.com/photo-1551163943-3f6a855d1153?q=80&w=500", 
        "tallas": ["S", "M", "L"]
    },
    {
        "nombre": "Pantalón Sastrero Arena", 
        "precio": "S/ 140", 
        "cat": "Pantalones", 
        "img": "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?q=80&w=500", 
        "tallas": ["28", "30", "32"]
    },
    {
        "nombre": "Vestido Gala Noche", 
        "precio": "S/ 220", 
        "cat": "Vestidos", 
        "img": "https://images.unsplash.com/photo-1566174053879-31528523f8ae?q=80&w=500", 
        "tallas": ["S", "M"]
    },
    {
        "nombre": "Vestido Floral Verano", 
        "precio": "S/ 180", 
        "cat": "Vestidos", 
        "img": "https://images.unsplash.com/photo-1515372039744-b8f02a3ae446?q=80&w=500", 
        "tallas": ["Standard"]
    },
]

# Lógica de filtrado
productos_filtrados = [p for p in productos if categoria == "Ver Todo" or p["cat"] == categoria]

# 7. Galería Dinámica de Productos
if not productos_filtrados:
    st.warning(f"Próximamente más modelos para la categoría: {categoria}")
else:
    cols = st.columns(2, gap="large")
    for i, p in enumerate(productos_filtrados):
        with cols[i % 2]:
            st.image(p["img"], use_container_width=True)
            st.subheader(p["nombre"])
            st.markdown(f"<h4 style='color: #5d4037;'>{p['precio']}</h4>", unsafe_allow_html=True)
            
            # Selector de Tallas (UX Mejorada)
            talla_sel = st.selectbox(f"Elige talla para {p['nombre']}:", p["tallas"], key=f"talla_{i}")
            
            # Galería de Detalles
            with st.expander("🔍 Ver detalles de la prenda"):
                st.write("• Material: Premium seleccionado.")
                st.write("• Confección: Hecho a mano en nuestro taller.")
                st.image(p["img"], width=150, caption="Detalle de tela")
            
            # Botón de Compra
            if st.button(f"🛒 Añadir al carrito", key=f"btn_{i}"):
                agregar_al_carrito(p["nombre"], p["precio"], talla_sel)

# 8. PIE DE PÁGINA PROFESIONAL (Doble columna)
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