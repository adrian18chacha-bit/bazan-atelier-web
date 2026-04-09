import streamlit as st

# 1. Configuración de página
st.set_page_config(page_title="Bazán Atelier | Tienda Oficial", page_icon="👗", layout="wide")

# --- LÓGICA DEL CARRITO ---
if 'carrito' not in st.session_state:
    st.session_state.carrito = []

def agregar_al_carrito(producto, precio, talla):
    st.session_state.carrito.append({"nombre": producto, "precio": precio, "talla": talla})
    st.toast(f"✅ {producto} añadido")

def eliminar_del_carrito(indice):
    st.session_state.carrito.pop(indice)
    st.rerun()

# 2. CSS AVANZADO (Diseño Limpio y Moderno)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lato:wght@300;400&display=swap');
    
    .main { background-color: #fdfaf7; }
    h1 { font-family: 'Playfair Display', serif; color: #5d4037; text-align: center; font-size: 3.5rem !important; margin-bottom: 10px; }
    
    /* Estilo de las tarjetas de producto */
    div[data-testid="stColumn"] {
        background-color: white;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border: 1px solid #f1ece7;
    }

    /* Botones Pro */
    .stButton>button { border-radius: 10px; font-weight: 600; transition: 0.3s; }
    .btn-comprar button { background-color: #25D366 !important; color: white !important; border: none; }
    .btn-pago button { background-color: #009EE3 !important; color: white !important; border: none; margin-top: 5px; }
    
    /* Diseño del carrito en sidebar */
    .cart-item {
        background-color: #f8f9fa;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        border-left: 4px solid #5d4037;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar (Carrito Ordenado)
with st.sidebar:
    st.image("logo.jpg", width=200)
    st.title("🛒 Mi Pedido")
    st.write("---")
    
    if not st.session_state.carrito:
        st.info("Tu carrito está vacío.")
    else:
        total = 0
        resumen_wa = "Hola Bazán Atelier! Mi pedido es:%0A"
        
        for i, item in enumerate(st.session_state.carrito):
            with st.container():
                # Fila de producto
                c1, c2 = st.columns([4, 1])
                c1.markdown(f"**{item['nombre']}**\nTalla: {item['talla']} | {item['precio']}")
                if c2.button("❌", key=f"del_{i}"):
                    eliminar_del_carrito(i)
                st.write("---")
            
            precio_num = int(item['precio'].replace('S/ ', ''))
            total += precio_num
            resumen_wa += f"- {item['nombre']} (Talla: {item['talla']})%0A"
        
        st.subheader(f"Total: S/ {total}")
        
        # Botones de Acción Final
        st.markdown(f'<div class="btn-comprar">', unsafe_allow_html=True)
        st.link_button("💬 Pedir por WhatsApp", f"https://wa.me/51937395562?text={resumen_wa}%0ATotal: S/ {total}")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown(f'<div class="btn-pago">', unsafe_allow_html=True)
        # CONFIGURACIÓN: Aquí va el link de Mercado Pago de tu prima
        st.link_button("💳 Pagar con Tarjeta / Yape", "https://link.mercadopago.com.pe/bazanatelier") 
        st.markdown('</div>', unsafe_allow_html=True)

        if st.button("Vaciar Carrito"):
            st.session_state.carrito = []
            st.rerun()

    st.markdown("---")
    st.write("📸 [@bazan_atelier](https://www.instagram.com/bazan_atelier/)")

# 4. Cuerpo Principal
st.markdown("<h1>Bazán Atelier</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8d7b6d;'>Exclusividad y elegancia en cada prenda</p>", unsafe_allow_html=True)

# 5. Filtros con mejor estilo
st.write("")
categoria = st.radio("", ["Ver Todo", "Tops", "Pantalones", "Vestidos"], horizontal=True)
st.write("---")

# 6. Base de Datos
productos = [
    {"nombre": "Top Seda Marfil", "precio": "S/ 95", "cat": "Tops", "img": "https://images.unsplash.com/photo-1551163943-3f6a855d1153?q=80&w=500", "tallas": ["S", "M", "L"]},
    {"nombre": "Pantalón Sastrero Arena", "precio": "S/ 140", "cat": "Pantalones", "img": "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?q=80&w=500", "tallas": ["28", "30", "32"]},
    {"nombre": "Vestido Gala Noche", "precio": "S/ 220", "cat": "Vestidos", "img": "https://images.unsplash.com/photo-1566174053879-31528523f8ae?q=80&w=500", "tallas": ["S", "M"]},
    {"nombre": "Vestido Floral Verano", "precio": "S/ 180", "cat": "Vestidos", "img": "https://images.unsplash.com/photo-1515372039744-b8f02a3ae446?q=80&w=500", "tallas": ["Standard"]},
]

productos_filtrados = [p for p in productos if categoria == "Ver Todo" or p["cat"] == categoria]

# 7. Galería Pro
cols = st.columns(2, gap="large")
for i, p in enumerate(productos_filtrados):
    with cols[i % 2]:
        st.image(p["img"], use_container_width=True)
        st.subheader(p["nombre"])
        st.markdown(f"**Precio: {p['precio']}**")
        talla_sel = st.selectbox(f"Talla:", p["tallas"], key=f"talla_{i}")
        
        if st.button(f"🛒 Añadir al carrito", key=f"btn_{i}"):
            agregar_al_carrito(p["nombre"], p["precio"], talla_sel)

# 8. Footer
st.write("---")
f1, f2 = st.columns([2, 1])
f1.write("© 2026 **Bazán Atelier** | Lima, Perú")
f2.markdown("<p style='text-align: right; color: #bcaaa4;'>Desarrollo: A. Chávez • Sistemas</p>", unsafe_allow_html=True)