# This is the portfolio home page
import streamlit as st

from pages.projects import display_projects
from pages.contact import display_contact

def display_home():
    text, image = st.columns([1, 1], vertical_alignment="center")

    with text:
        st.title("Nice to meet You! I'm Jadeon Miller")
        st.subheader("Graduate Software Developer | Johannesburg")
        st.write("I build scalable web applications and explore cloud infrastructure.")

        btn1, btn2, btn_ = st.columns([3, 3, 3])
        with btn1:
            if st.button("Contact Me", type="primary"):
                st.switch_page(st.Page(display_contact))
        with btn2:
            if st.button("Projects", type="primary"):
                 st.switch_page(st.Page(display_projects))

    with image:
        st.image("resources/images/Gemini_Avatar_Image.png")
