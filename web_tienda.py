import streamlit as st

# 1. Configuración de página
st.set_page_config(
    page_title="Bazán Atelier | Tienda Oficial", 
    page_icon="👗", 
    layout="wide"
)

# --- LÓGICA DEL CARRITO ---
if 'carrito' not in st.session_state:
    st.session_state.carrito = []

def agregar_al_carrito(producto, precio, talla):
    st.session_state.carrito.append({"nombre": producto, "precio": precio, "talla": talla})
    st.toast(f"✅ {producto} añadido")

def eliminar_del_carrito(indice):
    st.session_state.carrito.pop(indice)
    st.rerun()

# 2. CSS SANEADO (Sin errores de botones verticales)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lato:wght@300;400&display=swap');
    
    .main { background-color: #fdfaf7; }
    h1 { font-family: 'Playfair Display', serif; color: #5d4037; text-align: center; font-size: 3.5rem !important; }
    
    /* Tarjetas de producto */
    div[data-testid="stColumn"] {
        background-color: white;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border: 1px solid #f1ece7;
        margin-bottom: 25px;
    }

    /* Botones principales */
    .stButton>button { 
        width: 100%; 
        border-radius: 12px; 
        font-weight: bold; 
        background-color: #25D366 !important; 
        color: white !important; 
        border: none;
    }

    /* Botón X del carrito (Pequeño y circular) */
    [data-testid="stSidebar"] button[kind="secondary"] {
        padding: 0px !important;
        height: 22px !important;
        width: 22px !important;
        min-width: 22px !important;
        border-radius: 50% !important;
        font-size: 12px !important;
        color: #ff4b4b !important;
        border: 1px solid #ff4b4b !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar (Carrito Limpio)
with st.sidebar:
    st.image("logo.jpg", width=180)
    st.title("🛒 Mi Pedido")
    
    if not st.session_state.carrito:
        st.info("El carrito está vacío.")
    else:
        total = 0
        resumen_wa = "Hola Bazán Atelier! Mi pedido es:%0A"
        
        for i, item in enumerate(st.session_state.carrito):
            c1, c2 = st.columns([4, 1])
            with c1:
                st.markdown(f"**{item['nombre']}**\nTalla: {item['talla']} | {item['precio']}")
            with c2:
                if st.button("x", key=f"del_{i}"):
                    eliminar_del_carrito(i)
            st.write("---")
            
            precio_num = int(item['precio'].replace('S/ ', ''))
            total += precio_num
            resumen_wa += f"- {item['nombre']} ({item['talla']})%0A"
        
        st.subheader(f"Total: S/ {total}")
        
        # Botones finales
        st.link_button("🚀 Finalizar por WhatsApp", f"https://wa.me/51937395562?text={resumen_wa}%0ATotal: S/ {total}")
        st.link_button("💳 Pagar con Tarjeta/Yape", "https://link.mercadopago.com.pe/bazanatelier")
        
        if st.button("Vaciar Carrito"):
            st.session_state.carrito = []
            st.rerun()

    st.markdown("---")
    st.write("📸 **IG:** [@bazan_atelier](https://www.instagram.com/bazan_atelier/)")
    st.info("📦 **Envíos:** Lima y provincias.")

# 4. Cuerpo Principal
st.markdown("<h1>Bazán Atelier</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8d7b6d;'>Prendas exclusivas hechas a medida</p>", unsafe_allow_html=True)
st.write("---")

st.success("✨ **LANZAMIENTO WEB:** Usa el código **BAZAN10** y obtén un descuento especial.")

# 5. Filtros
categoria = st.radio("", ["Ver Todo", "Tops", "Pantalones", "Vestidos"], horizontal=True)
st.write("") 

# 6. Base de Datos
productos = [
    {"nombre": "Top Seda Marfil", "precio": "S/ 95", "cat": "Tops", "img": "https://images.unsplash.com/photo-1551163943-3f6a855d1153?q=80&w=500", "tallas": ["S", "M", "L"]},
    {"nombre": "Pantalón Sastrero Arena", "precio": "S/ 140", "cat": "Pantalones", "img": "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?q=80&w=500", "tallas": ["28", "30", "32"]},
    {"nombre": "Vestido Gala Noche", "precio": "S/ 220", "cat": "Vestidos", "img": "https://images.unsplash.com/photo-1566174053879-31528523f8ae?q=80&w=500", "tallas": ["S", "M"]},
    {"nombre": "Vestido Floral Verano", "precio": "S/ 180", "cat": "Vestidos", "img": "https://images.unsplash.com/photo-1515372039744-b8f02a3ae446?q=80&w=500", "tallas": ["Standard"]},
]

productos_filtrados = [p for p in productos if categoria == "Ver Todo" or p["cat"] == categoria]

# 7. Galería
cols = st.columns(2, gap="large")
for i, p in enumerate(productos_filtrados):
    with cols[i % 2]:
        st.image(p["img"], use_container_width=True)
        st.subheader(p["nombre"])
        st.write(f"Precio: {p['precio']}")
        talla_sel = st.selectbox(f"Talla:", p["tallas"], key=f"talla_{i}")
        
        if st.button(f"🛒 Añadir al carrito", key=f"btn_{i}"):
            agregar_al_carrito(p["nombre"], p["precio"], talla_sel)

# 8. Pie de Página
st.write("---")
c1, c2 = st.columns([2, 1])
with c1: st.markdown("© 2026 **Bazán Atelier** | Lima, Perú.")
with c2: st.markdown("<p style='text-align: right; color: #bcaaa4;'>A. Chávez • Systems Eng.</p>", unsafe_allow_html=True)