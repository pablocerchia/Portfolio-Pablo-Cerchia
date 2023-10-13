import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import streamlit.components.v1 as components
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode, ColumnsAutoSizeMode
import streamlit_antd_components as sac
from modulo.bancas import diputados, senadores
from modulo.presidentes import presidentes
from modulo.gobernador import gobernadores
from modulo.mesa import mesa

# st.set_page_config(page_title = 'Elecciones 2023 - Sitio de consulta',
#                     layout='wide', initial_sidebar_state='collapsed')



# tabla_delta_listas = pd.read_csv("data/tabla_delta_listas.csv")
# tabla_delta = pd.read_csv("data/tabla_delta.csv")
# partido_ganador_x_prov = pd.read_csv("data/partido_ganador_x_prov.csv")
# partidos_x_prov = pd.read_csv("data/partidos_x_prov.csv")
# ganadores_listas_prov = pd.read_csv("data/ganadores_listas_prov.csv")
# presidencial_x_AP = pd.read_csv("data/resultados_por_partido.csv")
# votos_candidatos_totales = pd.read_csv("data/votos_candidatos_totales.csv")
# listas_x_prov = pd.read_csv("data/resultados_por_lista_CLEAN.csv")
# fuente_votos = pd.read_csv("data/fuente_votos_partidos.csv")
#geojson_file = "data/Regions geometry.1692055458453.geojson"
#geojson = gpd.read_file(geojson_file)
#tabla_ganadores_x_prov = geojson.merge(partido_ganador_x_prov, on="Name")
#ganadores_listas_prov = geojson.merge(ganadores_listas_prov, on="Name")
#tabla_votos = tabla_ganadores_x_prov.merge(partidos_x_prov, on=["Name", 'Partido', 'perc'])



def resultados():
    tabs_generales = sac.tabs(['PRESIDENTE','DIPUTADOS','SENADORES', 'GOBERNADOR PBA', 'MESA'], index=0, format_func='upper', height=None, align='center', position='top', shape='default', grow=False, return_index=False)
    if tabs_generales == 'PRESIDENTE':
        presidentes()
    if tabs_generales == 'DIPUTADOS':
        diputados()
    if tabs_generales == 'SENADORES':
        senadores()
    if tabs_generales == 'GOBERNADOR PBA':
        gobernadores()
    if tabs_generales == 'MESA':
        mesa()