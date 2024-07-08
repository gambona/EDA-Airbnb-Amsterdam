import streamlit as st
import pandas as pd 
import json as js
import matplotlib.pyplot as plt
from plotly.offline import iplot
import streamlit.components.v1 as components

st.set_page_config(
    page_title="EDA Airbnb Amsterdam",
    page_icon="🌆",
    layout="wide")

#------------------------------INTRODUCCIÓN------------------------------#
def mostrar_introduccion():
        st.markdown("""
    <div class="container" style="text-align: center;">
        <h1 class='centered-title-pg1'>Análisis exploratiorio de datos de Airbnb en Amsterdam</h1>
        <h3 class='centered-text-pg1'>Desde Insideairbnb.com he obtenido los datos a 2023 y los he comparado con otro análisis de 2016.</h3>
    </div>""", unsafe_allow_html=True)   
        st.image("imagenes/portada.png", use_column_width=True)
        st.caption("Leyenda de la imagen: Generada con AI")
        
#------------------------------EDA_2023------------------------------#

def mostrar_eda():
    st.markdown("""
        <div class="container" style="text-align: center;">
            <h3 class='centered-text-pg1'>Cabe destacar la medida tomada por el gobierno de Amsterdam de máximo 30 días de alquiler al año, lo que ha reducido el número de alojamientos en la ciudad.</h3>
        </div>""", unsafe_allow_html=True)  
    st.header("Análisis Exploratorio de Datos (EDA)")
    st.write("Datos sobre Amsterdam informativos a 12 de Diciembre")
    st.image('imagenes/2.png', use_column_width=True)
    st.write("")
    st.write("")
    st.image('imagenes/3.png', use_column_width=True)
    st.write("")
    st.write("")
    st.image('imagenes/4.png', use_column_width=True)
    st.write("")
    st.write("")
    st.image('imagenes/5.png', use_column_width=True)

#------------------------------Comparación 2016 y 2023------------------------------#
def mostrar_comparacion():
    st.header("Comparación de Datos 2016 con 2023")
    st.write("Comparación de los datos de Airbnb en Amsterdam en 2016 y 2023")
    col1, col2 = st.columns(2)

    with col1:
        st.image('imagenes/7barrios+airbnbt.png', use_column_width=True)
        st.image('imagenes/output2.png', use_column_width=True)
        
    with col2:
        st.image('imagenes/output_copy_2.png', use_column_width=True)
        st.image('imagenes/output_copy.jpg', use_column_width=True)
    st.write("Debido a las medidas turisticas tomadas por el gobierno de Amsterdam, se ha reducido el número de alojamientos en la ciudad")
    st.write("Por consecuente, y agregando la inflacción, el precio promedio de los alojamientos ha aumentado considerablemente en 7 años")
#------------------------------MAPA------------------------------#
def mostrar_mapa():
    st.markdown("""<div class="container" style="text-align: center;">
        <h3 class='centered-text-pg1'>Las atracciones más populares de Amsterdam y la delimitación de cada barrio</h3>
    </div>""", unsafe_allow_html=True)  
    with open("map1.html", "r", encoding='utf-8') as f:    
        html_data = f.read()
        components.html(html_data, height=600)
    
#------------------------------Reviews------------------------------#
def mostrar_reviews():
    st.header("Reviews")
    st.write("El número de reviews, claramente un fuerte factor social que ayuda a los cleintes a finalizar reservas, ha mostrado un exponencial cfrecimiento desde el lanzamiento de Airbnb, mostrando el éxito de la Scale Up.")
    st.write("Solo en Amsterdam, de media, el número de reviews ha aumentado un 129% de media, incluyendo los graves efectos de la pandemia en el número de reservas.")
    tab1, tab2, tab3 = st.tabs(["Reviews mensuales", "Crecimiento absoluto", "Análisis de sentimientos"])
    with tab1:
        st.image('imagenes/7.png')
    with tab2:
        st.image('imagenes/6.png')
    with tab3:
        st.image('imagenes/8.png.jpg')
        
#------------------------------Power BI------------------------------#
def mostrar_powerbi():
    st.write("Power BI")  
    powerbi_url = "https://app.powerbi.com/view?r=eyJrIjoiN2E4NjA5YjUtOWM5Yi00NWIxLWJhZGQtNDBkMGZmYjM4ZTMwIiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9"
    st.markdown(f"""<iframe width="100%" height="600" src="{powerbi_url}" frameborder="0" allowFullScreen="true"></iframe>""", unsafe_allow_html=True)
    st.write("En este panel interactivo podemos ver donde se concentra el turismo y  el precio medio por barrio")
#####################################################################
with st.sidebar:
    st.image("/Users/aguedagambon/Bootcamp/Github/EDA_Airbnb_Amsterdam/Imagenes/amsterdam_image.png", width=100)
    st.write("## Navegación")
    diapositiva = st.radio(
        "Selecciona una Diapositiva",
        ("Introducción", "EDA", "Comparación 7 Años", "Reviews", "Mapa de barrios y atracciones", "Power BI"))

funciones_diapositivas = {
    "Introducción": mostrar_introduccion,
    "EDA": mostrar_eda,
    "Comparación 7 Años": mostrar_comparacion,
    "Reviews": mostrar_reviews,
    "Mapa de barrios y atracciones": mostrar_mapa,
    "Power BI": mostrar_powerbi,
    "Reviews": mostrar_reviews,
}
funciones_diapositivas[diapositiva]()
