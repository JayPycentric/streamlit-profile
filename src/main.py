import streamlit as st
from pages.home import display_home
from pages.about import display_about
from pages.projects import display_projects

pg = st.navigation([
    st.Page(display_home, title="home", icon=":material/home:"),
    st.Page(display_about, title="About", icon=":material/person:"),
    st.Page(display_projects, title="Projects", icon=":material/terminal:")
])

pg.run()