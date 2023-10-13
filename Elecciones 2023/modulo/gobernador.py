import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import streamlit.components.v1 as components
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode, ColumnsAutoSizeMode
import streamlit_antd_components as sac


def gobernadores():
    c116, c117, c118 = st.columns([0.1,0.8,0.1])
    with c117:
        st.markdown("<h3 style='text-align: center;'>Qué vas a poder encontrar en esta sección<br></h3>", unsafe_allow_html=True)
        st.markdown(
                    """
                    <div style="text-align:center; font-size: 1.5em;">• Consultá y compará cómo le fue a las agrupaciones y a los candidatos para gobernador en cada sección electoral de la provincia de Buenos Aires. <br>
                    • Además, podés comparar en detalle sus resultados en cada sección y circuito electoral del <a href='#el-conurbano-la-clave-del-xito-de-kicillof'>Conurbano Bonaerense</a>.<br>
                    • También vas a poder consultar cómo les fue en cada <a href='#consult-los-resultados-en-cada-secci-n-electoral-provincial'>sección provincial</a>.</div>
                    """,
                    unsafe_allow_html=True
                    )
        sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='1667')

        tabs = sac.buttons(['Por agrupación','Por candidato'], label=None, index=0, format_func=None, align='center', position='top', size='large', direction='horizontal', shape='round', compact=False, return_index=False)
    #st.markdown("""<style>.css-zt5igj svg{display:none}</style>""", unsafe_allow_html=True)

    if tabs == 'Por agrupación':

            c1, c2, c3 = st.columns([0.1,0.8,0.1])
            with c2:

                cmap, charts =st.columns([0.60,0.4])
                with cmap:
                        
                        components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15110175" data-height="850px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=860)
                with charts:
                        components.html("""<div style="min-height:447px"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/Zxg9C/embed.js?v=3" charset="utf-8"></script><noscript><img src="https://datawrapper.dwcdn.net/Zxg9C/full.png" alt="" /></noscript></div>""",height=460)
                        components.html("""<div style="min-height:364px"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/cvJp6/embed.js?v=3" charset="utf-8"></script><noscript><img src="https://datawrapper.dwcdn.net/cvJp6/full.png" alt="" /></noscript></div>""",height=400)
                sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='1')
                # st.subheader('Compará cómo les fue en cada sección electoral', anchor=False)
                st.markdown("<h3 style='text-align: center;'>RESULTADOS POR SECCIÓN ELECTORAL<br></h3>", unsafe_allow_html=True)
                st.markdown("<h5 style='text-align: center; font-weight: normal;'>Mirá dónde se hicieron fuertes y dónde tienen terreno por ganar las principales agrupaciones.<br></h5>", unsafe_allow_html=True)
                #st.write("Mirá dónde se hicieron fuertes y dónde tienen terreno por ganar las principales agrupaciones.")
                mapa111, mapa222, mapa333 = st.columns([0.33, 0.34, 0.33])
                with mapa111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15113723" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                with mapa222: 
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15113682" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=650)
                with mapa333:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15113705" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=650)
                sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='412') 
                st.markdown("<h3 style='text-align: center;'>EL CONURBANO: LA CLAVE DEL ÉXITO DE KICILLOF.<br></h3>", unsafe_allow_html=True)
                #st.subheader('EL CONURBANO: La clave del éxito de Kicillof. Compará cómo les fue a las agrupaciones en el conurbano a nivel circuito electoral', anchor=False)
                st.markdown("<h5 style='text-align: center; font-weight: normal;'>En el Conurbano viven 10 millones de personas, es decir, el 64% de la población de la provincia de Buenos Aires. En el gráfico de arriba se ve como la provincia está casi en su totalidad pintada de amarilla. A primera vista eso parece indicar una victoria demoledora de Juntos por el Cambio. <br><br> Sin embargo, los mejores resultados de Unión por la Patria se dieron allí donde la densidad poblacional es mayor. El resultado victorioso en las PASO 2023 del peronismo se explica a partir de su sólido rendimiento en ciertos municipios del Conurbano Bonaerense.<br></h5>", unsafe_allow_html=True)
                #st.write("En el Conurbano viven 10 millones de personas, es decir, el 64% de la población de la provincia de Buenos Aires. En el gráfico de arriba se ve como la provincia está casi en su totalidad pintada de amarilla. A primera vista eso parece indicar una victoria demoledora de Juntos por el Cambio. Sin embargo, los mejores resultados de UxP se dieron allí donde la densidad poblacional es mayor. El resultado victorioso en las PASO 2023 de Unión por la Patria se explica a partir de su sólido rendimiento en ciertos municipios del Conurbano Bonaerense.")
                mapa777, mapa77789, mapa636, mapa555999 = st.columns([0.1, 0.4, 0.4, 0.1])
                
                with mapa77789:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15113850" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=650)       
                with mapa636:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15113948" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=650)
                #st.subheader("Rendimiento individual de cada agrupación en el Conurbano:")
                mapa1116, mapa2226, mapa3336 = st.columns([0.33, 0.34, 0.33])
                
                with mapa1116:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15121346" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                with mapa2226: 
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15121377" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=650)
                with mapa3336:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15121343" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=650)
                sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='4126')
            st.markdown("<h3 style='text-align: center;'>CONSULTÁ LOS RESULTADOS EN CADA SECCIÓN ELECTORAL PROVINCIAL<br></h3>", unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: center; font-weight: normal;'>Las secciones electorales de la provincia de Buenos Aires son 8 divisiones territoriales que el gobierno provincial hace para la elección de sus legisladores provinciales.<br><br></h5>", unsafe_allow_html=True)
            #st.subheader("Consultá los resultados de cada sección provincialLas secciones electorales de la provincia de Buenos Aires (Argentina) son 8 divisiones territoriales que el gobierno provincial hace para la elección de sus legisladores provinciales (92 diputados y 46 senadores).")
            tabs2 = sac.buttons(['1º SECCIÓN','2º SECCIÓN', "3º SECCIÓN", "4º SECCIÓN","5º SECCIÓN","6º SECCIÓN","7º SECCIÓN","CAPITAL",], label=None, index=0, format_func=None, align='center', position='top', size='large', direction='horizontal', shape='round', compact=False, return_index=False, key=6553)
            
            
            c11, c22, c33 = st.columns([0.1,0.8,0.1])
            with c22:

                    if tabs2 == '1º SECCIÓN':
                        cmap1, charts2 =st.columns([0.60,0.4])
                        with cmap1:
                            
                            components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15118091" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=850)
                        with charts2:
                            components.html("""<div style="min-height:447px"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/vsKJj/embed.js?v=3" charset="utf-8"></script><noscript><img src="https://datawrapper.dwcdn.net/vsKJj/full.png" alt="" /></noscript></div>""",height=480)
                            components.html("""<div style="min-height:364px"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/VKaJ8/embed.js?v=2" charset="utf-8"></script><noscript><img src="https://datawrapper.dwcdn.net/VKaJ8/full.png" alt="" /></noscript></div>""",height=380) 
                    if tabs2 == '2º SECCIÓN':
                        cmap1, charts2 =st.columns([0.60,0.4])
                        with cmap1:
                            
                            components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15118122" data-height="850px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=850)
                        with charts2:
                            components.html("""<div style="min-height:447px"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/yll1f/embed.js?v=4" charset="utf-8"></script><noscript><img src="https://datawrapper.dwcdn.net/yll1f/full.png" alt="" /></noscript></div>""",height=480)
                            components.html("""<div style="min-height:364px"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/Jc7Ax/embed.js?v=2" charset="utf-8"></script><noscript><img src="https://datawrapper.dwcdn.net/Jc7Ax/full.png" alt="" /></noscript></div>""",height=380)
                    if tabs2 == '3º SECCIÓN':
                        cmap1, charts2 =st.columns([0.60,0.4])
                        with cmap1:
                            
                            components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15118173" data-height="850px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=850)
                        with charts2:
                            components.html("""<div style="min-height:428px"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/6btsH/embed.js?v=3" charset="utf-8"></script><noscript><img src="https://datawrapper.dwcdn.net/6btsH/full.png" alt="" /></noscript></div>""",height=480)
                            components.html("""<div style="min-height:364px"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/gh6IS/embed.js?v=2" charset="utf-8"></script><noscript><img src="https://datawrapper.dwcdn.net/gh6IS/full.png" alt="" /></noscript></div>""",height=380) 
                    if tabs2 == '4º SECCIÓN':
                        cmap1, charts2 =st.columns([0.60,0.4])
                        with cmap1:
                            
                            components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15118232" data-height="850px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=850)
                        with charts2:
                            components.html("""<div style="min-height:428px"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/Uj16X/embed.js?v=2" charset="utf-8"></script><noscript><img src="https://datawrapper.dwcdn.net/Uj16X/full.png" alt="" /></noscript></div>""",height=480)
                            components.html("""<div style="min-height:364px"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/GG5ky/embed.js?v=2" charset="utf-8"></script><noscript><img src="https://datawrapper.dwcdn.net/GG5ky/full.png" alt="" /></noscript></div>""",height=380)
                    if tabs2 == '5º SECCIÓN':
                        cmap1, charts2 =st.columns([0.60,0.4])
                        with cmap1:
                            
                            components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15118293" data-height="850px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=850)
                        with charts2:
                            components.html("""<div style="min-height:428px"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/znop1/embed.js?v=2" charset="utf-8"></script><noscript><img src="https://datawrapper.dwcdn.net/znop1/full.png" alt="" /></noscript></div>""",height=480)
                            components.html("""<div style="min-height:364px"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/0hnOs/embed.js?v=2" charset="utf-8"></script><noscript><img src="https://datawrapper.dwcdn.net/0hnOs/full.png" alt="" /></noscript></div>""",height=380)                                                           
                    if tabs2 == '6º SECCIÓN':
                        cmap1, charts2 =st.columns([0.60,0.4])
                        with cmap1:
                            
                            components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15118368" data-height="850px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=850)
                        with charts2:
                            components.html("""<div style="min-height:428px"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/q5bYC/embed.js?v=2" charset="utf-8"></script><noscript><img src="https://datawrapper.dwcdn.net/q5bYC/full.png" alt="" /></noscript></div>""",height=480)
                            components.html("""<div style="min-height:364px"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/Pvmfd/embed.js?v=2" charset="utf-8"></script><noscript><img src="https://datawrapper.dwcdn.net/Pvmfd/full.png" alt="" /></noscript></div>""",height=380) 
                    if tabs2 == '7º SECCIÓN':
                        cmap1, charts2 =st.columns([0.60,0.4])
                        with cmap1:
                            
                            components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15118395" data-height="850px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=850)
                        with charts2:
                            components.html("""<div style="min-height:428px"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/docmz/embed.js?v=2" charset="utf-8"></script><noscript><img src="https://datawrapper.dwcdn.net/docmz/full.png" alt="" /></noscript></div>""",height=480)
                            components.html("""<div style="min-height:364px"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/Yff75/embed.js?v=2" charset="utf-8"></script><noscript><img src="https://datawrapper.dwcdn.net/Yff75/full.png" alt="" /></noscript></div>""",height=380) 
                    if tabs2 == 'CAPITAL':
                        cmap1, charts2 =st.columns([0.60,0.4])
                        with cmap1:
                            
                            components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15118425" data-height="850px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=850)
                        with charts2:
                            components.html("""<div style="min-height:428px"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/xDOxR/embed.js?v=2" charset="utf-8"></script><noscript><img src="https://datawrapper.dwcdn.net/xDOxR/full.png" alt="" /></noscript></div>""",height=480)
                            components.html("""<div style="min-height:364px"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/tqust/embed.js?v=2" charset="utf-8"></script><noscript><img src="https://datawrapper.dwcdn.net/tqust/full.png" alt="" /></noscript></div>""",height=380)   

    if tabs == 'Por candidato':

            c11, c22, c33 = st.columns([0.1,0.8,0.1])
            with c22:

                cmap, charts =st.columns([0.60,0.4])
                with cmap:
                        
                        components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15342207" data-height="850px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=860)
                with charts:
                        components.html("""<div style="min-height:445px"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/3dfKj/embed.js?v=1" charset="utf-8"></script><noscript><img src="https://datawrapper.dwcdn.net/3dfKj/full.png" alt="" /></noscript></div>""",height=460)
                        components.html("""<div style="min-height:364px"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/cvJp6/embed.js?v=3" charset="utf-8"></script><noscript><img src="https://datawrapper.dwcdn.net/cvJp6/full.png" alt="" /></noscript></div>""",height=400)
                sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='1')
                # st.subheader('Compará cómo les fue en cada sección electoral', anchor=False)
                st.markdown("<h3 style='text-align: center;'>RESULTADOS POR SECCIÓN ELECTORAL<br></h3>", unsafe_allow_html=True)
                st.markdown("<h5 style='text-align: center; font-weight: normal;'>Mirá dónde se hicieron fuertes y dónde tienen terreno por ganar los principales candidatos.<br></h5>", unsafe_allow_html=True)
                #st.write("Mirá dónde se hicieron fuertes y dónde tienen terreno por ganar las principales agrupaciones.")
                mapa111, mapa222, mapa333 = st.columns([0.33, 0.34, 0.33])
                with mapa111:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15342947" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=650)
                with mapa222: 
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15342953" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=650)
                with mapa333:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15342917" data-height="650px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=650)
            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='1412') 
            st.markdown("<h3 style='text-align: center;'>LA INTERNA DE JUNTOS POR EL CAMBIO<br></h3>", unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: center; font-weight: normal;'>• Mirá cómo se dirimió la interna entre Grindetti y Santilli que determinó quién va a ser el principal competidor contra Kicillof en octubre. <br>• Si bien a primera vista parece que Santilli arrasó en el Conurbano (allí donde se concentra el 64% de la población de Buenos Aires), si se analiza en detalle puede verse que a pesar de ganar en menos municipios Grindetti tuvo excelente performance en municipios como San Miguel (yendo en la boleta del intendente actual Jaime Mendez que ganó con el 67% de los votos), Lanús (donde es intendente) y Avellaneda. <br>• Esos tres municipios fueron clave para que en el Conurbano solo pierda por el 0.07% (4.251 votos). Luego, en el resto de la provincia de Buenos Aires se puede observar que Grindetti gana en la mayoría de los municipios.<br><br></h5>", unsafe_allow_html=True)
            c1144, c2244, c3344, c4400 = st.columns([0.1,0.4,0.4,0.1])
            with c2244:
                        
                components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15342718" data-height="700px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=730)

            with c3344:
                 components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15343106" data-height="700px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=730)