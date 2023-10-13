import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import streamlit.components.v1 as components
from PIL import Image

# st.set_page_config(page_title = 'Elecciones 2023 - Sitio de consulta',
#                         layout='wide', initial_sidebar_state='collapsed')
# st.markdown(
#     """
#     <style>
#     [data-testid="collapsedControl"] svg {
#         height: 3rem;
#         width: 3rem;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )
# st.markdown(
#         """
#        <style>
#        [data-testid="stSidebar"][aria-expanded="true"]{
#            min-width: 200px;
#            max-width: 200px;
#        }
#        """,
#         unsafe_allow_html=True,
#     )
# st.markdown("""<style>.css-zt5igj svg{display:none}</style>""", unsafe_allow_html=True)

def mesa():

    @st.cache_data  
    def load_data(url):
        df = pd.read_csv(url)
        return df

    df = load_data("data/consultar_resultados_mesa_AP_presi.csv")


    comovotar = Image.open('data/comovotar.png')

    c11, c22, c33 = st.columns([0.1,0.8,0.1])

    with c22:

        st.markdown("<h3 style='text-align: center;'>CONSULTÁ LOS RESULTADOS DE TU MESA<br></h3>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center; font-weight: normal;'>Si querés conocer los resultados filtrá de acuerdo a tu distrito, luego por tu municipio y luego en qué circuito votaste.<br> Por último, ingresá el número de mesa correspondiente.<br><br></h5>", unsafe_allow_html=True)


        with st.expander("¿Cómo sé en cuál circuito y mesa voté?"):
                c1111, c2244, c3321 = st.columns([0.2,0.6,0.2])
                with c2244:
                    st.markdown("""<div style="text-align: justify;"><br> Para conocer en cuál sección, circuito y mesa votaste simplementa andá a la sección de la página '¿Dónde voto?', ingresa los datos que te pide la página y ahí te dará todo lo necesario para poder después rellenar los filtros de abajo y conocer los resultados de tu mesa. <br></div>""", unsafe_allow_html=True)
                    #st.write("Para conocer en cuál sección, circuito y mesa votaste simplementa andá a la sección de la página '¿Dónde voto?', ingresa los datos que te pide la página y ahí te dará todo lo necesario para poder después rellenar los filtros de abajo y conocer los resultados de tu mesa.")
                    st.image(comovotar)

        c55, c66, c77, c88 = st.columns(4)

        with c55:
            distrito = st.selectbox("Seleccioná tu distrito:",
                                                            df['distrito_id'].unique(),index=None, placeholder=""
            )
            filtrado_distrito = df.query('distrito_id == @distrito')
            filtrado_distrito = filtrado_distrito.sort_values(by='seccion')
        with c66:                                                   
            seccion = st.selectbox("Ingresá tu sección/municipio:",
                                                            filtrado_distrito['seccion'].unique(),index=None, placeholder=""
                                                            )
            filtrado_seccion = filtrado_distrito.query('seccion == @seccion')
            filtrado_seccion = filtrado_seccion.sort_values(by='circuito_id')
        with c77:    
            circuito = st.selectbox("Ingresá tu circuito:",
                                                            filtrado_seccion['circuito_id'].unique(),index=None, placeholder=""
                                    )
            filtrado_circuito = filtrado_seccion.query('circuito_id == @circuito')
            filtrado_circuito['mesa_id'] = filtrado_circuito['mesa_id'].astype(int)
            #filtrado_circuito = filtrado_circuito.sort_values(by='mesa_id')
        with c88:
            mesa = st.selectbox("Ingresá tu número de mesa:",
                                                            filtrado_circuito['mesa_id'].unique(),index=None, placeholder=""
                                                            )
            #mesa = int(mesa)

            # Query the DataFrame using mesa as an integer
            df_final = filtrado_circuito.loc[filtrado_circuito['mesa_id'] == mesa]
            df_final2 = df_final.groupby(['agrupacion', 'tipovoto'])['votos'].sum().reset_index().sort_values(by='votos', ascending=False)

        p1, p2,p3,p4 = st.columns(4)
        with p4:
            resultado = st.button("Graficá tus resultados!", use_container_width=True)

        values_to_drop = ['IMPUGNADO', 'NULO']


        df_sin_nulos = df_final[~df_final['tipovoto'].isin(values_to_drop)]
        df_sin_nulos.loc[df_sin_nulos['tipovoto'] == 'EN BLANCO', 'agrupacion'] = 'EN BLANCO'
        df_sin_nulos_grafico = df_sin_nulos.groupby('agrupacion')['votos'].sum().reset_index().sort_values(by='votos', ascending=False)
        df_sin_nulos_grafico['agrupacion'] = df_sin_nulos_grafico['agrupacion'].replace('FRENTE DE IZQUIERDA Y DE TRABAJADORES - UNIDAD', 'FRENTE DE IZQUIERDA')
        df_sin_nulos_grafico['agrupacion'] = df_sin_nulos_grafico['agrupacion'].replace('MOVIMIENTO IZQUIERDA JUVENTUD Y DIGNIDAD', 'MIJD')
        df_sin_nulos_grafico['agrupacion'] = df_sin_nulos_grafico['agrupacion'].replace('UNION DEL CENTRO DEMOCRATICO', 'UCEDE')

        sumavotos = df_sin_nulos['votos'].sum()

        df_sin_nulos_grafico['Porcentaje'] = (df_sin_nulos_grafico['votos'] / sumavotos * 100).round(2)

        colores_partido = {
            'UNION POR LA PATRIA': '#01b5f0',
            'JUNTOS POR EL CAMBIO': '#fcd201',
            'LA LIBERTAD AVANZA': '#9654e5',
            'HACEMOS POR NUESTRO PAIS': '#88e99a',
            'FRENTE DE IZQUIERDA': '#c11f1f',
            'EN BLANCO': '#c4c4c4',
                    }
        config = {'displayModeBar': False}

        hovertemp = "<b>Agrupación: </b> %{y} <br>"
        hovertemp += "<b>Porcentaje: </b> %{x} <br>"
        hovertemp += "<b>Cantidad de votos: </b> %{customdata[0]}"

        fig = px.bar(df_sin_nulos_grafico, x='Porcentaje', y='agrupacion', color='agrupacion', color_discrete_map=colores_partido, orientation='h', text='Porcentaje', 
                    custom_data=[df_sin_nulos_grafico['votos']], title=f'Resultados en mesa {mesa} del circuito {circuito} perteneciente a {seccion}, {distrito}')
        fig.update_traces(textposition='outside', textfont_color='black')
        fig.update_traces(hovertemplate=hovertemp, hoverlabel=dict(namelength=0))
            #fig_partidos_prov.update_yaxes(type='category', ticks="outside", ticklen=5, tickcolor='rgb(195,186,178)', linecolor='rgb(203,193,185)')
            #fig_partidos_prov.update_xaxes(anchor="free", shift= -10, gridcolor="rgb(228,217,208)")
        fig.update_layout(showlegend=False, template='simple_white', height=650)  
        #fig.update_traces(customdata=[df_sin_nulos_grafico['votos']], selector=dict(type='bar'))
        #fig.update_traces(hovertemplate='Agrupación: %{y}<br>Porcentaje: %{x}<br>Cantidad de votos: %{customdata[0]}', hoverlabel=dict(namelength=0))
        fig.update_yaxes(title="Porcentaje", fixedrange=True)
        fig.update_xaxes(title="", fixedrange=True)

        df_sin_nulos_grafico = df_sin_nulos_grafico[df_sin_nulos_grafico['Porcentaje'] != 0]
        fig2 = px.bar(df_sin_nulos_grafico, x='agrupacion', y='Porcentaje', color='agrupacion', color_discrete_map=colores_partido, orientation='v', text='Porcentaje', 
                    custom_data=[df_sin_nulos_grafico['votos']], title=f'Resultados en mesa {mesa} del circuito {circuito} <br>perteneciente a {seccion}, {distrito}')
        fig2.update_traces(textposition='outside', textfont_color='black')
        fig2.update_traces(hovertemplate=hovertemp, hoverlabel=dict(namelength=0))
            #fig_partidos_prov.update_yaxes(type='category', ticks="outside", ticklen=5, tickcolor='rgb(195,186,178)', linecolor='rgb(203,193,185)')
            #fig_partidos_prov.update_xaxes(anchor="free", shift= -10, gridcolor="rgb(228,217,208)")
        fig2.update_layout(showlegend=False, template='simple_white', height=650)  
        #fig.update_traces(customdata=[df_sin_nulos_grafico['votos']], selector=dict(type='bar'))
        #fig.update_traces(hovertemplate='Agrupación: %{y}<br>Porcentaje: %{x}<br>Cantidad de votos: %{customdata[0]}', hoverlabel=dict(namelength=0))
        fig2.update_yaxes(title="Porcentaje", fixedrange=True)
        fig2.update_xaxes(title="", fixedrange=True)


        df_final2.rename(columns={'agrupacion':'Agrupación política', 'tipovoto':'Tipo de voto', 'votos': 'Votos'}, inplace=True)
        df_final2.loc[df_final2['Tipo de voto'] == 'EN BLANCO', 'Agrupación política'] = 'EN BLANCO'
        df_final2.loc[df_final2['Tipo de voto'] == 'IMPUGNADO', 'Agrupación política'] = 'IMPUGNADO'
        df_final2.loc[df_final2['Tipo de voto'] == 'NULO', 'Agrupación política'] = 'NULO'
        df_final2['Agrupación política'] = df_final2['Agrupación política'].replace('FRENTE DE IZQUIERDA Y DE TRABAJADORES - UNIDAD', 'FRENTE DE IZQUIERDA')
        df_final2['Agrupación política'] = df_final2['Agrupación política'].replace('MOVIMIENTO IZQUIERDA JUVENTUD Y DIGNIDAD', 'MIJD')
        df_final2['Agrupación política'] = df_final2['Agrupación política'].replace('UNION DEL CENTRO DEMOCRATICO', 'UCEDE')
        sumavotos2 = df_final2['Votos'].sum()

        df_final2['Porcentaje'] = (df_final2['Votos'] / sumavotos2 * 100).round(2)
        df_final2 = df_final2[['Agrupación política', 'Porcentaje', 'Votos']]
        
        
        if resultado:

            st.plotly_chart(fig2, use_container_width=True, config=config)

            st.dataframe(df_final2, use_container_width=True, hide_index = True)

