import streamlit as st

# 1. Configuración de página
st.set_page_config(page_title="Bazán Atelier | Tienda Oficial", page_icon="👗", layout="wide")

# --- LÓGICA DE SEGURIDAD PARA EL CARRITO ---
if 'carrito' in st.session_state and isinstance(st.session_state.carrito, list):
    st.session_state.carrito = {}

if 'carrito' not in st.session_state:
    st.session_state.carrito = {}

def agregar_al_carrito(nombre, precio, talla):
    item_id = f"{nombre}_{talla}"
    if item_id in st.session_state.carrito:
        st.session_state.carrito[item_id]['cantidad'] += 1
    else:
        precio_limpio = int(precio.replace('S/ ', '').replace(',', ''))
        st.session_state.carrito[item_id] = {
            "nombre": nombre, 
            "precio": precio_limpio, 
            "talla": talla, 
            "cantidad": 1
        }
    st.toast(f"✅ {nombre} añadido")

def ajustar_cantidad(item_id, delta):
    st.session_state.carrito[item_id]['cantidad'] += delta
    if st.session_state.carrito[item_id]['cantidad'] <= 0:
        del st.session_state.carrito[item_id]
    st.rerun()

# CÁLCULO DE CANTIDAD TOTAL
cantidad_total = sum(item['cantidad'] for item in st.session_state.carrito.values())

# 2. CSS "BLACK & GRAY" CON DETALLES RECUPERADOS
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lato:wght@300;400&display=swap');
    
    .main {{ background-color: #ffffff; }}
    h1 {{ font-family: 'Playfair Display', serif; color: #1a1a1a; text-align: center; font-size: 3rem !important; margin-bottom: 0px; }}
    
    /* Botones Pro Negros */
    .stButton>button {{ 
        width: 100%; border-radius: 5px; font-weight: 300; letter-spacing: 1px;
        background-color: #1a1a1a !important; color: white !important; border: none; 
        transition: 0.4s; height: 3em;
    }}
    .stButton>button:hover {{ background-color: #444444 !important; transform: translateY(-1px); }}

    /* Cabecera del Carrito */
    .cart-header {{
        display: flex; align-items: center; justify-content: flex-end;
        padding: 10px 30px; margin-top: -50px;
    }}
    .cart-icon-container {{ position: relative; font-size: 1.2rem; margin-right: 8px; }}
    .cart-badge {{
        position: absolute; top: -5px; right: -10px;
        background-color: #000000; color: white;
        border-radius: 50%; padding: 1px 5px; font-size: 9px;
    }}
    .cart-text {{ font-family: 'Lato', sans-serif; font-size: 0.85rem; color: #1a1a1a; margin: 0; }}
    </style>
    """, unsafe_allow_html=True)

# 3. Cabecera Minimalista
st.markdown(f"""
    <div class="cart-header">
        <div class="cart-icon-container">
            🛒 <span class="cart-badge">{cantidad_total}</span>
        </div>
        <p class="cart-text">CARRITO</p>
    </div>
    """, unsafe_allow_html=True)

# 4. Sidebar (INFO COMPLETA RECUPERADA)
with st.sidebar:
    st.image("logo.jpg", width=130)
    st.markdown("### MI PEDIDO")
    st.write("---")
    
    if not st.session_state.carrito:
        st.write("No hay artículos seleccionados.")
    else:
        total_pagar = 0
        resumen_wa = "Hola Bazán Atelier! Mi pedido es:%0A"
        for item_id, item in st.session_state.carrito.items():
            st.markdown(f"**{item['nombre']}** ({item['talla']})")
            c1, c2, c3 = st.columns([1, 1, 1])
            with c1:
                if st.button("－", key=f"min_{item_id}"): ajustar_cantidad(item_id, -1)
            with c2:
                st.markdown(f"<p style='text-align:center; padding-top:5px;'>{item['cantidad']}</p>", unsafe_allow_html=True)
            with c3:
                if st.button("＋", key=f"add_{item_id}"): ajustar_cantidad(item_id, 1)
            subtotal = item['precio'] * item['cantidad']
            total_pagar += subtotal
            st.write(f"Subtotal: S/ {subtotal}")
            st.write("---")
            resumen_wa += f"- {item['nombre']} ({item['talla']}) x{item['cantidad']}%0A"

        st.subheader(f"Total: S/ {total_pagar}")
        st.link_button("🚀 ENVIAR A WHATSAPP", f"https://wa.me/51937395562?text={resumen_wa}%0ATotal: S/ {total_pagar}")
        st.link_button("💳 PAGAR CON TARJETA", "https://link.mercadopago.com.pe/bazanatelier")
        if st.button("VACIAR TODO"):
            st.session_state.carrito = {}
            st.rerun()

    st.markdown("---")
    # DETALLES RECUPERADOS
    st.write("📸 **IG:** [@bazan_atelier](https://www.instagram.com/bazan_atelier/)")
    st.write("📍 **Ubicación:**")
    st.link_button("🗺️ Ver en Google Maps", "https://goo.gl/maps/ejemplo_lima")
    st.info("📦 **Envíos:** Lima y todo el Perú vía Olva o Shalom.")

# 5. Cuerpo Principal
st.markdown("<h1>Bazán Atelier</h1>", unsafe_allow_html=True)
st.write("---")

# DETALLE RECUPERADO: Frase verde de lanzamiento
st.success("✨ **LANZAMIENTO WEB:** Usa el código **BAZAN10** y obtén un descuento especial.")

# Filtros
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
        st.write(f"S/ {p['precio']}")
        talla_sel = st.selectbox(f"TALLA:", p["tallas"], key=f"talla_{i}")
        if st.button(f"🛒 AÑADIR", key=f"btn_{i}"):
            agregar_al_carrito(p["nombre"], p["precio"], talla_sel)

# 8. Pie de Página Profesional
st.write("---")
st.markdown("<p style='text-align: center; color: #999; font-size: 0.7rem; letter-spacing: 2px;'>BAZÁN ATELIER | DESARROLLO: A. CHÁVEZ • SYSTEMS ENG.</p>", unsafe_allow_html=True)