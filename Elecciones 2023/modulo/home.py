import streamlit as st
from modulo.resultadostodos import resultados
from modulo.dondevoto import donde_voto
from modulo.faq import faq
from modulo.mesa import mesa
from modulo.electores import electores
from modulo.plataformas import propuestas
#from app import menu


def home():
    

    def make_grid(cols,rows):
        grid = [0]*cols
        for i in range(cols):
            with st.container():
                grid[i] = st.columns(rows)
        return grid
    
    c1, c2, c3 = st.columns([0.1,0.8,0.1])

    st.markdown("<h3 style='text-align: center;'>Qué vas a poder encontrar en esta sección<br></h3>", unsafe_allow_html=True)
    with c2:
        mygrid = make_grid(3,3)

        mygrid[0][0].markdown("<h3 style='text-align: center;'>RESULTADOS<br></h3>", unsafe_allow_html=True)
        mygrid[1][0].markdown("<h5 style='text-align: center; font-weight: normal;'>Consultá los resultados para presidente, diputados, senadores y gobernadores de las PASO 2023. Además, buscá los resultados de la mesa en la qué votaste. También vas a poder encontrar datos históricos de comparación con elecciones anteriores, la evolución del voto en blanco y la participación en las elecciones.  <br></h5>", unsafe_allow_html=True)
        mygrid[2][0].button("Consultá los resultados", key=12)

        if st.button("Consultá los resultados"):
            resultados()

    
    
