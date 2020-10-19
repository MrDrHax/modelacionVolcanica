import streamlit as st

body = """
Here you will be able to learn about the physics of projectiles in motion.

To start, click on one of the options to the left!

***
The learn page will take you into the main learning page, where interactive graphs will teach you how physics work

The load page will allow you to open saved graphs, and will allow you to test them

The volcano editor will allow you to create your own volcanoes for you to experiment with, and you will be able to export them to excel afterwards for you to experiment!
***
"""

def page():
    st.title('Hello and welcome.')
    st.markdown(body)
