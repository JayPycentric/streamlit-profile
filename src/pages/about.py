import streamlit as st
import time

def display_about():
    st.title("About Me", text_alignment="center")

    about_text = """
    I’m **Jadeon Miller**, a Software Engineering graduate from WeThinkCode_ with a passion for building 
    scalable backend systems and cloud‑native solutions. My journey has taken me from mentoring on campus 
    to hands‑on roles in backend development, DevOps, and cloud infrastructure.

    I thrive on designing modular architectures, troubleshooting Linux environments, and delivering 
    reliable software that makes an impact. Beyond code, I enjoy mentoring peers, optimizing workflows, and 
    tinkering with computers.
    """

    def text_generator():
        for word in about_text.split(" "):
            yield word + " "
            time.sleep(0.15)

    st.write_stream(text_generator)


def display_tech():
    # TODO
    pass