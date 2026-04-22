import streamlit as st

def display_contact():

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

    st.title(":material/contact_mail: Get In Touch", anchor=False)
    st.write("I am always open to discussing backend, cloud architecture, or potential collaborations.")
    st.divider()

    col_linkedin, col_cv, col_github,col_email = st.columns(4, border=True)
    with col_linkedin:
        st.subheader("Professional Network")
        st.write("Let's connect on LinkedIn")
        # Link to LinkedIn profile
        st.link_button("View LinkedIn Profile", url="https://www.linkedin.com/in/jadeon-miller-80705420b", type="primary")

    with col_cv:
        st.subheader("My Credentials")
        st.write("Download my Cv Here")
        
        try:
            # CV Download
            with open("resources/Jadeon_Miller_CV.PDF", "rb") as cv_file:
                st.download_button(label="Download CV (PDF)", data=cv_file, file_name="Jadeon_Miller_CV.pdf", mime="application/pdf", type="primary")
        except FileNotFoundError:
            st.error("CV File not found.")
            st.button("CV Unavailable", disabled=True)

    with col_github:
        st.subheader("Code Collab")
        st.write("Let's collaborate on GitHub")
        # Link to my GitHub
        st.link_button("View GitHub Profile", url="https://github.com/JadeonMiller", type="primary")


    with col_email:
        st.subheader("Direct Inquiry")
        st.write("Feel free to contact me via Email")
        # Link to my email
        st.link_button("Send Email", "mailto:jadeon@pycentric.co.za", type="primary")
