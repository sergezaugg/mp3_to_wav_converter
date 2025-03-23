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
    st.subheader("Batch convert mp3 to wav")
    st.text("-- Under development --")
    st.text("Objective: convert mp3 to wav for further processing in Python/Pytorch")
    st.text("Primarily meant fo XC MP3 data")
    st.text("Uses ffmpeg")

  