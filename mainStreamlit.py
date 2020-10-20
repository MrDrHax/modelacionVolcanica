import streamlit as st
import pages.veditor as volcanoEditor
import pages.landingPage as landingPage
import pages.learn as learn
import pages.graph as graph
import pages.references as ref

PAGES = {
    "Main": landingPage,
    "Learn": learn,
    "Load graph": graph,
    "Crazy volcano editor": volcanoEditor,
    "References": ref
}

st.sidebar.title('Go to:')

selection = st.sidebar.radio("", list(PAGES.keys()))

page = PAGES[selection]
page.page()

st.text('This work by Alejandro Fernandez del Valle Herrera is licensed under CC BY 4.0 CC')