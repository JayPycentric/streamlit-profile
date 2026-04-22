import streamlit as st

def display_projects():
    st.title("My Projects")
    st.write("A showcase of my work")
    
    with st.container(border=True):
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image("resources/images/Gemini_Generated_Image_xawk3dxawk3dxawk.png")
            
        with col2:
            st.subheader("Rugby Union Tracker(RUT)")
            st.write("""
                A Rugby Union Tracker.  
                - Python 
                - Flask
                - Angular
                - sqlite3  
                Made to assist players and coaches  
                track team stats throughout the season  
                at a club rugby level
                
            """)
            
            btn1, btn2 = st.columns(2)
            with btn1:
                st.link_button("View Code (GitHub)", "https://github.com/JadeonMiller/Rugby-Union-Tracker")
            with btn2:
                st.button("Demo Coming Soon", disabled=True, key="demo1")

    st.divider()

    with st.container(border=True):
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image("resources/images/Gemini_Generated_Image_bp8gnubp8gnubp8g.png", use_container_width=True)
            
        with col2:
            st.subheader("Signly")
            st.write("""
                PDF Signer
                - Angular
                - PrimeNG
                - HTML
                - CSS  
                Made to sign PDF Dcouments on the go.
            """)
            
            btn1, btn2 = st.columns(2)
            with btn1:
                st.link_button("View Code (GitHub)", "https://github.com/JadeonMiller/Signly-Angular")
            with btn2:
                st.button("Demo Coming Soon", disabled=True, key="demo2")
