# Análisis de Velocidad mediante Cálculo Integral

Este proyecto es un simulador interactivo construido en Python usando [Streamlit](https://streamlit.io/) que analiza el movimiento de un vehículo aplicando la **Segunda Ley de Newton** y los principios del **Cálculo Integral**.

## Características

- Configuración de parámetros físicos (masa del vehículo, fuerza del motor, fuerza de resistencia y velocidad inicial).
- Cálculo de la velocidad en el tiempo mediante la integración numérica de la aceleración neta.
- Gráficos interactivos que visualizan la relación cinemática, demostrando cómo la velocidad equivale al área bajo la curva de la aceleración.
- Registros detallados de integración paso a paso en formato de tabla.

## Requisitos

Asegúrate de tener instalado Python. Las librerías principales de este proyecto son:

- `streamlit`
- `pandas`
- `numpy`

## Ejecución

Para ejecutar la aplicación, abre una terminal en el directorio del proyecto y usa el siguiente comando:

```bash
pip install -r requirements.txt
streamlit run main.py
```

La simulación se abrirá automáticamente en tu navegador web predeterminado.
