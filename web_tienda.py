import streamlit as st

st.set_page_config(page_title="Bazán Atelier | Tienda", page_icon="👗", layout="wide")

# --- LÓGICA DEL CARRITO (Session State) ---
if 'carrito' not in st.session_state:
    st.session_state.carrito = []

def agregar_al_carrito(producto, precio):
    st.session_state.carrito.append({"nombre": producto, "precio": precio})
    st.toast(f"✅ {producto} añadido")

# --- CSS MEJORADO ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lato:wght@300;400&display=swap');
    .main { background-color: #fdfaf7; }
    h1 { font-family: 'Playfair Display', serif; color: #5d4037; text-align: center; font-size: 3.5rem !important; }
    .stButton>button { width: 100%; border-radius: 12px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR CON CARRITO ---
with st.sidebar:
    st.image("logo.jpg", width=200)
    st.title("🛒 Tu Carrito")
    
    if not st.session_state.carrito:
        st.write("El carrito está vacío.")
    else:
        total = 0
        resumen_wa = "Hola Bazán Atelier! Quiero pedir: %0A"
        for i, item in enumerate(st.session_state.carrito):
            st.write(f"- {item['nombre']} ({item['precio']})")
            # Extraer número del precio para el total
            precio_num = int(item['precio'].replace('S/ ', ''))
            total += precio_num
            resumen_wa += f"- {item['nombre']} ({item['precio']})%0A"
        
        st.write("---")
        st.subheader(f"Total: S/ {total}")
        resumen_wa += f"%0ATotal a pagar: S/ {total}"
        
        # Botón Final de Compra
        link_final = f"https://wa.me/51937395562?text={resumen_wa}"
        st.link_button("🚀 Finalizar Pedido por WhatsApp", link_final)
        
        if st.button("Vaciar Carrito"):
            st.session_state.carrito = []
            st.rerun()

    st.markdown("---")
    st.write("📸 [@bazan_atelier](https://www.instagram.com/bazan_atelier/)")

# --- CUERPO PRINCIPAL ---
st.markdown("<h1>Bazán Atelier</h1>", unsafe_allow_html=True)
st.write("---")

# Filtros
categoria = st.radio("", ["Ver Todo", "Tops", "Pantalones"], horizontal=True)

# Productos
productos = [
    {"nombre": "Top Seda Marfil", "precio": "S/ 95", "cat": "Tops", "img": "https://images.unsplash.com/photo-1434389677669-e08b4cac3105?q=80&w=500"},
    {"nombre": "Pantalón Sastrero Arena", "precio": "S/ 140", "cat": "Pantalones", "img": "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?q=80&w=500"},
]

productos_filtrados = [p for p in productos if categoria == "Ver Todo" or p["cat"] == categoria]

cols = st.columns(2, gap="large")
for i, p in enumerate(productos_filtrados):
    with cols[i % 2]:
        st.image(p["img"], use_container_width=True)
        st.subheader(p["nombre"])
        st.write(p["precio"])
        # Botón para agregar
        if st.button(f"Añadir al carrito", key=p["nombre"]):
            agregar_al_carrito(p["nombre"], p["precio"])

# --- FOOTER ---
st.write("---")
cols_f = st.columns([2, 1])
with cols_f[0]:
    st.markdown("© 2026 **Bazán Atelier** | Lima, Perú")
with cols_f[1]:
    st.markdown("<p style='text-align: right; color: #bcaaa4;'>A. Chávez • Systems Eng.</p>", unsafe_allow_html=True)