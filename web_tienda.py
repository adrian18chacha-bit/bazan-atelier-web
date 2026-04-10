import streamlit as st

# 1. Configuración de página
st.set_page_config(page_title="Bazán Atelier | Tienda Oficial", page_icon="👗", layout="wide")

# --- LÓGICA AVANZADA DEL CARRITO ---
if 'carrito' not in st.session_state:
    st.session_state.carrito = {}

def agregar_al_carrito(nombre, precio, talla):
    # Creamos una clave única por producto y talla
    item_id = f"{nombre}_{talla}"
    if item_id in st.session_state.carrito:
        st.session_state.carrito[item_id]['cantidad'] += 1
    else:
        st.session_state.carrito[item_id] = {
            "nombre": nombre, 
            "precio": int(precio.replace('S/ ', '')), 
            "talla": talla, 
            "cantidad": 1
        }
    st.toast(f"✅ {nombre} añadido")

def ajustar_cantidad(item_id, delta):
    st.session_state.carrito[item_id]['cantidad'] += delta
    if st.session_state.carrito[item_id]['cantidad'] <= 0:
        del st.session_state.carrito[item_id]
    st.rerun()

# 2. CSS PROFESIONAL (Estilo Boutique)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lato:wght@300;400&display=swap');
    .main { background-color: #fdfaf7; }
    h1 { font-family: 'Playfair Display', serif; color: #5d4037; text-align: center; font-size: 3rem !important; }
    
    /* Tarjetas de producto */
    div[data-testid="stColumn"] {
        background-color: white; padding: 20px; border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.03); border: 1px solid #f1ece7;
    }

    /* Botón añadir (Elegante) */
    .stButton>button { 
        width: 100%; border-radius: 8px; font-weight: bold; 
        background-color: #25D366 !important; color: white !important; border: none;
    }

    /* Estilo del Carrito en Sidebar */
    .cart-title { font-family: 'Playfair Display', serif; font-size: 1.5rem; color: #5d4037; }
    .item-name { font-size: 0.9rem; font-weight: bold; margin-bottom: -5px; }
    .item-details { font-size: 0.8rem; color: #666; }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar (CARRITO CON CANTIDADES)
with st.sidebar:
    st.image("logo.jpg", width=120)
    st.markdown('<p class="cart-title">Tu Pedido</p>', unsafe_allow_html=True)
    
    if not st.session_state.carrito:
        st.write("Tu carrito está vacío.")
    else:
        total_pagar = 0
        resumen_wa = "Hola Bazán Atelier! Mi pedido es:%0A"
        
        for item_id, item in st.session_state.carrito.items():
            st.markdown(f"<p class='item-name'>{item['nombre']} (Talla {item['talla']})</p>", unsafe_allow_html=True)
            
            # Controles de cantidad en una sola línea
            c1, c2, c3 = st.columns([1, 1, 1])
            with c1:
                if st.button("➖", key=f"min_{item_id}"): ajustar_cantidad(item_id, -1)
            with c2:
                st.markdown(f"<p style='text-align:center; padding-top:5px;'>{item['cantidad']}</p>", unsafe_allow_html=True)
            with c3:
                if st.button("➕", key=f"add_{item_id}"): ajustar_cantidad(item_id, 1)
            
            subtotal = item['precio'] * item['cantidad']
            total_pagar += subtotal
            st.markdown(f"<p class='item-details'>Subtotal: S/ {subtotal}</p>", unsafe_allow_html=True)
            st.write("---")
            
            resumen_wa += f"- {item['nombre']} ({item['talla']}) x{item['cantidad']}: S/ {subtotal}%0A"

        st.subheader(f"Total: S/ {total_pagar}")
        
        # Botones de Acción
        st.link_button("🚀 Enviar a WhatsApp", f"https://wa.me/51937395562?text={resumen_wa}%0ATotal: S/ {total_pagar}")
        st.link_button("💳 Pago con Tarjeta/Yape", "https://link.mercadopago.com.pe/bazanatelier")
        
        if st.button("Vaciar Carrito"):
            st.session_state.carrito = {}
            st.rerun()

    st.markdown("---")
    st.write("📸 [@bazan_atelier](https://www.instagram.com/bazan_atelier/)")

# 4. Cuerpo Principal
st.markdown("<h1>Bazán Atelier</h1>", unsafe_allow_html=True)
st.write("---")

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
st.markdown("<p style='text-align: center; color: #bcaaa4; font-size: 0.8rem;'>© 2026 Bazán Atelier | Desarrollo: A. Chávez • Systems Eng.</p>", unsafe_allow_html=True)