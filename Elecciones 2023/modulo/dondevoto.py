import streamlit as st 

# st.set_page_config(page_title = 'Elecciones 2023 - Sitio de consulta',
#                     layout='wide', initial_sidebar_state='collapsed')
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


def donde_voto():
    c4, c5, c6 = st.columns([0.2, 0.6, 0.2])

    with c5:

        iframe_url = "https://www.padron.gob.ar/"
        st.components.v1.iframe(iframe_url, width=1000, height=1200)
