# This is the portfolio home page
import streamlit as st


def display_home():
    col1, col2 = st.columns([1, 1], vertical_alignment="center")

    with col1:
        st.title("Nice to meet You! I'm Jadeon Miller")
        st.subheader("Graduate Software Developer | Johannesburg")
        st.write("I build scalable web applications and explore cloud infrastructure.")
        if st.button("Contact Me"):
            st.info("Add contact field link LATER.")

    with col2:
        st.image("resources/images/Gemini_Avatar_Image.png")
