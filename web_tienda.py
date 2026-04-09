import streamlit as st

# 1. Configuración de pestaña y página
st.set_page_config(
    page_title="Bazán Atelier | Tienda Oficial", 
    page_icon="👗", 
    layout="wide"
)

# --- LÓGICA DEL CARRITO MEJORADA ---
if 'carrito' not in st.session_state:
    st.session_state.carrito = []

def agregar_al_carrito(p_id, producto, precio, talla):
    # Usamos un ID único para poder borrar el exacto
    st.session_state.carrito.append({
        "id": p_id,
        "nombre": producto, 
        "precio": precio, 
        "talla": talla
    })
    st.toast(f"✅ {producto} añadido")

def eliminar_del_carrito(indice):
    st.session_state.carrito.pop(indice)
    st.rerun()

# 2. CSS DE LUJO
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lato:wght@300;400&display=swap');
    .main { background-color: #fdfaf7; }
    h1 { font-family: 'Playfair Display', serif; color: #5d4037; text-align: center; font-size: 3.5rem !important; margin-bottom: 0px; }
    div[data-testid="stColumn"] {
        background-color: white;
        padding: 20px; border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.02);
        border: 1px solid #f1ece7; margin-bottom: 25px;
    }
    .stButton>button { width: 100%; border-radius: 12px; font-weight: bold; }
    /* Estilo especial para el botón de eliminar (rojo sutil) */
    .btn-eliminar>button {
        background-color: #ff4b4b1a !important;
        color: #ff4b4b !important;
        border: 1px solid #ff4b4b !important;
        height: 1.5em !important;
        font-size: 0.7rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar (CARRITO CON OPCIÓN DE QUITAR)
with st.sidebar:
    st.image("logo.jpg", width=200)
    st.title("🛒 Tu Carrito")
    
    if not st.session_state.carrito:
        st.write("Tu carrito está vacío.")
    else:
        total = 0
        resumen_wa = "Hola Bazán Atelier! Quiero este pedido: %0A"
        
        # Iteramos con el índice para saber cuál borrar
        for i, item in enumerate(st.session_state.carrito):
            col_item, col_btn = st.columns([4, 1])
            with col_item:
                st.write(f"**{item['nombre']}** ({item['talla']})")
                st.write(f"{item['precio']}")
            with col_btn:
                # Botón pequeño para eliminar
                if st.button("❌", key=f"del_{i}"):
                    eliminar_del_carrito(i)
            
            precio_num = int(item['precio'].replace('S/ ', ''))
            total += precio_num
            resumen_wa += f"- {item['nombre']} (Talla: {item['talla']})%0A"
            st.write("---")
        
        st.subheader(f"Total: S/ {total}")
        resumen_wa += f"%0ATotal a pagar: S/ {total}"
        
        st.link_button("🚀 Finalizar Pedido WhatsApp", f"https://wa.me/51937395562?text={resumen_wa}")
        
        if st.button("Vaciar Todo el Carrito"):
            st.session_state.carrito = []
            st.rerun()

    st.markdown("---")
    st.write("📸 **IG:** [@bazan_atelier](https://www.instagram.com/bazan_atelier/)")
    st.write("📍 **Ubicación:**")
    st.link_button("📍 Ver en Google Maps", "https://goo.gl/maps/ejemplo_lima")

# 4. Cuerpo Principal
st.markdown("<h1>Bazán Atelier</h1>", unsafe_allow_html=True)
st.write("---")
st.success("✨ **LANZAMIENTO WEB:** Usa el código **BAZAN10** para tu descuento.")

# 5. Filtros
categoria = st.radio("", ["Ver Todo", "Tops", "Pantalones", "Vestidos"], horizontal=True)

# 6. Base de Datos
productos = [
    {"nombre": "Top Seda Marfil", "precio": "S/ 95", "cat": "Tops", "img": "https://images.unsplash.com/photo-1551163943-3f6a855d1153?q=80&w=500", "tallas": ["S", "M", "L"]},
    {"nombre": "Pantalón Sastrero Arena", "precio": "S/ 140", "cat": "Pantalones", "img": "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?q=80&w=500", "tallas": ["28", "30", "32"]},
    {"nombre": "Vestido Gala Noche", "precio": "S/ 220", "cat": "Vestidos", "img": "https://images.unsplash.com/photo-1566174053879-31528523f8ae?q=80&w=500", "tallas": ["S", "M"]},
    {"nombre": "Vestido Floral Verano", "precio": "S/ 180", "cat": "Vestidos", "img": "https://images.unsplash.com/photo-1515372039744-b8f02a3ae446?q=80&w=500", "tallas": ["Standard"]},
]

productos_filtrados = [p for p in productos if categoria == "Ver Todo" or p["cat"] == categoria]

# 7. Galería
if not productos_filtrados:
    st.warning(f"Próximamente más en: {categoria}")
else:
    cols = st.columns(2, gap="large")
    for i, p in enumerate(productos_filtrados):
        with cols[i % 2]:
            st.image(p["img"], use_container_width=True)
            st.subheader(p["nombre"])
            st.write(p["precio"])
            talla_sel = st.selectbox(f"Talla:", p["tallas"], key=f"talla_{i}")
            
            if st.button(f"🛒 Añadir al carrito", key=f"btn_{i}"):
                agregar_al_carrito(i, p["nombre"], p["precio"], talla_sel)

# 8. Pie de Página
st.write("---")
c1, c2 = st.columns([2, 1])
with c1: st.markdown("© 2026 **Bazán Atelier** | Lima, Perú.")
with c2: st.markdown("<p style='text-align: right; color: #bcaaa4;'>A. Chávez • Systems Eng.</p>", unsafe_allow_html=True)