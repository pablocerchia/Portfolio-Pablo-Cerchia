import streamlit as st  
import streamlit_antd_components as sac
def contacto ():

    c1, c2, c3 = st.columns([0.2,0.6,0.2])
    with c2:
        #st.header(":mailbox: Si tenés alguna duda o sugerencia para la página escribime!")
        st.markdown("<h3 style='text-align: center;'>Si tenés alguna duda o sugerencia para la página escribime!<br></h3>", unsafe_allow_html=True)

        contact_form = """
        <form action="https://formsubmit.co/pablocerchia@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Tu nombre" required>
            <input type="email" name="email" placeholder="Tu mail" required>
            <textarea name="message" placeholder="Escribí tu mensaje acá"></textarea>
            <button type="submit">Send</button>
        </form>
        """

        st.markdown(contact_form, unsafe_allow_html=True)

        # Use Local CSS File
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


        local_css("style/style.css")


        st.markdown("<h3 style='text-align: center;'>Otras redes:<br></h3>", unsafe_allow_html=True)

        botones = sac.buttons([
                    sac.ButtonsItem(label='github', href='https://github.com/pablocerchia/', icon='github'),
                    sac.ButtonsItem(label='linkedin', href='https://www.linkedin.com/in/pablo-cerchia-0501a7151/', icon='linkedin'),
                    sac.ButtonsItem(label='twitter', href='https://twitter.com/pablocerchia',icon='twitter')
                    ], format_func='title', align='center', shape='round', index=None)
        