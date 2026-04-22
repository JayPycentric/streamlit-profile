import streamlit as st
from pages.home import display_home
from pages.about import display_about

# display_home()
# display_about()


pg = st.navigation([
    st.Page(display_home, title="home", icon=":material/home:"),
    st.Page(display_about, title="About", icon=":material/person:")
])

pg.run()