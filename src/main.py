# import streamlit as st
# import itertools as iter
# from time import sleep

# # st.title("Welcome to Jadeon", text_alignment="center")

# # st.write("""
# # Hello World
# # This is my first streamlit text 
# # """)

# # st.button(label="Happy Happy", icon="🎃")
# # st.image("/home/jadeon/Pictures/Wallpapers/wallhaven-gw9j7q_3840x2160.png", caption="This is my wallpaper")

# # user_input = st.text_input("Like the image Yes/No", placeholder="No")
# # if user_input:
# #     st.write(f"Thanks for the feedback! Your input was: {user_input.upper()}")

# # # languages = ["java", "python", "docker"]
# # # lan_loop = st.empty()
# # # while True:
# # #     for lan in iter.cycle(languages):
# # #         sleep(5)
# # #         lan_loop.write(f"I have used: {lan.upper()}")


# import streamlit as st

# # This creates a top-level tab bar
# tab_home, tab_about, tab_skills, tab_projects, tab_contact = st.tabs([
#     "Home", "About Me", "Skills", "Projects", "Contact"
# ])

# # 1. Define your sections as functions
# def show_home():
#     st.title("Welcome to my Portfolio 👋")
#     st.subheader("Graduate Software Developer based in Johannesburg")
#     st.write("I build scalable web applications and explore cloud infrastructure.")

# def show_about():
#     st.header("About Me")
#     st.write("I am a Computer Science graduate with a passion for clean code and problem solving...")

# def show_skills():
#     st.header("Frameworks & Languages")
#     # ... your columns logic here

# def show_projects():
#     st.header("Featured Projects")
#     # ... your projects and download button logic here

# def show_contact():
#     st.header("Get In Touch")
#     # ... your form logic here

# # 2. Setup the Navigation
# # We map the labels/icons to the functions
# # pg = st.navigation([
# #     st.Page(show_home, title="Home", icon=":material/home:"),
# #     st.Page(show_about, title="About", icon=":material/person:"),
# #     st.Page(show_skills, title="Skills", icon=":material/code:"),
# #     st.Page(show_projects, title="Projects", icon=":material/work:"),
# #     st.Page(show_contact, title="Contact", icon=":material/mail:"),
# # ])


# with tab_home:
#     show_home()

# with tab_about:
#     show_about()


# # 3. Run the navigation
# st.set_page_config(page_title="Jadeon Miller | Portfolio", layout="wide")
# # pg.run()