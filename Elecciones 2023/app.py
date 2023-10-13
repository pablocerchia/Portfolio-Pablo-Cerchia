
import streamlit as st
from streamlit_option_menu import option_menu
from modulo.bancas import diputados, senadores
from modulo.presidentes import presidentes
from modulo.gobernador import gobernadores
from modulo.resultadostodos import resultados
from modulo.dondevoto import donde_voto
from modulo.faq import faq
from modulo.mesa import mesa
from modulo.electores import electores
from modulo.plataformas import propuestas
from modulo.contact_form import contacto

st.set_page_config(page_title='Elecciones 2023 - Página de consulta', layout='wide')
st.write("#")


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# selected2 = option_menu("Elecciones 2023", ["Resultados", "Resultados en tu mesa", "Propuestas", "Electores", 'Preguntas frecuentes', "¿Dónde voto?"], 
#     icons=['bar-chart','search', 'card-list', "people", 'patch-question', "envelope-paper"], 
#     menu_icon="cast", default_index=0, orientation="horizontal")
# selected2
styles = {
      "container": {"padding": "0!important", "background-color": "#ffffff"},
       "icon": {"color": "black", "font-size": "20px"}, 
       "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
       "nav-link-selected": {"background-color": "lightblue", "font-size": "20px", "font-weight": "normal", "color": "black"},
   }
menu = {
    'title': "Elecciones 2023",
    'items': { 
        'Resultados' : {
            'action': resultados, 'item_icon': 'bar-chart'
        },
        'Propuestas' : {
            'action': propuestas, 'item_icon': 'card-list'
        },
        'Electores' : {
            'action': electores, 'item_icon': 'people'
        },
        'FAQ' : {
            'action': faq, 'item_icon': 'patch-question'
        },
        '¿Dónde voto?' : {
            'action': donde_voto, 'item_icon': 'envelope'
        },
        'Contacto' : {
            'action': contacto, 'item_icon': 'person-circle'
        }
    },
    'menu_icon': 'envelope-paper',
    'default_index': 0,
    'with_view_panel': 'main',
    'orientation': 'horizontal',
    'styles': styles
}

def show_menu(menu):
    def _get_options(menu):
        options = list(menu['items'].keys())
        return options

    def _get_icons(menu):
        icons = [v['item_icon'] for _k, v in menu['items'].items()]
        return icons

    kwargs = {
        'menu_title': menu['title'] ,
        'options': _get_options(menu),
        'icons': _get_icons(menu),
        'menu_icon': menu['menu_icon'],
        'default_index': menu['default_index'],
        'orientation': menu['orientation'],
        'styles': menu['styles']
    }

    with_view_panel = menu['with_view_panel']
    if with_view_panel == 'sidebar':
        with st.sidebar:
            menu_selection = option_menu(**kwargs)
    elif with_view_panel == 'main':
        menu_selection = option_menu(**kwargs)
    else:
        raise ValueError(f"Unknown view panel value: {with_view_panel}. Must be 'sidebar' or 'main'.")

    if menu['items'][menu_selection]['action']:
        menu['items'][menu_selection]['action']()


show_menu(menu)
