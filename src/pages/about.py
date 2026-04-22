import streamlit as st
import time

def display_tech_stack():
    st.title("Tech Stack", text_alignment="center") 
    
    stack1, stack2, stack3, stack4 = st.columns(4, border=True)

    with stack1:
        st.image("resources/images/icons/python.png", caption="Python")

    with stack2:
        st.image("resources/images/icons/Flask.png", caption="Flask")

    with stack3:
        st.image("resources/images/icons/SQLite.png", caption="SQLite")

    with stack4:
        st.image("resources/images/icons/Angular.png", caption="Angular")


def display_tools():
    st.title("Tools", text_alignment="center") 
    
    tool1, tool2, tool3, tool4 = st.columns(4, border=True)

    with tool1:
        st.image("resources/images/icons/Git.png", caption="Git")

    with tool2:
        st.image("resources/images/icons/Docker.png", caption="Docker")

    with tool3:
        st.image("resources/images/icons/Linux.png", caption="Linux")

    with tool4:
        st.image("resources/images/icons/Postman.png", caption="Postman")

def display_cloud():
    st.title("Cloud", text_alignment="center")
    left, center, right = st.columns([1, 1, 1])
    with center:
        with st.container():
            st.markdown("---")
            st.image("resources/images/icons/AWS.png", width=250)
            st.markdown("---")

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
            time.sleep(0.05)

    st.write_stream(text_generator)

    st.divider()
    display_tech_stack()
    display_tools()
    display_cloud()
