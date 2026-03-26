import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="Análisis de Velocidad - Cálculo Integral", layout="wide")

st.title("Análisis de la variación de la velocidad mediante cálculo integral")
st.markdown("""
Este simulador analiza el movimiento de un vehículo basándose en la **Segunda Ley de Newton** y el **Cálculo Integral**. 
Aquí, la velocidad se calcula como la integral de la aceleración respecto al tiempo.
""")

st.divider()

# --- Entradas de Datos en el Cuerpo de la Página ---
st.subheader("1. Configuración de Parámetros Físicos")
st.latex(r"a(t) = \frac{F_{motor} - F_{resistencia}}{m}")
st.latex(r"v(t) = v_0 + \int_{0}^{t} a(t) \, dt")

col_params1, col_params2 = st.columns(2)

with col_params1:
    m = st.number_input("Masa del vehículo (kg)", value=1500, min_value=1, step=100, help="Masa inercial del vehículo.")
    f_motor = st.number_input("Fuerza del motor (N)", value=5000, min_value=0, step=500, help="Fuerza de propulsión constante.")

with col_params2:
    f_resistencia = st.number_input("Fuerza de resistencia (N)", value=500, min_value=0, step=100, help="Resistencia aerodinámica y de rodadura estimada.")
    t_final = st.number_input("Tiempo total de simulación (s)", value=20, min_value=1, max_value=300, step=5)
    v0 = st.number_input("Velocidad inicial (m/s)", value=0.0, step=1.0, help="Velocidad al inicio de la simulación.")

st.divider()

# --- Lógica Matemática (Cálculo Integral) ---
# Cálculo de la aceleración: a(t) = (F_motor - F_resistencia) / m
f_neta = f_motor - f_resistencia
aceleracion_constante = f_neta / m 

# Definición del diferencial de tiempo (dt) para la aproximación de la integral
dt = 0.1 
tiempo = np.arange(0, t_final + dt, dt)

# Modelo de aceleración: a(t) es constante en el tiempo
aceleracion_t = np.full_like(tiempo, aceleracion_constante)

# Cálculo de la velocidad: v(t) = v_0 + ∫ a(t) dt
# Usamos el método de acumulación (Suma de Riemann) para integrar
velocidad = v0 + np.cumsum(aceleracion_t) * dt 

# --- Visualización de Resultados ---
st.subheader("2. Análisis de Resultados")

# Métricas principales
m1, m2, m3 = st.columns(3)
m1.metric("Aceleración Inicial", f"{aceleracion_t[0]:.2f} m/s²")
m2.metric("Velocidad Final (m/s)", f"{velocidad[-1]:.2f} m/s")
m3.metric("Velocidad Final (km/h)", f"{velocidad[-1] * 3.6:.2f} km/h")

# Gráfico de Integración
st.markdown("### Relación Cinemática: Velocidad como Integral de la Aceleración")
chart_data = pd.DataFrame(
    {
        "Aceleración a(t) m/s²": aceleracion_t,
        "Velocidad v(t) m/s": velocidad,
    },
    index=tiempo
)
st.line_chart(chart_data)

# Tabla de Datos para Referencia Académica
if st.checkbox("Ver registros de integración paso a paso"):
    df = pd.DataFrame({
        "Tiempo (s)": tiempo,
        "Aceleración (m/s²)": aceleracion_t,
        "Velocidad (m/s)": velocidad
    })
    st.dataframe(df.style.format("{:.3f}"))