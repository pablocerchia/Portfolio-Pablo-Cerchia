import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import datetime
import streamlit.components.v1 as components
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode
import streamlit_antd_components as sac

# st.set_page_config(page_title = 'Elecciones 2023 - Sitio de consulta',
#                     layout='wide', initial_sidebar_state='collapsed')
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
### DIPUTADOS

def diputados():

    df2023_v2 = pd.read_csv("data/distribucionGEN_diputados.csv")
    lista_DIPUTADOS_candidatos = pd.read_csv("data/listadiputadosCANDIDATOS.csv")
    encabezan_DIPUTADOS_candidatos = pd.read_csv("data/encabezanDIPUTADOSgenero.csv")
    lista_DIPUTADOS = pd.read_csv("data/bancas/TABLA_LIMPIA_DIPUTADOS257.csv")
    finalizan_mandato_DIPUTADOS = pd.read_csv("data/bancas/terminan_mandato_diputados.csv")
    finalizan_mandato_BLOQUE_DIPUTADOS = pd.read_csv("data/bancas/renovacion_x_bloque.csv")
    finalizan_mandato_INTERBLOQUE_DIPUTADOS = pd.read_csv('data/bancas/renovacion_interbloque.csv')
    lista_DIPUTADOS = lista_DIPUTADOS[['Apellido', 'Nombre', 'Distrito', 'Bloque', 'INTERBLOQUE','IniciaMandato', 'FinalizaMandato']]
    finalizan_mandato_DIPUTADOS = finalizan_mandato_DIPUTADOS[['INTERBLOQUE','Bloque','Apellido', 'Nombre', 'Distrito', 'IniciaMandato', 'FinalizaMandato']]

    #st.markdown("<h1 style='text-align: center;'>Composición y proyección de las Cámaras de Diputados y Senadores</h1>", unsafe_allow_html=True)



    tab_titles_dip = [
                    "Por interbloque",
                    "Por bloque",
    ]


    #tabs_sac = sac.buttons(['Diputados','Senadores'], label=None, index=0, format_func='title', align='center', position='top', size='default', direction='horizontal', shape='round', compact=True, return_index=False)
    #tabs_sac = sac.tabs(['Diputados','Senadores'], index=0, format_func='title', height=None, align='center', position='top', shape='default', grow=True, return_index=False)

    #if tabs_sac == 'Diputados':

    c4, c5, c6 = st.columns([0.1, 0.8, 0.1])

    with c5:

        st.markdown("<h3 style='text-align: center;'>Qué vas a poder encontrar en esta sección<br></h3>", unsafe_allow_html=True)
        st.markdown(
                    """
                    <div style="text-align:center; font-size: 1.5em;">Consultá y compará cómo le fue a las agrupaciones y a los candidatos a nivel diputados en cada provincia y sección electoral del país. A su vez podrás <a href='#proyect-cu-ntas-bancas-ganar-a-cada-partido-en-tu-provincia'>proyectar cuántas bancas ganaría cada partido</a> en las elecciones generales. Acá vas a poder informarte sobre cómo se compone la Cámara, <a href='#informate-sobre-los-candidatos-de-cada-agrupaci-n'>quién compone cada lista</a>, <a href='#qui-nes-terminan-su-mandato-en-2023'>quiénes terminan su mandato en 2023</a> y <a href='#qui-nes-componen-actualmente-la-c-mara-de-diputados'>quiénes son sus miembros actuales</a>. 
                    <br>También vas a poder comparar <a href='#distribuci-n-por-edad-y-o-g-nero-de-los-candidatos'>la distribución de género y edad en las listas</a> de cada agrupación, 
                    sumado a ver <a href='#qui-n-encabeza-m-s-las-listas-en-cada-agrupaci-n'>cuál género es el que encabeza más listas</a> en cada partido.</div>
                    """,
                    unsafe_allow_html=True
                    )
        sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='1667')
        st.markdown("<h5 style='text-align: center;'><br></h5>", unsafe_allow_html=True)
        #st.markdown("<h1 style='text-align: center;'>Así está y así quedaría la Cámara de Diputados</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'>EL PRESENTE Y FUTURO DE LA CÁMARA DE DIPUTADOS<br></h3>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center; font-weight: normal;'>Mirá cómo está compuesta hoy la cámara y cómo quedaría conformada si se repiten los resultados en octubre.<br></h5>", unsafe_allow_html=True)
        #st.markdown("<h3 style='text-align: center;'>Mirá cómo está compuesta hoy la cámara y cómo quedaría conformada si se repiten los resultados en octubre.</h3>", unsafe_allow_html=True)
        c412, c533, c645 = st.columns([0.2, 0.6, 0.2])
        with c533:
            components.html("""<div class="flourish-embed flourish-parliament" data-src="visualisation/14778887"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=900)
        
        sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='112')
        st.markdown("<h3 style='text-align: center;'>CONSULTÁ LOS RESULTADOS EN CADA PROVINCIA<br></h3>", unsafe_allow_html=True)
        #st.markdown("<h1 style='text-align: center;'>Consultá los resultados en cada provincia</h1>", unsafe_allow_html=True)
        tabs44 = sac.buttons(['Por agrupación','Por candidato'], label=None, index=0, format_func=None, align='center', position='top', size='large', direction='horizontal', shape='round', compact=False, return_index=False, key=887)
        #tabs_sac = sac.buttons(['Por provincia','Por sección'], label=None, index=0, format_func=None, align='center', position='top', size='default', direction='horizontal', shape='round', compact=True, return_index=False, key=888)
        boton_depto_seccion1 = sac.buttons(['Por provincia','Por sección'], label=None, index=0, format_func=None, align='center', position='top', size='default', direction='horizontal', shape='round', compact=True, return_index=False, key=889)
        if tabs44 == 'Por agrupación':
            if boton_depto_seccion1 == 'Por provincia':
                components.html("""<div class="flourish-embed" data-src="story/2025681" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=600)
            if boton_depto_seccion1 == 'Por sección':
                components.html("""<div class="flourish-embed" data-src="story/2026087" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=600)
        if tabs44 == 'Por candidato':
            if boton_depto_seccion1 == 'Por provincia':
                components.html("""<div class="flourish-embed" data-src="story/2035378" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=600)
            if boton_depto_seccion1 == 'Por sección':
                components.html("""<div class="flourish-embed" data-src="story/2035422" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=600)
        sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='111')
        
        st.subheader('¿Cómo se compone la Cámara?')
        st.write("La cámara está integrada por 257 diputados nacionales quienes representan directamente al pueblo de la Nación. Tienen mandatos de cuatro años y pueden ser reelegidos. Son elegidos utilizando el sistema de representación proporcional D'Hondt en cada uno de los 24 distritos autónomos que integran la federación (23 provincias y la Ciudad Autónoma de Buenos Aires). Cada dos años la Cámara renueva la mitad de sus miembros. Para dar quórum se necesitan 129 diputados. ", unsafe_allow_html=True)
        sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='4')
        st.subheader('Proyectá cuántas bancas ganaría cada partido en tu provincia')
        with st.expander("**¿Qué es el sistema de representación proporcional D'Hondt?**"):
            st.write("<br>Es una fórmula mediante la cual se determinan cuántas bancas se le asignará a cada partido político en cada distrito.", unsafe_allow_html=True)
            st.video('https://www.youtube.com/watch?v=kXbUXugLnlc')

        def formula_dhont(cant_bancas, votos):
            total_votes = sum(votos.values())
            votos_porcentaje = {partido: total_votes * (porcentaje / 100) for partido, porcentaje in votos.items()}
            
            lista = []
            for partido, votos_partido in votos_porcentaje.items():
                for bancas in range(1, cant_bancas + 1):
                    lista.append((votos_partido / bancas, partido))

            lista.sort(reverse=True)
            lista_final = lista[:cant_bancas]

            results = {}

            for l in lista_final:
                partido = l[1]
                results[partido] = results.get(partido, 0) + 1

            return results

        with st.expander("**Hacé tu propia proyección! Calculá cuántas bancas ganaría tu partido en las elecciones generales**"):

            st.write("<br> **Editá el nombre de los partidos y los porcentajes que podría sacar cada uno para calcular así cuántas bancas a diputados obtendría cada partido en las elecciones generales** <br>", unsafe_allow_html=True)
        
            states_seats = {"Buenos Aires": 35, "Capital Federal": 12,
                "Catamarca": 2,
                "Chaco": 3,
                "Chubut": 3,
                "Córdoba": 9,
                "Corrientes": 4,
                "Entre Ríos": 4,
                "Formosa": 3,
                "Jujuy": 3,
                "La Pampa": 2,
                "La Rioja": 3,
                "Mendoza": 2,
                "Misiones": 4,
                "Neuquén": 2,
                "Río Negro": 3,
                "Salta": 4,
                "San Juan": 3,
                "Santa Cruz": 2,
                "San Luis": 2,
                "Santiago del Estero": 4,
                "Santa Fe": 10,
                "Tierra del Fuego": 3,
                "Tucumán": 5,
                
            }
            
            selected_state = st.selectbox("Seleccione una provincia", list(states_seats.keys()))
            cant_bancas = states_seats[selected_state]
            
            num_parties = st.number_input("Cantidad de partidos", min_value=1, max_value=10, value=3)
            
            votos = {}
            total_percentage = 0  # Initialize total_percentage
            
            for i in range(1, num_parties + 1):
                partido = st.text_input(f"Partido {i}", f"Partido {chr(64+i)}", help='Podés editar el nombre del partido y el porcentaje')
                porcentaje = st.number_input(f"Porcentaje de votos para {partido}", min_value=0.1, max_value=100.0, value=30.0)
                
                # Update total_percentage
                total_percentage += porcentaje
                
                votos[partido] = porcentaje
            
            if total_percentage > 100:
                st.warning("El total de los porcentajes supera el 100%. Por favor corregir.")
            
            if st.button("Calcular"):
                results = formula_dhont(cant_bancas, votos)
                
                st.write("Distribución de Bancas:")
                for partido, bancas in results.items():
                    if bancas == 1:
                        st.write(f"{partido} obtendría {bancas} banca.")
                    elif bancas == 0:
                        st.write(f"{partido} no obtendría bancas.")
                    else:
                        st.write(f"{partido} obtendría {bancas} bancas.")
        
        sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='123')
        st.subheader("Informate sobre los candidatos de cada agrupación")
        st.write("Filtrá por distrito y por agrupación para averiguar quiénes componen las listas de diputados.", help="La tabla también es interactiva. Haciendo click derecho en una columna se puede seleccionar si filtrarla, moverla, achicarla, etc.")
        c4, c5, c6= st.columns(3)
        ######################################
        ####################### DROPDOWNS DE LA PRIMERA OPCION ####################### 
        st.markdown("""<style>.css-zt5igj svg{display:none}</style>""", unsafe_allow_html=True)
        

        with c4: 
            distrito = st.selectbox("Seleccione distrito:",
                                                lista_DIPUTADOS_candidatos['Distrito'].unique()
                                                )
            df_distrito = lista_DIPUTADOS_candidatos.query("Distrito == @distrito")

        with c5: 
            agrupacion = st.selectbox("Seleccione la agrupación política:",
                                                df_distrito['Agrupación Política'].unique())
            df_agrupacion = df_distrito.query("`Agrupación Política` == @agrupacion")
        with c6:
            lista = st.selectbox("Seleccione lista:",
                                                df_agrupacion['Lista'].unique()
                                                )
            df_lista = df_agrupacion.query("Lista == @lista")
        df_lista = df_lista[['Agrupación Política', 'Lista', 'Distrito','Precandidato', 'Subcategoría Cargo', 'Posición']]
        gd33 = GridOptionsBuilder.from_dataframe(df_lista)
        #gd.configure_pagination(enabled=True)
        #gd.configure_default_column(
        #resizable=True,
        #filterable=True,
        #sortable=True,
        #editable=False,)


        cellstyle_jscode = JsCode("""
            function(params){
                if (params.value == 'UNION POR LA PATRIA') {
                    return {
                        'color': 'black',
                        'backgroundColor' : '#01b5f0'
                }
                }
                if (params.value == 'JUNTOS POR EL CAMBIO') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#fcd201'
                    }
                }
                if (params.value == 'LA LIBERTAD AVANZA') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#695eb0'
                    }
                }
                if (params.value == 'FRENTE DE IZQUIERDA Y DE TRABAJADORES-UNIDAD') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#cd4137'
                    }
                }
                if (params.value == 'FRENTE DE IZQUIERDA Y DE TRABAJADORES') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#cd4137'
                    }
                }
                if (params.value == 'HACEMOS POR NUESTRO PAIS') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#7ec69b'
                    }
                }
                if (params.value == 'LIBER.AR') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#88e99a'
                    }
                }
                if (params.value == 'MOVIMIENTO AL SOCIALISMO') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#c11f1f'
                    }
                }
                if (params.value == 'FRENTE PATRIOTA FEDERAL') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#dc61e5'
                    }
                }
                if (params.value == 'MOVIMIENTO DE ACCION VECINAL') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#3e3c3c'
                    }
                }
                if (params.value == 'MOVIMIENTO IZQUIERDA JUVENTUD DIGNIDAD') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#909f41'
                    }
                }
                if (params.value == 'MOVIMIENTO LIBRES DEL SUR') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#d69405'
                    }
                }
                if (params.value == 'POLíTICA OBRERA') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#bc5938'
                    }
                }
                if (params.value == 'PRINCIPIOS Y VALORES') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#82e8dc'
                    }
                }
                if (params.value == 'PROYECTO JOVEN') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#25ef3c'
                    }
                }                                                                         
                else{
                    return{
                        'color': 'black',
                        'backgroundColor': 'lightpink'
                    }
                }

        };
        """)
        gd33.configure_columns('Agrupación Política', cellStyle=cellstyle_jscode)
        gridOptions33 = gd33.build()
        grid_table = AgGrid(df_lista, 
                gridOptions = gridOptions33, 
                enable_enterprise_modules = True,
                fit_columns_on_grid_load = True,
                height=400,
                width='100%',
                allow_unsafe_jscode=True,
                )

        
        sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='1')
        st.subheader("Distribución por edad y/o género de los candidatos")
        c11, c22, c33= st.columns(3)

        with c11:
            distritos = st.selectbox("Seleccionar distrito:",
                                                    df2023_v2['Distrito'].unique()
                                                    )
            df_distrito = df2023_v2.query('Distrito == @distritos')
        with c22:
            agrupaciones = st.selectbox("Seleccionar la agrupación política:",
                                                df_distrito['Agrupación Política'].unique()
                                                )
            df_agrupaciones = df_distrito.query('`Agrupación Política` == @agrupaciones')
        with c33: 
            lista = st.selectbox("Seleccionar lista:",
                                                df_agrupaciones['Lista'].unique()
                                                )
            df_lista = df_agrupaciones.query("Lista == @lista")

            colores_genero = {
            'Masculino': '#0f203a',
            'Femenino': '#f39a58'
        }
            colores_genero2 = {
            'Femenino': '#0f203a',
            'Masculino': '#0f203a'
        }

        #age_range_gender_counts = df_agrupaciones.groupby(['Age_Range', 'Genero']).size().unstack().reset_index()
        df_lista['Totales'] = 1
        df_lista['Género'] = df_lista['Género'].replace({'M': 'Masculino', 'F': 'Femenino'})
        age_range_gender_counts = df_lista.groupby(['Age_Range', 'Género'])['Totales'].sum().reset_index()
        age_range_gender_counts2 = df_lista.groupby(['Age_Range'])['Totales'].sum().reset_index()
        gender_counts = df_lista.groupby(['Género'])['Totales'].sum().reset_index()
        barras, pie = st.columns(2)

        tabs_gen = [
                    "Por edad y género",
                    "Por edad",
                    "Por género"]
        tabs_gen2 = [
                    "Por edad y género",
                    "Por edad","Por género"]


        fig = px.bar(age_range_gender_counts, x='Age_Range', y='Totales', color=age_range_gender_counts['Género'], color_discrete_map=colores_genero, text=age_range_gender_counts['Totales'])
        fig.update_traces(textposition='outside', textfont_color='black')
        fig.update_xaxes(type='category', ticks="outside", ticklen=5, tickcolor='rgb(195,186,178)', linecolor='rgb(203,193,185)', title='Grupo etario')
        fig.update_yaxes(anchor="free", shift= -10, gridcolor="rgb(228,217,208)", title='Cantidad')
        fig.update_yaxes(dtick=1)
        fig.update_layout(barmode='group', template='simple_white',            
                title=f"<b>DISTRIBUCIÓN DIPUTADOS NACIONALES DE {agrupaciones} EN {distritos}</b><br><sup>Lista: {lista} - Elecciones PASO 2023</sup>")
            
        fig_edad = px.bar(age_range_gender_counts2, x='Age_Range', y='Totales', text=age_range_gender_counts2['Totales'])
        fig_edad.update_traces(textposition='outside', textfont_color='black', marker=dict(color='#254f8f'))
        fig_edad.update_xaxes(type='category', ticks="outside", ticklen=5, tickcolor='rgb(195,186,178)', linecolor='rgb(203,193,185)', title='Grupo etario')
        fig_edad.update_yaxes(anchor="free", shift= -10, gridcolor="rgb(228,217,208)", title='Cantidad')
        fig_edad.update_layout(barmode='group', template='simple_white',            
                title=f"<b>DIPUTADOS NACIONALES DE {agrupaciones} EN {distritos}</b><br><sup>Lista: {lista} - Elecciones PASO 2023</sup>")
            
        tabs1, tabs2, tabs3 = st.tabs(tabs_gen)

            #boton_productos = st.radio(
                #"Elegir tipo de gráfico",
                #('Por edad y genero', 'Por edad'), horizontal=True,label_visibility='collapsed')

        with tabs1:
                st.plotly_chart(fig, use_container_width=True)
        with tabs2:
                st.plotly_chart(fig_edad, use_container_width=True)
        with tabs3:
            fig3 = px.bar(gender_counts, x='Género', y='Totales', color=gender_counts['Género'], color_discrete_map=colores_genero, text=gender_counts['Totales'])
            fig3.update_traces(textposition='outside', textfont_color='black')
            #fig_totales_genero.update_xaxes(type='category', ticks="outside", ticklen=5, tickcolor='rgb(195,186,178)', linecolor='rgb(203,193,185)', title='Grupo etario')
            #fig_totales_genero.update_yaxes(anchor="free", shift= -10, gridcolor="rgb(228,217,208)", title='Cantidad')
            #fig_totales_genero.update_xaxes(tickmode='array',tickvals=[0.5, 1], ticktext=gender_counts2['Genero'])
            fig3.update_layout(barmode='stack', template='simple_white',            
            title=f'GÉNERO DE DIPUTADOS NACIONALES DE {agrupaciones} EN {distritos}<br><sup>Lista: {lista} - Elecciones PASO 2023</sup>')
            st.plotly_chart(fig3, use_container_width=True)

        totales_candidatos = df2023_v2 
        totales_candidatos['Totales'] = 1
        totales_candidatos['Género'] = totales_candidatos['Género'].replace({'M': 'Masculino', 'F': 'Femenino'})
        totales_gen_edad = totales_candidatos.groupby(['Age_Range', 'Género'])['Totales'].sum().reset_index()
        totales_edad = totales_candidatos.groupby(['Age_Range'])['Totales'].sum().reset_index()
        gender_counts2 = totales_candidatos.groupby(['Género'])['Totales'].sum().reset_index()
        sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='222')
        st.subheader("¿Quién encabeza más las listas en cada agrupación?")
        st.write("Si bien según la Ley de Paridad de Género en Ámbitos de Representación Política (Ley 27.412) es obligatorio ubicar de manera intercalada mujeres y varones desde el primer candidato hasta el último candidato suplente, la disparidad de género sigue siendo posible porque las listas pueden estar predominantemente encabezadas por varones de manera legal.")

        enc1, enc2, enc3= st.columns(3)
        custom_order = ['JUNTOS POR EL CAMBIO','UNION POR LA PATRIA', 'LA LIBERTAD AVANZA', 'HACEMOS POR NUESTRO PAIS']

        encabezan = encabezan_DIPUTADOS_candidatos.sort_values(by=['Agrupación Política'], key=lambda x: x.map({v: i for i, v in enumerate(custom_order)}))
        
        with enc1:
            ap_encabeza = st.selectbox('Seleccionar agrupación política:', encabezan['Agrupación Política'].unique())
            encabezan_final = encabezan.query('`Agrupación Política`== @ap_encabeza')
            
        #     encabezan_sliced = encabezan_sliced.sort_values(by=['Agrupación Política'], key=lambda x: x.map({v: i for i, v in enumerate(custom_order)}))
        # with enc2:
        #     ap_encabeza = st.selectbox('Seleccionar agrupación política:', encabezan_sliced['Agrupación Política'].unique())
        #     encabezan_final = encabezan_sliced.query('`Agrupación Política`== @ap_encabeza')
        #     #lista_sliced = st.selectbox('Seleccionar lista:', encabezan_sliced['Lista'].unique())
        #     #encabezan_final = encabezan_sliced.query('Lista == @lista_sliced')


        encabezan_final['Contador'] = 1
        encabezan_final_plot = encabezan_final.groupby(['Género'])['Contador'].sum().reset_index()

        fig_encabezan = px.bar(encabezan_final_plot, x='Género', y='Contador', color=encabezan_final_plot['Género'], color_discrete_map=colores_genero, text=encabezan_final_plot['Contador'])
        fig_encabezan.update_traces(textposition='outside', textfont_color='black')
        fig_encabezan.update_xaxes(type='category', ticks="outside", ticklen=5, tickcolor='rgb(195,186,178)', linecolor='rgb(203,193,185)', title='Grupo etario')
        fig_encabezan.update_yaxes(anchor="free", shift= -10, gridcolor="rgb(228,217,208)", title='Cantidad')
        fig_encabezan.update_layout(barmode='stack', template='simple_white',            
                title=f"<b>DISTRIBUCIÓN DE GÉNERO EN LAS LISTAS DE {ap_encabeza} </b><br><sup>Según qué género las encabeza - Elecciones PASO 2023</sup>")
        st.plotly_chart(fig_encabezan, use_container_width=True)
        #sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='232')
        #st.subheader('¿Qué es un bloque y un interbloque?', anchor=False)
        #st.write("Un bloque es un conjunto de legisladores constituido de un modo formal generalmente a partir de afinidades políticas y/o partidarias. Mientras que un interbloque es una asociación de un conjunto de diversos bloques a partir de afinidades políticas y/o partidarias. No están definidos en el reglamento, pero refieren a grupos de bloques unidos por afinidades o frentes de coalición.")
        sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='2')
        st.subheader('¿Quiénes terminan su mandato en 2023?')
        st.write("Los siguientes diputados son quienes finalizan su mandato. A su vez, se puede observar cuantas bancas renueva cada bloque.")
        finalizan_mandato_DIPUTADOS = finalizan_mandato_DIPUTADOS.sort_values(by='INTERBLOQUE')
        gd = GridOptionsBuilder.from_dataframe(finalizan_mandato_DIPUTADOS)
        #gd.configure_pagination(enabled=True)
        #gd.configure_default_column(
        #resizable=True,
        #filterable=True,
        #sortable=True,
        #editable=False,)


        cellstyle_jscode = JsCode("""
            function(params){
                if (params.value == 'FRENTE DE TODOS') {
                    return {
                        'color': 'black',
                        'backgroundColor' : '#01b5f0'
                }
                }
                if (params.value == 'JUNTOS POR EL CAMBIO') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#fcd201'
                    }
                }
                if (params.value == 'PROVINCIAS UNIDAS') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#fa7900'
                    }
                }
                if (params.value == 'FEDERAL') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#043cbe'
                    }
                }
                if (params.value == 'SER - SOMOS ENERGÍA PARA RENOVAR') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#007d8e'
                    }
                }                                                                       
                else{
                    return{
                        'color': 'black',
                        'backgroundColor': 'lightpink'
                    }
                }
        
        };
        """)
        gd.configure_columns('INTERBLOQUE', cellStyle=cellstyle_jscode)
        gridOptions = gd.build()
        grid_table = AgGrid(finalizan_mandato_DIPUTADOS, 
                gridOptions = gridOptions, 
                enable_enterprise_modules = True,
                fit_columns_on_grid_load = True,
                height=400,
                width='100%',
                allow_unsafe_jscode=True,
                )


        #st.dataframe(finalizan_mandato_DIPUTADOS, hide_index=True, use_container_width=True)

        tabs_dip = st.tabs(tab_titles_dip)

        colores_partido = {
        'FRENTE DE TODOS': '#01b5f0',
        'JUNTOS POR EL CAMBIO': '#fcd201',
        'FEDERAL': '#043cbe',
        'PROVINCIAS UNIDAS': '#fa7900',
        'SER - SOMOS ENERGÍA PARA RENOVAR': '#007d8e',
                }
        colores_bloque = {
        'FRENTE DE TODOS': '#01b5f0',
        'PRO': '#fcd201',
        'UCR': '#730000',
        'ENCUENTRO FEDERAL': '#043cbe',
        'SER - SOMOS ENERGÍA PARA RENOVAR': '#007d8e',
                }
        config = {'displayModeBar': False}
        with tabs_dip[0]:
            fig_bloques_dip2 = px.bar(finalizan_mandato_INTERBLOQUE_DIPUTADOS, x='cantidad', y='Interbloque', color='Interbloque', color_discrete_map=colores_partido, orientation='h', text='cantidad',
                                        title=f'Renovación de bancas por interbloque')
            fig_bloques_dip2.update_traces(textposition='outside', textfont_color='black')
                #fig_partidos_prov.update_yaxes(type='category', ticks="outside", ticklen=5, tickcolor='rgb(195,186,178)', linecolor='rgb(203,193,185)')
                #fig_partidos_prov.update_xaxes(anchor="free", shift= -10, gridcolor="rgb(228,217,208)")
            fig_bloques_dip2.update_layout(showlegend=False, template='simple_white')  
            fig_bloques_dip2.update_traces(hovertemplate='Interbloque: %{y}<br>Bancas a renovar: %{x}<br>', hoverlabel=dict(namelength=0))
            fig_bloques_dip2.update_yaxes(title="", fixedrange=True)
            fig_bloques_dip2.update_xaxes(title="", fixedrange=True)
            st.plotly_chart(fig_bloques_dip2, use_container_width=True, config=config)

        with tabs_dip[1]:
            
                fig_bloques_dip = px.bar(finalizan_mandato_BLOQUE_DIPUTADOS, x='cantidad', y='Bloque', color='Bloque', color_discrete_map=colores_bloque, orientation='h', text='cantidad',
                                            title=f'Renovación de bancas por bloque')
                fig_bloques_dip.update_traces(textposition='outside', textfont_color='black')
                    #fig_partidos_prov.update_yaxes(type='category', ticks="outside", ticklen=5, tickcolor='rgb(195,186,178)', linecolor='rgb(203,193,185)')
                    #fig_partidos_prov.update_xaxes(anchor="free", shift= -10, gridcolor="rgb(228,217,208)")
                fig_bloques_dip.update_layout(showlegend=False, template='simple_white')  
                fig_bloques_dip.update_traces(hovertemplate='Bloque: %{y}<br>Bancas a renovar: %{x}<br>', hoverlabel=dict(namelength=0))
                fig_bloques_dip.update_yaxes(title="", fixedrange=True)
                fig_bloques_dip.update_xaxes(title="", fixedrange=True)
                st.plotly_chart(fig_bloques_dip, use_container_width=True, config=config)

        sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='3')
        st.subheader('¿Quiénes componen actualmente la Cámara de Diputados?')
        st.write("Esta es una tabla que contiene a todos los diputados actuales. Más abajo podrás filtrar la tabla para ver la distribución por provincia, interbloque, etc.")

        #st.dataframe(lista_DIPUTADOS, hide_index=True, use_container_width=True)
        #@st.cache_data
        #def convert_df(df_presi2):
                    #return df_presi2.to_csv(index=False).encode('utf-8')
                
        #csv2 = convert_df(lista_DIPUTADOS)

        #st.download_button(
                #"Descargar tabla como archivo CSV",
                #csv2,
                #"lista_diputados.csv",
                #"text/csv",
                #key='download-csv44'
                #)       
        
        sb10, sb12= st.columns(2)
        lista_DIPUTADOS = lista_DIPUTADOS.sort_values(by='Distrito')
        with sb10:
            provincia_diputado = st.selectbox('Provincia', lista_DIPUTADOS['Distrito'].unique())
            df11 = lista_DIPUTADOS.query('Distrito == @provincia_diputado')
            df11 = df11.sort_values(by='INTERBLOQUE')
        with sb12:
            interbloque_diputado = st.multiselect('Interbloque', df11['INTERBLOQUE'].unique(), default=df11['INTERBLOQUE'].unique())
            lista_diputados_final = df11.query('INTERBLOQUE == @interbloque_diputado')
        lista_diputados_final = lista_diputados_final[['INTERBLOQUE', 'Bloque', 'Apellido', 'Nombre', 'Distrito', 'IniciaMandato', 'FinalizaMandato']]
        #lista_diputados_final = lista_diputados_final.sort_values(by='INTERBLOQUE')
        gd2 = GridOptionsBuilder.from_dataframe(finalizan_mandato_DIPUTADOS)
        #gd.configure_pagination(enabled=True)
        #gd.configure_default_column(
        #resizable=True,
        #filterable=True,
        #sortable=True,
        #editable=False,)


        cellstyle_jscode = JsCode("""
            function(params){
                if (params.value == 'FRENTE DE TODOS') {
                    return {
                        'color': 'black',
                        'backgroundColor' : '#01b5f0'
                }
                }
                if (params.value == 'JUNTOS POR EL CAMBIO') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#fcd201'
                    }
                }
                if (params.value == 'PROVINCIAS UNIDAS') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#fa7900'
                    }
                }
                if (params.value == 'FEDERAL') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#043cbe'
                    }
                }
                if (params.value == 'SER - SOMOS ENERGÍA PARA RENOVAR') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#007d8e'
                    }
                }
                if (params.value == 'FRENTE DE IZQUIERDA Y DE TRABAJADORES - UNIDAD') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#cd4137'
                    }
                }
                if (params.value == 'BUENOS AIRES LIBRE') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#695eb0'
                    }
                }
                if (params.value == 'LA LIBERTAD AVANZA') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#695eb0'
                    }
                }
                if (params.value == 'MOVIMIENTO POPULAR NEUQUINO') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#019c00'
                    }
                }                                                                            
                else{
                    return{
                        'color': 'black',
                        'backgroundColor': 'lightpink'
                    }
                }
        
        };
        """)
        gd2.configure_columns('INTERBLOQUE', cellStyle=cellstyle_jscode)
        gridOptions2 = gd2.build()
        grid_table = AgGrid(lista_diputados_final, 
                gridOptions = gridOptions2, 
                enable_enterprise_modules = True,
                fit_columns_on_grid_load = True,
                height=400,
                width=700,
                allow_unsafe_jscode=True,
                )
        #st.dataframe(lista_diputados_final, hide_index=True, use_container_width=True)
        sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='5')
        st.subheader('Si querés saber más sobre la Cámara de Diputados...', anchor=False)

        with st.expander('**¿Qué es el Congreso? Diferencia entre Diputados y Senadores**'):
            st.write("El Congreso de la Nación Argentina es el órgano en el cual se ejerce uno de los tres poderes del Estado, el Poder Legislativo, engranaje de nuestro sistema de gobierno representativo, republicano y federal. Dicho Poder está integrado por dos cámaras: la Cámara de Diputados y la Cámara de Senadores, que tienen su sede en el edificio del Palacio del Congreso Nacional. Se trata de un cuerpo deliberativo. Los integrantes de cada una de las Cámaras son elegidos por el voto popular en sufragio universal, secreto y obligatorio.<br><br> **Integrantes:** de la Cámara de Diputados en la actualidad son 257 y representan a los ciudadanos en cuanto a atender y defender sus intereses, son elegidos utilizando el sistema de representación proporcional D'Hondt. A la Cámara de Diputados se la denomina coloquialmente como “la casa del pueblo” “Cámara Baja”. Mientras que a la Cámara de Senadores se la denomina “Cámara Alta”, y los senadores actualmente 72, representan los intereses de las provincias. Son elegidos 3 senadores por provincia y 3 por la Ciudad Autónoma de Buenos Aires.<br><br> **Requisitos:** Para ser diputado un ciudadano debe haber cumplido la edad de veinticinco años, tener cuatro años de ciudadanía en ejercicio, y ser natural de la provincia que lo elija, o con dos años de residencia inmediata en ella. Para ser Senador debe tener la edad de treinta años, haber sido seis años ciudadano de la Nación, y ser natural de la provincia que lo elija, o con dos años de residencia inmediata en ella.<br><br> **Mandato y Renovación de Cámara:** cuatro son los años de mandato de un diputado y la Cámara se renueva por mitad cada dos años, mientras que la Cámara de Senadores se renueva por tercios cada dos años y los senadores tienen un mandato de 6 años. Presidencias de las Cámaras; en la Cámara de Diputados el Presidente/a es un Diputado/a que a propuesta de los Bloques Parlamentarios es elegido por el voto de la mayoría en Sesión Preparatoria, los usos y costumbres dan la Presidencia de la Cámara al partido oficialista. Mientras que la Cámara de Senadores la preside el/la Vicepresidente/a de la Nación.", unsafe_allow_html=True)
        with st.expander('**Funciones**'):
            st.write("Conforme a lo dispuesto en la Constitución Nacional, son competencias específicas de la Cámara de Diputados:<br><br>- Recibir los proyectos de Ley presentados por iniciativa popular (CN Art.39)<br><br>- Iniciar el proceso de consulta popular para un proyecto de ley (CN Art. 40)<br><br>- Iniciar las leyes sobre contribuciones y reclutamiento de tropas (CN Art. 52)<br><br>- Acusar ante el Senado, en juicio político, al presidente y vicepresidente de la Nación, al jefe de Gabinete de ministros, a ministros del Poder Ejecutivo y a miembros de la Corte Suprema (CN Art. 53)", unsafe_allow_html=True)
        with st.expander('**¿Qué hace un diputado?**'):
            st.write("La función específica de un Diputado es legislar, representando los intereses del pueblo que lo llevó a ocupar una banca en el Congreso de la Nación, velar por sus intereses, y adecuar la legislación vigente o proponer nuevas alternativas. Para cumplir su cometido debe asesorarse, investigar, comparar legislaciones, asistir a las reuniones de comisión y ser partícipe de las Sesiones del pleno. Como así también comprometerse con su voto conforme a sus convicciones.", unsafe_allow_html=True)
        with st.expander('**Bloques e interbloques**'):
            st.write("El reglamento de la Cámara de Diputados en su artículo 55 define: “Los grupos de tres o más diputados podrán organizarse en bloques de acuerdo con sus afinidades políticas. Cuando un partido político existente con anterioridad a la elección de los diputados tenga sólo uno o dos diputados en la Cámara, podrán ellos asimismo actuar como bloque.”<br><br>Los bloques tienen un Presidente, que es un diputado/a que los representa ante el pleno y es nexo con la presidencia de la Cámara, también cuentan con un Vicepresidente y un Secretario todos ellos legisladores, internamente cuentan con un Secretario Parlamentario de bloque, y uno Administrativo estos últimos no legisladores.<br><br>Hace unos años estos Bloques políticos se comenzaron a agrupar en Interbloques, siguiendo el criterio de afinidad política, lo que no está reglamentado al día de la fecha.", unsafe_allow_html=True)
        with st.expander('**Comisiones**'):
            st.write("Las comisiones legislativas son órganos de asesoramiento existentes en ambas Cámaras del Congreso de la Nación. Estan integradas por legísladores, asesores y personal de planta. Su funcion es estudiar los proyectos de ley y producir dictámenes sobre los mismos. Pueden ser permanentes o especiales.", unsafe_allow_html=True)
        with st.expander('**Sesiones**'):    
            st.write("Se denomina sesión a la reunión del pleno de los diputados o senadores en recinto. Ambas Cámaras del Congreso inician su Período Parlamentario el 1 de marzo con la Asamblea Legislativa (reunión de Diputados y Senadores) en la que el Presidente de la Nación brinda al pleno el informe de gestión, y finaliza el 30 de noviembre, a este período se lo denomina de Sesiones Ordinarias, dentro del mismo las sesiones pueden ser “de tablas” o “especiales”. Fuera del período descripto, el presidente de la Nación tiene la facultad de convocar a Sesiones Extraordinarias, lo hace por decreto especificando el período de duración de las mismas y el temario a considerar, como así también puede prorrogar el período de sesiones ordinarias aquí las Cámaras continúan su normal funcionamiento.", unsafe_allow_html=True)
 
def senadores():   
    ### SENADORES
    df2023_v3 = pd.read_csv("data/distribucionGEN_senadores.csv")
    lista_SENADORES_candidatos = pd.read_csv("data/listasenadoresCANDIDATOS.csv")
    encabezan_SENADORES_candidatos = pd.read_csv("data/encabezanSENADORES.csv")
    lista_senadores = pd.read_csv("data/bancas/lista_senadores_CLEAN.csv")
    finalizan_mandato = pd.read_csv("data/bancas/terminan_mandato_SENADORES.csv")
    finalizan_mandato_bloque = pd.read_csv("data/bancas/terminan_mandato_SENADORES_BLOQUE.csv")
    finalizan_mandato = finalizan_mandato[['BLOQUE', 'APELLIDO', 'NOMBRE', 'PROVINCIA']]
    finalizan_mandato_bloque = finalizan_mandato_bloque[['Bloque', 'Cantidad']]
    lista_senadores = lista_senadores[['BLOQUE', 'APELLIDO', 'NOMBRE', 'PROVINCIA','Inicia_Mandato', 'Finaliza_Mandato']]
    lista_senadores2 = lista_senadores.copy()
    #if tabs_sac == 'Senadores':
    config = {'displayModeBar': False}
    c11, c242, c33 = st.columns([0.1, 0.8, 0.1])

    with c242:
        st.markdown("<h3 style='text-align: center;'>Qué vas a poder encontrar en esta sección<br></h3>", unsafe_allow_html=True)
        st.markdown(
                    """
                    <div style="text-align:center; font-size: 1.5em;">Consultá y compará cómo le fue a las agrupaciones y a los candidatos a nivel senadores en cada provincia y sección electoral del país. Acá vas a poder informarte sobre cómo se compone la Cámara, <a href='#informate-sobre-los-candidatos-de-cada-agrupaci-n'>quién compone cada lista</a>, <a href='#qui-nes-terminan-su-mandato-en-2023'>quiénes terminan su mandato en 2023</a> y <a href='#qui-nes-componen-actualmente-el-senado'>quiénes son sus miembros actuales</a>. 
                    También vas a poder comparar <a href='#distribuci-n-por-edad-y-o-g-nero-de-los-candidatos'>la distribución de género y edad en las listas</a> de cada agrupación, 
                    sumado a ver <a href='#cu-l-g-nero-encabeza-m-s-las-listas-en-cada-agrupaci-n'>cuál género es el que encabeza más listas</a> en cada partido.</div>
                    """,
                    unsafe_allow_html=True
                    )
        sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='66637')
        st.markdown("<h3 style='text-align: center;'>EL PRESENTE Y FUTURO DE LA CÁMARA DE SENADORES<br></h3>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center; font-weight: normal;'>Mirá cómo está compuesta hoy la cámara y cómo quedaría conformada si se repiten los resultados en octubre.<br></h5>", unsafe_allow_html=True)
        c412, c533, c645 = st.columns([0.2, 0.6, 0.2])
        with c533:
            components.html("""<div class="flourish-embed flourish-parliament" data-src="visualisation/14777971"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=700)
        sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='6667')
        st.markdown("<h3 style='text-align: center;'>CONSULTÁ LOS RESULTADOS EN CADA PROVINCIA<br></h3>", unsafe_allow_html=True)
        tabs245 = sac.buttons(['Por agrupación','Por candidato'], label=None, index=0, format_func=None, align='center', position='top', size='large', direction='horizontal', shape='round', compact=False, return_index=False, key=668)
        boton_depto_seccion = sac.buttons(['Por provincia','Por sección'], label=None, index=0, format_func=None, align='center', position='top', size='default', direction='horizontal', shape='round', compact=True, return_index=False, key=628)
        if tabs245 == 'Por agrupación':
            if boton_depto_seccion == 'Por provincia':
                components.html("""<div class="flourish-embed" data-src="story/2024729" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=600)
            if boton_depto_seccion == 'Por sección':
                components.html("""<div class="flourish-embed" data-src="story/2024910" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=600)
        if tabs245 == 'Por candidato':
            if boton_depto_seccion == 'Por provincia':
                components.html("""<div class="flourish-embed" data-src="story/2035174" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=600)
            if boton_depto_seccion == 'Por sección':
                components.html("""<div class="flourish-embed" data-src="story/2035426" data-height="600px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=600)
        sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='111')
        #st.title('Cámara de Senadores')
        
        st.subheader('¿Cómo se compone la Cámara?')
        st.write("La Cámara de Senadores se compone de 72 integrantes, los cuales tienen un mandato de seis años. tres por cada provincia y tres por la Ciudad Autónoma de Buenos Aires. Todos los distritos tienen igual representación. Corresponden dos bancas al partido mayoritario y una al que le sigue en cantidad de votos obtenidos. Cada dos años se renueva un tercio de la cámara, es decir, se renuevan 24 bancas. Formalmente los senadores están organizados por bloques, los cuales a su vez pueden formar alianzas entre sí (en el gráfico de arriba se visualizan las alianzas pero a continuación se tratará a cada bloque por separado). Para dar quórum se necesitan 37 senadores.")
        sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='6')
        ########################################################################################################################################
        st.subheader("Informate sobre los candidatos de cada agrupación")
        st.write("Filtrá por distrito y por agrupación para averiguar quiénes fueron los candidatos en tu distrito.", help="La tabla también es interactiva. Haciendo click derecho en una columna se puede seleccionar si filtrarla, moverla, achicarla, etc.")
        c4, c5, c6= st.columns(3)
        ######################################
        ####################### DROPDOWNS DE LA PRIMERA OPCION ####################### 
        st.markdown("""<style>.css-zt5igj svg{display:none}</style>""", unsafe_allow_html=True)
        

        with c4: 
            distrito = st.selectbox("Seleccione distrito:",
                                                lista_SENADORES_candidatos['Distrito'].unique()
                                                )
            df_distrito = lista_SENADORES_candidatos.query("Distrito == @distrito")

        with c5: 
            agrupacion = st.selectbox("Seleccione la agrupación política:",
                                                df_distrito['Agrupación Política'].unique())
            df_agrupacion = df_distrito.query("`Agrupación Política` == @agrupacion")
        with c6:
            lista = st.selectbox("Seleccione lista:",
                                                df_agrupacion['Lista'].unique()
                                                )
            df_lista = df_agrupacion.query("Lista == @lista")
        df_lista = df_lista[['Agrupación Política', 'Lista', 'Distrito','Precandidato', 'Subcategoría Cargo', 'Posición']]
        gd33 = GridOptionsBuilder.from_dataframe(df_lista)
        #gd.configure_pagination(enabled=True)
        #gd.configure_default_column(
        #resizable=True,
        #filterable=True,
        #sortable=True,
        #editable=False,)


        cellstyle_jscode = JsCode("""
            function(params){
                if (params.value == 'UNION POR LA PATRIA') {
                    return {
                        'color': 'black',
                        'backgroundColor' : '#01b5f0'
                }
                }
                if (params.value == 'JUNTOS POR EL CAMBIO') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#fcd201'
                    }
                }
                if (params.value == 'LA LIBERTAD AVANZA') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#695eb0'
                    }
                }
                if (params.value == 'FRENTE DE IZQUIERDA Y DE TRABAJADORES-UNIDAD') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#cd4137'
                    }
                }
                if (params.value == 'FRENTE DE IZQUIERDA Y DE TRABAJADORES') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#cd4137'
                    }
                }
                if (params.value == 'HACEMOS POR NUESTRO PAIS') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#7ec69b'
                    }
                }
                if (params.value == 'LIBER.AR') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#88e99a'
                    }
                }
                if (params.value == 'MOVIMIENTO AL SOCIALISMO') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#c11f1f'
                    }
                }
                if (params.value == 'FRENTE PATRIOTA FEDERAL') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#dc61e5'
                    }
                }
                if (params.value == 'MOVIMIENTO DE ACCION VECINAL') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#3e3c3c'
                    }
                }
                if (params.value == 'MOVIMIENTO IZQUIERDA JUVENTUD DIGNIDAD') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#909f41'
                    }
                }
                if (params.value == 'MOVIMIENTO LIBRES DEL SUR') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#d69405'
                    }
                }
                if (params.value == 'POLíTICA OBRERA') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#bc5938'
                    }
                }
                if (params.value == 'PRINCIPIOS Y VALORES') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#82e8dc'
                    }
                }
                if (params.value == 'PROYECTO JOVEN') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#25ef3c'
                    }
                }                                                                         
                else{
                    return{
                        'color': 'black',
                        'backgroundColor': 'lightpink'
                    }
                }

        };
        """)
        gd33.configure_columns('Agrupación Política', cellStyle=cellstyle_jscode)
        gridOptions33 = gd33.build()
        grid_table = AgGrid(df_lista, 
                gridOptions = gridOptions33, 
                enable_enterprise_modules = True,
                fit_columns_on_grid_load = True,
                height=160,
                width='100%',
                allow_unsafe_jscode=True,
                )

        
        sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='1')
        st.subheader("Distribución por edad y/o género de los candidatos")
        c11, c22, c33= st.columns(3)

        with c11:
            distritos = st.selectbox("Seleccionar distrito:",
                                                    df2023_v3['Distrito'].unique()
                                                    )
            df_distrito = df2023_v3.query('Distrito == @distritos')
        with c22:
            agrupaciones = st.selectbox("Seleccionar la agrupación política:",
                                                df_distrito['Agrupación Política'].unique()
                                                )
            df_agrupaciones = df_distrito.query('`Agrupación Política` == @agrupaciones')
        with c33: 
            lista = st.selectbox("Seleccionar lista:",
                                                df_agrupaciones['Lista'].unique()
                                                )
            df_lista = df_agrupaciones.query("Lista == @lista")

            colores_genero = {
            'Masculino': '#0f203a',
            'Femenino': '#f39a58'
        }
            colores_genero2 = {
            'Femenino': '#0f203a',
            'Masculino': '#0f203a'
        }

        #age_range_gender_counts = df_agrupaciones.groupby(['Age_Range', 'Genero']).size().unstack().reset_index()
        df_lista['Totales'] = 1
        df_lista['Género'] = df_lista['Género'].replace({'M': 'Masculino', 'F': 'Femenino'})
        age_range_gender_counts = df_lista.groupby(['Age_Range', 'Género'])['Totales'].sum().reset_index()
        age_range_gender_counts2 = df_lista.groupby(['Age_Range'])['Totales'].sum().reset_index()
        gender_counts = df_lista.groupby(['Género'])['Totales'].sum().reset_index()
        barras, pie = st.columns(2)

        tabs_gen = [
                    "Por edad y género",
                    "Por edad",
                    "Por género"]
        tabs_gen2 = [
                    "Por edad y género",
                    "Por edad","Por género"]


        fig = px.bar(age_range_gender_counts, x='Age_Range', y='Totales', color=age_range_gender_counts['Género'], color_discrete_map=colores_genero, text=age_range_gender_counts['Totales'])
        fig.update_traces(textposition='outside', textfont_color='black')
        fig.update_xaxes(type='category', ticks="outside", ticklen=5, tickcolor='rgb(195,186,178)', linecolor='rgb(203,193,185)', title='Grupo etario')
        fig.update_yaxes(anchor="free", shift= -10, gridcolor="rgb(228,217,208)", title='Cantidad')
        fig.update_yaxes(dtick=1)
        fig.update_layout(barmode='group', template='simple_white',            
                title=f"<b>DISTRIBUCIÓN DIPUTADOS NACIONALES DE {agrupaciones} EN {distritos}</b><br><sup>Lista: {lista} - Elecciones PASO 2023</sup>")
            
        fig_edad = px.bar(age_range_gender_counts2, x='Age_Range', y='Totales', text=age_range_gender_counts2['Totales'])
        fig_edad.update_traces(textposition='outside', textfont_color='black', marker=dict(color='#254f8f'))
        fig_edad.update_xaxes(type='category', ticks="outside", ticklen=5, tickcolor='rgb(195,186,178)', linecolor='rgb(203,193,185)', title='Grupo etario')
        fig_edad.update_yaxes(anchor="free", shift= -10, gridcolor="rgb(228,217,208)", title='Cantidad')
        fig_edad.update_layout(barmode='group', template='simple_white',            
                title=f"<b>DIPUTADOS NACIONALES DE {agrupaciones} EN {distritos}</b><br><sup>Lista: {lista} - Elecciones PASO 2023</sup>")
            
        tabs1, tabs2, tabs3 = st.tabs(tabs_gen)

            #boton_productos = st.radio(
                #"Elegir tipo de gráfico",
                #('Por edad y genero', 'Por edad'), horizontal=True,label_visibility='collapsed')

        with tabs1:
                st.plotly_chart(fig, use_container_width=True)
        with tabs2:
                st.plotly_chart(fig_edad, use_container_width=True)
        with tabs3:
            fig3 = px.bar(gender_counts, x='Género', y='Totales', color=gender_counts['Género'], color_discrete_map=colores_genero, text=gender_counts['Totales'])
            fig3.update_traces(textposition='outside', textfont_color='black')
            #fig_totales_genero.update_xaxes(type='category', ticks="outside", ticklen=5, tickcolor='rgb(195,186,178)', linecolor='rgb(203,193,185)', title='Grupo etario')
            #fig_totales_genero.update_yaxes(anchor="free", shift= -10, gridcolor="rgb(228,217,208)", title='Cantidad')
            #fig_totales_genero.update_xaxes(tickmode='array',tickvals=[0.5, 1], ticktext=gender_counts2['Genero'])
            fig3.update_layout(barmode='stack', template='simple_white',            
            title=f'GÉNERO DE DIPUTADOS NACIONALES DE {agrupaciones} EN {distritos}<br><sup>Lista: {lista} - Elecciones PASO 2023</sup>')
            st.plotly_chart(fig3, use_container_width=True)

        totales_candidatos = df2023_v3 
        totales_candidatos['Totales'] = 1
        totales_candidatos['Género'] = totales_candidatos['Género'].replace({'M': 'Masculino', 'F': 'Femenino'})
        totales_gen_edad = totales_candidatos.groupby(['Age_Range', 'Género'])['Totales'].sum().reset_index()
        totales_edad = totales_candidatos.groupby(['Age_Range'])['Totales'].sum().reset_index()
        gender_counts2 = totales_candidatos.groupby(['Género'])['Totales'].sum().reset_index()
        sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='222')
        st.subheader("¿Cuál género encabeza más las listas en cada agrupación?")
        st.write("Si bien según la Ley de Paridad de Género en Ámbitos de Representación Política (Ley 27.412) es obligatorio ubicar de manera intercalada mujeres y varones desde el primer candidato hasta el último candidato suplente, la disparidad de género sigue siendo posible porque las listas pueden estar predominantemente encabezadas por varones de manera legal.")

        enc1, enc2, enc3 = st.columns(3)
        custom_order = ['JUNTOS POR EL CAMBIO','UNION POR LA PATRIA', 'LA LIBERTAD AVANZA', 'HACEMOS POR NUESTRO PAIS']

        encabezan = encabezan_SENADORES_candidatos.sort_values(by=['Agrupación Política'], key=lambda x: x.map({v: i for i, v in enumerate(custom_order)}))
        with enc1:
            ap_encabeza = st.selectbox('Seleccionar agrupación política:', encabezan['Agrupación Política'].unique())
            encabezan_final = encabezan.query('`Agrupación Política`== @ap_encabeza')
            
        # with enc2:
        #     lista_sliced = st.selectbox('Seleccionar lista:', encabezan_sliced['Lista'].unique())
        #     encabezan_final = encabezan_sliced.query('Lista == @lista_sliced')


        encabezan_final['Contador'] = 1
        encabezan_final_plot = encabezan_final.groupby(['Género'])['Contador'].sum().reset_index()

        fig_encabezan = px.bar(encabezan_final_plot, x='Género', y='Contador', color=encabezan_final_plot['Género'], color_discrete_map=colores_genero, text=encabezan_final_plot['Contador'])
        fig_encabezan.update_traces(textposition='outside', textfont_color='black')
        fig_encabezan.update_xaxes(type='category', ticks="outside", ticklen=5, tickcolor='rgb(195,186,178)', linecolor='rgb(203,193,185)', title='Grupo etario')
        fig_encabezan.update_yaxes(anchor="free", shift= -10, gridcolor="rgb(228,217,208)", title='Cantidad')
        fig_encabezan.update_layout(barmode='stack', template='simple_white',            
                title=f"<b>DISTRIBUCIÓN DE GÉNERO PARA LAS LISTAS DE {ap_encabeza} </b><br><sup>Según qué género las encabeza - Elecciones PASO 2023</sup>")
        st.plotly_chart(fig_encabezan, use_container_width=True)
        sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='232')
        st.subheader('¿Quiénes terminan su mandato en 2023?')
        st.write("Los siguientes senadores son quienes finalizan su mandato. A su vez, se puede observar cuantas bancas renueva cada bloque.")
        finalizan_mandato = finalizan_mandato.sort_values(by='BLOQUE')
    #gd.configure_pagination(enabled=True)
    #gd.configure_default_column(
    #resizable=True,
    #filterable=True,
    #sortable=True,
    #editable=False,)


        cellstyle_jscode = JsCode("""
            function(params){
                if (params.value == 'FRENTE NACIONAL Y POPULAR') {
                    return {
                        'color': 'black',
                        'backgroundColor' : '#01b5f0'
                }
                }
                if (params.value == 'FRENTE PRO') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#fcd201'
                    }
                }
                if (params.value == 'MISIONES') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#019c00'
                    }
                }
                if (params.value == 'PRODUCCIÓN Y TRABAJO') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#fa7900'
                    }
                }
                if (params.value == 'UNIDAD CIUDADANA') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#82e8dc'
                    }
                }
                if (params.value == 'UNIÓN CÍVICA RADICAL') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#cd4137'
                    }
                }
                if (params.value == 'UNIDAD FEDERAL') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#043cbe'
                    }
                }                                                                            
                else{
                    return{
                        'color': 'black',
                        'backgroundColor': 'lightpink'
                    }
                }
        
        };
        """)
        gd3 = GridOptionsBuilder.from_dataframe(finalizan_mandato)
        gd3.configure_columns('BLOQUE', cellStyle=cellstyle_jscode)
        gridOptions33 = gd3.build()
        grid_table = AgGrid(finalizan_mandato, 
                gridOptions = gridOptions33, 
                enable_enterprise_modules = True,
                fit_columns_on_grid_load = True,
                height=400,
                width='100%',
                allow_unsafe_jscode=True,
                )
        #st.dataframe(finalizan_mandato, hide_index=True, use_container_width=True)

        colores_BLOQUE_SEN = {
        'FRENTE NACIONAL Y POPULAR': '#01b5f0',
        'FRENTE PRO': '#fcd201',
        'UNIÓN CÍVICA RADICAL': '#cd4137',
        'UNIDAD FEDERAL': '#043cbe',
        'UNIDAD CIUDADANA': '#82e8dc',
        'PRODUCCIÓN Y TRABAJO': '#fa7900',
        'MISIONES': '#019c00',
        'HAY FUTURO ARGENTINA': 'lightpink',
                }

        fig_bloques = px.bar(finalizan_mandato_bloque, x='Cantidad', y='Bloque', color='Bloque', color_discrete_map=colores_BLOQUE_SEN,orientation='h', text='Cantidad',
                                    title=f'Renovación de bancas por bloque')
        fig_bloques.update_traces(textposition='outside', textfont_color='black')
        fig_bloques.update_yaxes(fixedrange=True)
        fig_bloques.update_xaxes(fixedrange=True)
        fig_bloques.update_layout(showlegend=False, template='simple_white')  
        fig_bloques.update_traces(hovertemplate='Bloque: %{y}<br>Bancas a renovar: %{x}<br>', hoverlabel=dict(namelength=0))
        st.plotly_chart(fig_bloques, use_container_width=True, config=config)
        sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='76')
        st.subheader('¿Quiénes componen actualmente el Senado?')
        st.write("Esta es una tabla que contiene a todos los senadores actuales donde podrás filtrar la tabla para ver la distribución por provincia, bloque, etc.")

        # st.dataframe(lista_senadores2, hide_index=True, use_container_width=True)
        # @st.cache_data
        # def convert_df(df_presi2):
        #             return df_presi2.to_csv(index=False).encode('utf-8')
                
        # csv = convert_df(lista_senadores2)

        # st.download_button(
        #         "Descargar tabla como archivo CSV",
        #         csv,
        #         "lista_senadores.csv",
        #         "text/csv",
        #         key='download-csv4'
        #         )       
        
        sb, sb2= st.columns(2)
        lista_senadores2 = lista_senadores2.sort_values(by='PROVINCIA')
        with sb:
            provincia_senador = st.selectbox('Provincia', lista_senadores2['PROVINCIA'].unique())
            df1 = lista_senadores2.query('PROVINCIA == @provincia_senador')
            df1 = df1.sort_values(by='BLOQUE')
        with sb2:
            bloque_senador = st.multiselect('Bloque', df1['BLOQUE'].unique(), default=df1['BLOQUE'].unique())
            lista_senadores_final = df1.query('BLOQUE == @bloque_senador')

        gd34 = GridOptionsBuilder.from_dataframe(finalizan_mandato)
        gd34.configure_columns('BLOQUE', cellStyle=cellstyle_jscode)
        gridOptions34 = gd34.build()
        #st.dataframe(lista_senadores_final, hide_index=True, use_container_width=True)
        grid_table = AgGrid(lista_senadores_final, 
                gridOptions = gridOptions34, 
                enable_enterprise_modules = True,
                fit_columns_on_grid_load = True,
                height=160,
                width='100%',
                allow_unsafe_jscode=True,
                )
        
        sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='8')
        st.subheader('Si querés saber más sobre la Cámara de Senadores...', anchor=False)

        with st.expander('**Funciones**'):
            st.write("El Poder Legislativo es ejercido en la República Argentina por el Congreso Nacional, que está compuesto por dos cámaras: la de Diputados y la de Senadores. **Su tarea primordial es deliberar y sancionar leyes. Además de legislar, otra de las funciones esenciales del Congreso es ejercer el control de gobierno.** Esta actividad se lleva a cabo al evaluar el cumplimiento de los planes o programas previamente elaborados, para lo cual el Congreso tiene las facultades de investigar, requerir informes y realizar tareas de campo. La publicidad de sus actos es otra de sus tareas clave ya que, en tanto fuente de información, permite también a la ciudadanía evaluar el cumplimiento del mandato conferido.")
        with st.expander('**Conformación**'):
            st.write("Los senadores y senadoras cumplen un mandato de seis años y pueden ser reelectos indefinidamente. Sin embargo, no se eligen todos en simultáneo: la Cámara se renueva en un tercio cada dos años, en elecciones nacionales. Cabe recordar que la reforma constitucional de 1994 consagró la elección directa de los senadores y senadoras y la designación de un tercer senador o senadora por la minoría en cada distrito. Para el período 1995-2001, ese tercer senador o senadora fue electo por cada legislatura provincial. La reforma constitucional también acortó la duración del mandato de nueve a seis años y estableció la renovación parcial de la Cámara, un tercio de los distritos cada dos años. <br><br> La reforma constitucional dispuso en una cláusula transitoria que la totalidad de los integrantes del Senado serían elegidos de forma directa en el año 2001. Pero como la reforma también disponía la renovación parcial del Cuerpo por tercios cada dos años, fue necesario disponer la división de los distritos en tres grupos y decidir por la suerte qué senadores y senadoras cumplirían mandatos de dos, cuatro y seis años. Los grupos quedaron conformados de la siguiente manera:<br><br>**Grupo I:** Catamarca, Córdoba, Corrientes, Chubut, La Pampa, Mendoza, Santa Fe y Tucumán.<br><br>**Grupo II:** Buenos Aires, Formosa, Jujuy, La Rioja, Misiones, San Juan, San Luis y Santa Cruz.<br><br>**Grupo III:** Ciudad de Buenos Aires, Chaco, Entre Ríos, Neuquén, Río Negro, Salta, Santiago del Estero y Tierra del Fuego.<br><br>Estos grupos siguen vigentes hasta hoy y determinan qué distritos renuevan sus bancas cada dos años.", unsafe_allow_html=True)
        with st.expander('**Autoridades**'):
            st.write("El presidente natural del Senado de la Nación es el vicepresidente o vicepresidenta de la Nación . En el orden parlamentario preside las sesiones pero no participa de los debates ni vota, salvo en caso de empate. Además, es titular de todas las atribuciones administrativas que hacen al funcionamiento del Cuerpo.<br><br>En lo que respecta al resto de sus autoridades, el Senado designa cada año entre sus miembros a un presidente o presidenta provisional, un vicepresidente o vicepresidenta, un vicepresidente o vicepresidenta primero y un vicepresidente o vicepresidenta segundo . Esta mesa de autoridades es asistida por dos secretarios o secretarias y tres prosecretarios o prosecretarias que no son legisladores y cumplen funciones parlamentarias, administrativas y de coordinación. El mandato de los miembros de la mesa de autoridades dura un período, que vence el último día del mes de febrero del año siguiente a su designación.<br><br>Con respecto al presidente provisional del Senado, cabe señalar que deberá reemplazar a quien preside el Cuerpo en caso de su ausencia o vacancia. Además, de acuerdo con la Ley de Acefalía, será llamado a suceder al presidente o presidenta de la República en tercer término ante el supuesto de renuncia, muerte o incapacidad del presidente o presidenta y de su sucesor natural, el vicepresidente o vicepresidenta de la Nación.",unsafe_allow_html=True)
        with st.expander('**Comisiones**'):
            st.write("Los senadores y senadoras debaten en el marco de comisiones permanentes que abordan diferentes áreas temáticas específicas y están facultadas para dictaminar sobre los proyectos sometidos a decisión. Se trata de instancias de investigación, análisis y discusión que permiten una especialización y un mejor conocimiento de los temas que son objeto de tratamiento legislativo.<br><br>Los senadores y senadoras que integran las comisiones recogen información, escuchan a los diferentes actores involucrados, piden asesoramiento y contemplan la opinión pública y los intereses de la comunidad.<br><br>A partir de la labor de las comisiones, se obtiene información técnica precisa y simplificada, que constituye el soporte elemental para todo el proceso de decisión de los legisladores y legisladoras.",unsafe_allow_html=True)
        with st.expander('**Bloques parlamentarios**'):
            st.write('Los bloques parlamentarios reúnen legisladores y legisladoras por afinidades políticas e intereses comunes.<br><br>El objetivo principal de los bloques es mantener un criterio y delinear estrategias políticas coherentes frente a los diversos problemas e iniciativas que se plantean. La complejidad de la tarea legislativa hace que el trabajo deba dividirse para no dispersar esfuerzos, siendo los bloques los encargados de determinar y coordinar esta tarea.<br><br>Los bloques cuentan con un presidente o presidenta, que es elegido entre sus miembros y suele funcionar como nexo con las autoridades del Cuerpo y con las autoridades nacionales. Los presidentes y presidentas de los bloques, junto con el presidente o presidenta del Senado, forman el Plenario de Labor Parlamentaria, que se ocupa de proyectar el orden del día que se seguirá en las sesiones, informarse acerca del estado de los asuntos en las comisiones y promover medidas prácticas para agilizar los debates y mejorar el funcionamiento del Senado, entre otras funciones.', unsafe_allow_html=True)


###
