# This is the portfolio home page
import streamlit as st

from pages.projects import display_projects
from pages.contact import display_contact

def display_home():
    st.markdown(
        """
        <style>
            /* This targets the main content area and forces it to fill the screen */
            .block-container {
                max-width: 100% !important;
                padding-left: 5rem !important;
                padding-right: 5rem !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )


    text, image = st.columns([1, 1], vertical_alignment="center")

    with text:
        st.title("Nice to meet You! I'm Jadeon Miller")
        st.subheader("Graduate Software Developer | Johannesburg")
        st.write("I build scalable web applications and explore cloud infrastructure.")

        btn1, btn2, _ = st.columns([0.3, 0.3, 1.2], gap="xxsmall")
        with btn1:
            if st.button("Contact Me", type="primary", use_container_width=True):
                st.switch_page(st.Page(display_contact))
        with btn2:
            if st.button("Projects", type="primary", use_container_width=True):
                 st.switch_page(st.Page(display_projects))

    with image:
        st.image("resources/images/Gemini_Generated_Image_ppinwyppinwyppin.png")
