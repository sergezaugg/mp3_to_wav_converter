#--------------------             
# Author : Serge Zaugg
# Description : Main streamlit entry point
# Run locally : streamlit run stmain.py
#--------------------

import streamlit as st

st.set_page_config(layout="wide")

pages = [
    st.Page("st_page_01.py", title="Interactive"),
    ]

pg = st.navigation(pages)

pg.run()

with st.sidebar:
    st.text("-- Under development --")
    st.title(""); st.title(""); st.title(""); st.title(""); st.title(""); st.title(""); st.title("")
  