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

# 2. CSS PARA ELIMINAR BLOQUES GIGANTES
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lato:wght@300;400&display=swap');
    
    .main { background-color: #fdfaf7; }
    h1 { font-family: 'Playfair Display', serif; color: #5d4037; text-align: center; font-size: 3.5rem !important; }
    
    /* Tarjetas de producto */
    div[data-testid="stColumn"] {
        background-color: white; padding: 20px; border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.03); border: 1px solid #f1ece7;
    }

    /* Botones de la tienda (Verdes) */
    .stButton>button { 
        width: 100%; border-radius: 8px; font-weight: bold; 
        background-color: #25D366 !important; color: white !important; border: none;
    }

    /* BOTÓN X (DENTRO DEL MISMO CUADRO) */
    [data-testid="stSidebar"] button[kind="secondary"] {
        padding: 0px !important; height: 18px !important; width: 18px !important;
        min-width: 18px !important; border-radius: 50% !important;
        font-size: 10px !important; color: #000 !important;
        border: 1px solid #ddd !important; background-color: #f9f9f9 !important;
        float: right; margin-top: -35px; /* Sube la X para que esté junto al nombre */
    }

    /* BOTÓN VACIAR CARRITO (PEQUEÑO Y FINO) */
    .btn-vaciar button {
        background-color: transparent !important; color: #999 !important;
        border: 1px solid #eee !important; font-size: 11px !important; 
        height: 25px !important; width: auto !important; padding: 0 10px !important;
        margin-top: 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar (Carrito Compacto)
with st.sidebar:
    st.image("logo.jpg", width=150)
    st.title("Mi Pedido")
    
    if not st.session_state.carrito:
        st.write("El carrito está vacío.")
    else:
        total = 0
        resumen_wa = "Hola Bazán Atelier! Mi pedido es:%0A"
        
        # Eliminamos columnas para que no se vea desordenado
        for i, item in enumerate(st.session_state.carrito):
            st.markdown(f"**{item['nombre']}** ({item['talla']})\n{item['precio']}")
            # La X ahora flota a la derecha gracias al CSS
            if st.button("x", key=f"del_{i}"):
                eliminar_del_carrito(i)
            st.write("---")
            
            precio_num = int(item['precio'].replace('S/ ', ''))
            total += precio_num
            resumen_wa += f"- {item['nombre']} ({item['talla']})%0A"
        
        st.subheader(f"Total: S/ {total}")
        
        st.link_button("🚀 Finalizar por WhatsApp", f"https://wa.me/51937395562?text={resumen_wa}%0ATotal: S/ {total}")
        st.link_button("💳 Pagar con Tarjeta/Yape", "https://link.mercadopago.com.pe/bazanatelier")
        
        # Contenedor especial para el botón de vaciar
        st.markdown('<div class="btn-vaciar">', unsafe_allow_html=True)
        if st.button("Vaciar Carrito"):
            st.session_state.carrito = []
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.write("📸 **IG:** [@bazan_atelier](https://www.instagram.com/bazan_atelier/)")

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

# Lógica de filtrado
productos_filtrados = [p for p in productos if categoria == "Ver Todo" or p["cat"] == categoria]

# 7. Galería
cols = st.columns(2, gap="large")
for i, p in enumerate(productos_filtrados):
    with cols[i % 2]:
        st.image(p["img"], use_container_width=True)
        st.subheader(p["nombre"])
        st.write(f"**Precio: {p['precio']}**")
        talla_sel = st.selectbox(f"Talla:", p["tallas"], key=f"talla_{i}")
        
        if st.button(f"🛒 Añadir al carrito", key=f"btn_{i}"):
            agregar_al_carrito(p["nombre"], p["precio"], talla_sel)

# 8. Pie de Página
st.write("---")
st.markdown("<p style='text-align: center; color: #bcaaa4; font-size: 0.8rem;'>© 2026 Bazán Atelier | Desarrollo: A. Chávez • Systems Eng.</p>", unsafe_allow_html=True)