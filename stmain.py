#--------------------             
# Author : Serge Zaugg
# Description : Main streamlit entry point
# Run locally : streamlit run stmain.py
#--------------------

import streamlit as st

st.set_page_config(layout="wide")

pages = [
    st.Page("st_page_01.py", title="Converter"),
    st.Page("st_page_02.py", title="Info"),
    ]

pg = st.navigation(pages)

pg.run()

with st.sidebar:
    st.subheader("BATCH CONVERT MP3 TO WAV")
    st.text("-- Under development --")
    st.markdown("""
            Convert multiple mp3 to wav while controlling the sampling frequency and number of channels.
            Primarily for further processing with Python/Pytorch. Uses [ffmpeg](https://ffmpeg.org) in the back. 
            """)
   
  