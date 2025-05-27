import streamlit as st
import random

st.set_page_config(page_title="Ecuaciones de Primer Grado", layout="centered")
st.title("🧠 Resuelve la Ecuación de Primer Grado")

# Generar valores aleatorios
if 'a' not in st.session_state:
    st.session_state['a'] = random.randint(1, 10)
    st.session_state['x_real'] = random.randint(-10, 10)
    st.session_state['b'] = random.randint(-10, 10)
    st.session_state['c'] = st.session_state['a'] * st.session_state['x_real'] + st.session_state['b']

# Mostrar la ecuación
a = st.session_state['a']
b = st.session_state['b']
c = st.session_state['c']
x_real = st.session_state['x_real']

st.latex(f"{a}x + {b} = {c}")

# Entrada del usuario
respuesta = st.number_input("Introduce el valor de x:", step=1.0)

# Verificación
if st.button("Verificar"):
    if respuesta == x_real:
        st.success("✅ ¡Correcto! 🎉")
    else:
        st.error(f"❌ Incorrecto. La solución era x = {x_real}")

# Botón para nueva ecuación
if st.button("Nueva ecuación"):
    st.session_state.clear()
    st.experimental_rerun()
