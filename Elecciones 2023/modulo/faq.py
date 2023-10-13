import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
from PIL import Image

# st.set_page_config(page_title = 'Elecciones 2023 - Sitio de consulta',
#                         layout='wide', initial_sidebar_state='collapsed')
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

def faq():

    c4, c5, c6 = st.columns([0.1, 0.8, 0.1])

    votov1 = Image.open('data/votosvalidos.png')
    votov2 = Image.open('data/votosvalidos2.png')
    votonulo = Image.open('data/votosnulos.png')



    with c5:
        #st.markdown("<h1 style='text-align: center;'>Preguntas frecuentes sobre las elecciones<br><br><br></h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'>PREGUNTAS FRECUENTES SOBRE LAS ELECCIONES<br></h3>", unsafe_allow_html=True)

        with st.expander('**¿Qué son las elecciones generales?**'):
            st.write("Son aquellas elecciones donde el electorado define entre las listas de candidatos y candidatas de las agrupaciones políticas quienes serán elegidos y elegidas para ocupar los cargos públicos electivos.")

        with st.expander('**¿Cuántos votos necesita un candidato ganar en primera vuelta?**'):
            st.write("Un candidato a presidente tendrá que cumplir con estas normas para ganar en primera vuelta: <br><br> - Sacar más del 45% de los votos afirmativos válidamente emitidos.<br><br> - Sacar el 40% de los votos afirmativos válidamente emitidos, con una diferencia de 10 puntos porcentuales sobre la fórmula que le sigue.", unsafe_allow_html=True)

        with st.expander('**¿El voto es obligatorio?**'):
            st.write("El voto es obligatorio para todos los electores que tengan entre 18 y 70 años. Para los que tienen entre 16 y 18 y los que son mayores de 70 el voto es optativo.")

        with st.expander('**¿Quiénes pueden votar?**'):
            st.write("Los ciudadanos y las ciudadanas que figuren en el padrón electoral y acrediten su identidad con documento habilitante.")

        with st.expander('**¿Cuáles son los documentos válidos para votar?**'):
            st.write("Libreta de enrolamiento/libreta cívica<br><br> DNI libreta verde<br><br> DNI libreta celeste<br><br> Tarjeta del DNI libreta celeste, que contiene la leyenda “No válido para votar”. <br><br> Nuevo DNI tarjeta<br><br> El ejemplar del documento debe ser igual o posterior al que figura en el padrón. No se permitirá el voto de ciudadanos/as cuyo documento corresponde a un ejemplar anterior al que figura en el padrón electoral ni de aquellos/as que presenten el “DNI en su celular”.", unsafe_allow_html=True)

        with st.expander('**¿Por qué no estoy en el padrón electoral si tengo 16 años?**'):
            st.write("Es posible que no hayas realizado la actualización de mayor del DNI (se debe efectuar a partir de los 14 años); hayas realizado la actualización luego del cierre del padrón provisorio o el Registro Nacional de las Personas no haya remitido a la Cámara Nacional Electoral la información para que seas incluido/a. En este caso, se deberá realizar un reclamo ante la Justicia Nacional Electoral, en los plazos previstos en el Código Electoral Nacional. El mismo podrás realizarlo:<br><br> https://www.padron.gov.ar/cne_reclamos/<br><br> reclamos.padron@pjn.gov.ar<br><br> La Secretaría Electoral correspondiente a tu distrito.", unsafe_allow_html=True)

        with st.expander('**¿Cómo voto?**'):
            st.write("Los ciudadanos y las ciudadanas ubican su mesa en el padrón que se encuentra exhibido en el exterior del establecimiento, y se presentan en ella con su documento habilitante. El electorado exhibirá el documento y lo depositará en la mesa, sin contacto de la autoridad y luego lo retirará. El/la Presidente le entregará un sobre vacío firmado en el acto de su puño y letra y lo invitará a pasar al cuarto oscuro. A solas en el cuarto oscuro el/la ciudadano/a coloca en el sobre la/s boleta/s de sufragio de su preferencia y pasará a depositar el sobre en la urna. A continuación, firmará el padrón y el/la Presidente/a de Mesa firmará la constancia de emisión del voto la que le será entregada al ciudadano/a junto con su documento cívico.")

        with st.expander('**¿Cuándo abre y cierra la jornada electoral?**'):
            st.write("La apertura del acto electoral se realizará a las 8.00 horas y el establecimiento se cerrará a las 18:00 hs. No obstante, podrán votar luego de las 18:00 horas los/as electores/as que aguardaban su turno antes de ese horario.")

        with st.expander('**¿Cómo se clasifican los votos?**'):
            st.image(votov1)
            st.image(votov2)
            st.image(votonulo, caption='Fuente: CIPPEC')

        with st.expander('**¿Qué son los votos de identidad impugnada y recurridos?**'):
            st.write("Los y las integrantes de la mesa pueden impugnar tu identidad antes de que emitas tu voto porque existen dudas sobre ella. En este caso, tendrás que introducir tu voto en un sobre especial.<br><br> Además, al momento de contar los votos, los y las fiscales pueden recurrir la clasificación del voto hecha por el/la presidente/a de mesa.Los motivos de esto se asientan en un formulario especial que se adjunta al voto en un sobre para votos recurridos.<br><br>Los votos recurridos y de identidad  impugnada no serán contados el día de la votación en el escrutinio provisorio sino que se envían a la Justicia Electoral para que decida sobre su validez.", unsafe_allow_html=True)

        with st.expander('**¿Qué pasa si no encuentro la boleta que quiero votar?**'):
            st.write("Le tenés que avisar al presidente o a la presidenta de mesa que faltan boletas, sin especificar cuál. Los/as fiscales repondrán las boletas faltantes. Si después de tal reposición aún siguieran faltando, podés votar en el cuarto oscuro complementario, donde estarán las boletas de todas las agrupaciones.")

        with st.expander('**¿Cómo se integraron/conformaron las listas definitivas de candidatos/as luego de las PASO?**'):
            st.write("Solo podrán competir en esta elección las fuerzas que en las PASO hayan obtenido 1,5% de los votos válidos en el distrito correspondiente.<br><br> Para las agrupaciones que presentaron más de una lista interna en la elección de candidatos/as a diputados/as nacionales, cada agrupación política definió la manera en la que se integró la lista definitiva para la elección general, de acuerdo a la carta orgánica partidaria o acta constitutiva de la alianza.<br><br> En la elección de candidatos/as a senadores/as, en el caso de las agrupaciones que presentaron más de una lista interna, la lista completa que consiguió más votos en las primarias es la que pasó a la general.", unsafe_allow_html=True)

        with st.expander('**¿Qué sucede en los casos de faltantes de boletas?**'):
            st.write("La Autoridad de Mesa debe verificar que existan en todo momento boletas de las agrupaciones políticas. Los/as fiscales las repondrán a pedido del Presidente/a de Mesa o, en su defecto, lo hará él/ella con las boletas de contingencia entregadas por el servicio de correo. En caso de que se agoten las boletas de contingencia, la responsabilidad de reponerlas es de los/as fiscales partidarios.")

        with st.expander('**¿Si no voté en las elecciones primarias, puedo votar en las elecciones generales?**'):
            st.write("Sí, debe votar en las elecciones generales.:gun::knife:")

        with st.expander('**El recorrido de tu voto**'):
            st.write("En el video de CIPPEC se muestra cómo es el proceso desde el momento en que emitís tu voto hasta la proclamación de candidatos/as electos/as.")
            st.video('https://www.youtube.com/watch?v=zKuaJZInwZQ')


        st.write('Fuente: CIPPE y CNE')
