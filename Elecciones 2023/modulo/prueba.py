# UPDATED: 2 May 2022

import streamlit as st
# https://discuss.streamlit.io/t/streamlit-option-menu-is-a-simple-streamlit-component-that-allows-users-to-select-a-single-item-from-a-list-of-options-in-a-menu
# https://icons.getbootstrap.com/
from streamlit_option_menu import option_menu
from modulo.bancas import diputados, senadores
from modulo.presidentes import presidentes
from modulo.gobernador import gobernadores

# st.set_page_config(page_title='Muti-page app example', layout='wide')



styles = {
    "container": {"margin": "0px !important", "padding": "0!important", "align-items": "stretch", "background-color": "#fafafa"},
    "icon": {"color": "black", "font-size": "20px"}, 
    "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
    "nav-link-selected": {"background-color": "lightblue", "font-size": "20px", "font-weight": "normal", "color": "black", },
}

menu = {
    'title': 'Todo App',
    'items': { 
        'Diputados' : {
            'action': diputados, 'item_icon': 'house'
        },
        'Senadores' : {
            'action': senadores, 'item_icon': 'gear'
        }
    },
    'menu_icon': 'clipboard2-check-fill',
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