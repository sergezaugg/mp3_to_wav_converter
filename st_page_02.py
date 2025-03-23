#--------------------             
# Author : Serge Zaugg
# Description : Streamlit page 
#--------------------

import streamlit as st

st.subheader("Batch convert mp3 to wav")
st.text("-- Under development --")
st.text("""
        Allows to convert several mp3 to wav while controlling the sampling frequency and number of channels. 
        Primarily for further processing with Python/Pytorch.
        Uses ffmpeg in the back. 

        onyl converts to 16-bit wavs


        use case: convert hundreds of mp3 from xc (varvariable n-ch and fs) to a neat collection of wavs all with same fs and n-ch 



        wav will not correct mp3 artefacts !

        add link to ffmpeg

        add link to xc

        """)





    