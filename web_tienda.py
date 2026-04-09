import streamlit as st

# 1. Configuración de página
st.set_page_config(page_title="Bazán Atelier | Tienda Oficial", page_icon="👗", layout="wide")

# --- LÓGICA DEL CARRITO ---
if 'carrito' not in st.session_state:
    st.session_state.carrito = []

def agregar_al_carrito(producto, precio):
    st.session_state.carrito.append({"nombre": producto, "precio": precio})
    st.toast(f"✅ {producto} añadido")

# 2. CSS de Lujo
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lato:wght@300;400&display=swap');
    .main { background-color: #fdfaf7; }
    h1 { font-family: 'Playfair Display', serif; color: #5d4037; text-align: center; font-size: 3.5rem !important; margin-bottom: 0px; }
    div[data-testid="stColumn"] {
        background-color: white;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.02);
        border: 1px solid #f1ece7;
        margin-bottom: 25px;
        text-align: center;
    }
    .stButton>button { width: 100%; border-radius: 12px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar (Carrito + Info)
with st.sidebar:
    st.image("logo.jpg", width=200)
    st.title("🛒 Tu Carrito")
    if not st.session_state.carrito:
        st.write("Tu carrito está vacío.")
    else:
        total = 0
        resumen_wa = "Hola Bazán Atelier! Quiero realizar este pedido: %0A"
        for item in st.session_state.carrito:
            st.write(f"- {item['nombre']} ({item['precio']})")
            precio_num = int(item['precio'].replace('S/ ', ''))
            total += precio_num
            resumen_wa += f"- {item['nombre']} ({item['precio']})%0A"
        st.write("---")
        st.subheader(f"Total: S/ {total}")
        resumen_wa += f"%0ATotal a pagar: S/ {total}"
        st.link_button("🚀 Finalizar Pedido WhatsApp", f"https://wa.me/51937395562?text={resumen_wa}")
        if st.button("Vaciar Carrito"):
            st.session_state.carrito = []
            st.rerun()
    st.markdown("---")
    st.write("📸 **IG:** [@bazan_atelier](https://www.instagram.com/bazan_atelier/)")
    st.write("📍 **Ubicación:**")
    st.link_button("📍 Ver en Google Maps", "https://goo.gl/maps/ejemplo_lima")
    st.info("📦 **Envíos:** Lima y provincias.")

# 4. Cuerpo Principal
st.markdown("<h1>Bazán Atelier</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-style: italic; color: #8d7b6d;'>Diseños exclusivos hechos a medida</p>", unsafe_allow_html=True)
st.write("---")
st.success("✨ **LANZAMIENTO WEB:** Usa el código **BAZAN10** y obtén un descuento especial.")

# 5. Filtros
st.markdown("<h3 style='text-align: center;'>Explora nuestra colección</h3>", unsafe_allow_html=True)
categoria = st.radio("", ["Ver Todo", "Tops", "Pantalones", "Vestidos"], horizontal=True)
st.write("") 

# 6. Base de Datos (Links de fotos arreglados)
productos = [
    {"nombre": "Top Seda Marfil", "precio": "S/ 95", "cat": "Tops", "img": "https://images.unsplash.com/photo-1551163943-3f6a855d1153?q=80&w=500"},
    {"nombre": "Pantalón Sastrero Arena", "precio": "S/ 140", "cat": "Pantalones", "img": "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?q=80&w=500"},
    {"nombre": "Vestido Gala Noche", "precio": "S/ 220", "cat": "Vestidos", "img": "https://images.unsplash.com/photo-1566174053879-31528523f8ae?q=80&w=500"},
    {"nombre": "Vestido Floral Verano", "precio": "S/ 180", "cat": "Vestidos", "img": "https://images.unsplash.com/photo-1515372039744-b8f02a3ae446?q=80&w=500"},
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
            st.markdown(f"**{p['precio']}**")
            if st.button(f"🛒 Añadir al carrito", key=f"btn_{i}"):
                agregar_al_carrito(p["nombre"], p["precio"])

# 8. Pie de Página
st.write("---")
c1, c2 = st.columns([2, 1])
with c1: st.markdown("© 2026 **Bazán Atelier** | Hecho en Lima, Perú.")
with c2: st.markdown("<p style='text-align: right; color: #bcaaa4;'>A. Chávez • Systems Eng.</p>", unsafe_allow_html=True)