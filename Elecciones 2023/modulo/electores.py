import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import streamlit.components.v1 as components
from streamlit_folium import st_folium

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

def electores ():

    # Load CSV file into GeoDataFrame
    tabla_csv = pd.read_csv("data/tabla_electores.csv")
    #geojson_file = "data/Regions geometry.1692055458453.geojson"
    #geojson = gpd.read_file(geojson_file)
    #tabla_electores = geojson.merge(tabla_csv, on="Name")
    electores_anio = pd.read_csv("data/electores_anio.csv")
    electores_grupo_etario = pd.read_csv("data/electores_grupo_etario.csv")
    config = {'displayModeBar': False}

    c11, c22, c33 = st.columns([0.1,0.8,0.1])


        #st.title('Resultados presidenciales por provincia')
        #tabla_ganadores_x_prov2 = pd.DataFrame(tabla_ganadores_x_prov)
        #tabla_ganadores_x_prov['Color'] = tabla_ganadores_x_prov['Partido'].map(color_dict)
    with c22:

        st.markdown("<h3 style='text-align: center;'>ELECTORES REGISTRADOS POR PROVINCIA<br></h3>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center; font-weight: normal;'>Consultá cuántos electores hay por distrito y cómo están distribuidos por género.<br> También podés consultar cuántas mesas, secciones electorales y circuitos electorales hay en cada distrito.<br><br></h5>", unsafe_allow_html=True)
        #st.title('Electores por provincia', anchor=False)
        #st.write("Consultá cuántos electores hay por distrito y cómo están distribuidos por género. También podés consultar cuántas mesas, secciones electorales y circuitos electorales hay en cada distrito.")

        c1, c2 = st.columns(2)

        with c1:
            components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/14870718" data-height="1150px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=1150)

        with c2: 
                    st.markdown("<h5 style='text-align: center;'><br></h5>", unsafe_allow_html=True)
                    melted_df = pd.melt(tabla_csv, id_vars=['Name'], value_vars=['Femenino', 'Masculino', 'NoBinario'],
                            var_name='Genero', value_name='Cant_genero')
                    melted_df2 = pd.melt(tabla_csv, id_vars=['Name'], value_vars=['M_Percentage', 'F_Percentage', 'X_Percentage'],
                            var_name='Porc_genero', value_name='Cant_porc_genero')
                    #result = pd.merge(melted_df, melted_df2, on=['Name'])

                    prov_select_electores = st.selectbox("Filtrar distribución de género y edad por distrito:",
                                                            melted_df['Name'].unique()
                                                            )
                    df_provincial = melted_df.query('Name == @prov_select_electores')
                    df_provincial = df_provincial.sort_values(by='Cant_genero', ascending=False)
                    df_provincial2 = melted_df2.query('Name == @prov_select_electores')
                    df_provincial2 = df_provincial2.sort_values(by='Cant_porc_genero', ascending=False)

                    colores_partido = {
                    'Femenino': '#f39a58',
                    'Masculino': '#0f203a',
                    '% Femenino': '#f39a58',
                    '% Masculino': '#0f203a'
                            }

                    fig_partidos_prov = px.bar(df_provincial, x='Cant_genero', y='Genero', color='Genero', color_discrete_map=colores_partido, orientation='h', text='Cant_genero',
                                            title=f'Distribución por género de electores en {prov_select_electores}')
                    fig_partidos_prov.update_traces(textposition='outside', textfont_color='black', texttemplate='%{text:,.2s}')
                    fig_partidos_prov.update_yaxes(title='Género', fixedrange=True)
                    fig_partidos_prov.update_xaxes(title='Cantidad', fixedrange=True)
                    fig_partidos_prov.update_layout(showlegend=False, template='simple_white')  
                    fig_partidos_prov.update_traces(hovertemplate='Genero: %{y}<br>Electores: %{x}<br>', hoverlabel=dict(namelength=0))
                    #st.plotly_chart(fig_partidos_prov, use_container_width=True)

                    df_generos_alt = df_provincial2
                    df_generos_alt['Porc_genero'] = df_generos_alt['Porc_genero'].replace({'X_Percentage': '% No Binario','M_Percentage': '% Masculino', 'F_Percentage': "% Femenino"})
                    fig_partidos_prov_porc = px.bar(df_generos_alt, x='Cant_porc_genero', y='Porc_genero', color='Porc_genero', color_discrete_map=colores_partido, orientation='h', text='Cant_porc_genero',
                                            title=f'Distribución por género de electores en {prov_select_electores}')
                    fig_partidos_prov_porc.update_traces(textposition='outside', textfont_color='black')
                    fig_partidos_prov_porc.update_yaxes(title='Género', fixedrange=True)
                    fig_partidos_prov_porc.update_xaxes(title='Porcentaje', fixedrange=True)
                    fig_partidos_prov_porc.update_layout(showlegend=False, template='simple_white')  
                    fig_partidos_prov_porc.update_traces(hovertemplate='Genero: %{y}<br>Porcentaje: %{x}<br>', hoverlabel=dict(namelength=0))
                    #st.plotly_chart(fig_partidos_prov_porc, use_container_width=True)

                    boton_productos2 = st.radio(
                    "Elegir tipo de distribución",
                    ('Por totales', 'Por porcentaje'), horizontal=True,label_visibility='collapsed')

                    if boton_productos2 == 'Por totales':
                        st.plotly_chart(fig_partidos_prov, use_container_width=True, config=config)
                    else:
                        st.plotly_chart(fig_partidos_prov_porc, use_container_width=True, config=config)

                    #prov_select_electores2 = st.selectbox("Filtrar resultados por distrito:",
                    #                                        electores_anio['DISTRITO'].unique()
                    #                                        )
                    df_anios = electores_anio.query('DISTRITO == @prov_select_electores')
                    df_grupo_etario = electores_grupo_etario.query('DISTRITO == @prov_select_electores')           
                    df_anios['CLASE']  = 2023 - df_anios['CLASE']

                    boton_productos3 = st.radio(
                    "Elegir tipo de distribuciosadaasn",
                    ('Por edad', 'Por grupo etario'), horizontal=True,label_visibility='collapsed')

                    fig_electores_anio = px.histogram(df_anios, x='CLASE', y='ELECTORES', color_discrete_sequence=['#453b84'], title=f'Distribución de los electores por edad en {prov_select_electores}', hover_data=None, nbins=100)
                    fig_electores_anio.update_xaxes(title='Edad', fixedrange=True)
                    fig_electores_anio.update_yaxes(title='Cantidad electores', fixedrange=True)
                    fig_electores_anio.update_layout(showlegend=False, template='simple_white')  

                    df_grupo_etario['GRUPO'] = df_grupo_etario['GRUPO'].replace('1953-anteriores', '+ 70')
                    df_grupo_etario['GRUPO'] = df_grupo_etario['GRUPO'].replace('1954-1963', '60-69')
                    df_grupo_etario['GRUPO'] = df_grupo_etario['GRUPO'].replace('1964-1973', '50-59')
                    df_grupo_etario['GRUPO'] = df_grupo_etario['GRUPO'].replace('1974-1983', '40-49')
                    df_grupo_etario['GRUPO'] = df_grupo_etario['GRUPO'].replace('1984-1993', '30-39')
                    df_grupo_etario['GRUPO'] = df_grupo_etario['GRUPO'].replace('1994-2005', '18-29')
                    df_grupo_etario['GRUPO'] = df_grupo_etario['GRUPO'].replace('2006-2007', '16-17')

                    fig_electores_grupo_etario = px.bar(df_grupo_etario, x='GRUPO', y='ELECTORES', 
                                                            title=f'Distribución de los electores por grupo etario en {prov_select_electores}', text='Percentage')
                    fig_electores_grupo_etario.update_traces(texttemplate='%{text:.1f}%', textposition='outside', marker_color='#453b84')
                    fig_electores_grupo_etario.update_xaxes(title='Grupo Etario', fixedrange=True)
                    fig_electores_grupo_etario.update_yaxes(title='Cantidad electores', fixedrange=True)
                    fig_electores_grupo_etario.update_layout(showlegend=False, template='simple_white')  

                    if boton_productos3 == 'Por edad':
                        st.plotly_chart(fig_electores_anio, use_container_width=True, config=config)
                    else:
                        st.plotly_chart(fig_electores_grupo_etario, use_container_width=True, config=config)

        # tabla_csv.rename(columns={"Num_dist": "ID Distrito", "Name": "Distrito","Porcentaje": "Porcentaje Electores","NoBinario": "No Binario",
        #                         "M_Percentage": "M_Porcentaje", "F_Percentage": "F_Porcentaje", "X_Percentage": "NB_Porcentaje"}, inplace=True)
        # tabla_csv2=tabla_csv[['ID Distrito', 'Distrito', 'Electores', 'Porcentaje Electores', 'Mesas', 'Secciones', 'Circuitos', 'Femenino', 'Masculino',
        #                     'No Binario', 'F_Porcentaje', 'M_Porcentaje', 'NB_Porcentaje']]
        
        # st.dataframe(df_grupo_etario, use_container_width=True)
        # st.dataframe(tabla_csv2, hide_index=True, use_container_width=True)
        # def convert_df(tabla_csv2):
        #                 return tabla_csv2.to_csv(index=False).encode('utf-8')
                        
        # csv2 = convert_df(tabla_csv2)

        # st.download_button(
        #                 "Descargar tabla como archivo CSV",
        #                 csv2,
        #                 "tabla_electores.csv",
        #                 "text/csv",
        #                 key='download-csv'
        #                 )
