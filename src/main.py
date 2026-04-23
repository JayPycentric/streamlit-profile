import streamlit as st
from pages.home import display_home
from pages.about import display_about
from pages.projects import display_projects
from pages.contact import display_contact

st.set_page_config(
    page_title="Jadeon Miller | Portfolio",
    page_icon=":material/person:",
    layout="centered",             
    initial_sidebar_state="expanded" 
)

pg = st.navigation([
    st.Page(display_home, title="home", icon=":material/home:"),
    st.Page(display_about, title="About", icon=":material/person:"),
    st.Page(display_projects, title="Projects", icon=":material/terminal:"),
    st.Page(display_contact, title="Contact", icon=":material/contact_mail:")
])

pg.run()