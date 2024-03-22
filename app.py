import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="JFernandezapp", page_icon="🤖", layout="wide")
email_contact = "emaildecontaco@hotmail.com"

def css_load(css_file):
    with open(css_file) as file:
        st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)

css_load("style/main.css")

url = "https://lottie.host/83f246c0-50f4-4074-a351-fe7343001e3e/vDfqjlZx4S.json"

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie = load_lottie(url)

#Intro
with st.container():
    st.header("Hola somo JFernandez App 👋")
    st.title("Creamos soluciones para acelerar tu negocio")
    st.write("Somos unos apasionados de la tecnologia y la inovación, especializados en el sector de la digitalización y automatización de negocios")
    st.write("[Saber mas >](https://www.linkedin.com/in/julio-cesar-fernandez-estela-45357267/)")

#Sobre Nosotros
with st.container():
    st.write("---") 
    text_colum, animation_colum = st.columns(2)
    with text_colum:
        st.header("Sobre Nosotros 🔍")
        st.write(
            """
            
            Como Ingeniero de Petróleo con 10 años de experiencia en la industria, he tenido el privilegio de explorar y contribuir a uno de los sectores más dinámicos y desafiantes del mundo. Mi carrera me ha llevado a través de diversas facetas de la industria petrolera, desde la exploración y producción hasta el refinamiento y distribución de petróleo.

            Mi pasión por la ingeniería y el compromiso con la innovación me han permitido desarrollar soluciones eficientes y sostenibles que no solo optimizan la extracción y utilización de recursos petrolíferos, sino que también abordan los desafíos ambientales asociados con la industria. Estoy profundamente comprometido con la búsqueda de un equilibrio entre el aprovechamiento de los recursos naturales y la preservación de nuestro planeta para las generaciones futuras.

            En mi viaje profesional, he tenido la fortuna de trabajar con equipos multidisciplinarios, aprendiendo y aportando a un ambiente colaborativo que valora la innovación, la integridad y la excelencia. Estas experiencias han enriquecido mi visión profesional y personal, impulsándome a seguir avanzando y buscando nuevas oportunidades para contribuir a la industria petrolera con una perspectiva fresca y sostenible.

            A través de esta página, espero compartir mis conocimientos, experiencias y pasión por la ingeniería de petróleo, así como explorar nuevas colaboraciones y oportunidades que nos lleven hacia un futuro energético más brillante y sostenible.

            ***Si suena interesante para ti puedes contactarnos***
            
            """
        )
        st.write("[Saber mas >](https://www.linkedin.com/in/julio-cesar-fernandez-estela-45357267/)")

    with animation_colum:
        st_lottie(lottie, height = 400)
    
# Servicios
    
with st.container():
    st.write("---")
    st.header("Servicios 🛠")
    st.write("##")
    image_column, text_colum = st.columns((1,2))
    with image_column:
        st.image("imagens/app1.jpg", use_column_width=True)
    with text_colum:
        st.subheader("Diseño de aplicaciones")
        st.write(
            """
            Como ingeniero de petróleo con amplia experiencia, me dedico a innovar en la industria, buscando un equilibrio entre la eficiencia energética y la sostenibilidad ambiental. Mi carrera me ha permitido colaborar en equipos multidisciplinarios, fomentando soluciones que avanzan hacia un futuro energético más sostenible. A través de este espacio, comparto mi pasión por la ingeniería de petróleo y mi compromiso con el desarrollo energético responsable.
            """
        )

        st.write("[Ver Servicios >](https://www.linkedin.com/in/julio-cesar-fernandez-estela-45357267/)")


#Contacto
with st.container():
    st.write("---")
    st.header("Contacta con nosotros 📩")
    st.write("##")
    contac_form = f"""
    <form action="https://formsubmit.co/{email_contact}" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Tu nombre" requiered>
    <input type="email" name="email" placeholder="Tu email" requiered>
    <textarea type="message" name="message" placeholder="Tu mensaje aqui" requiered></textarea>
    <button type="submit">Send</button>
    </form>
    """
    left_column, right_column =st.columns(2)
    with left_column:
        st.markdown(contac_form, unsafe_allow_html=True)
    with right_column:
        st.empty()  