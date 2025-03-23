#--------------------             
# Author : Serge Zaugg
# Description : Streamlit page 
#--------------------

import streamlit as st

st.subheader("Batch convert mp3 to wav")

st.markdown(''' 
        Allows to convert many mp3 to wav while controlling the sampling frequency and number of channels. 
            
        Uses [ffmpeg](https://ffmpeg.org) in the back. 
            
        Only converts to wavs with a bit-depth of 16.
            
        Conversion to wav will not correct mp3 artifacts.
            
        Was develop for bio-acoustic projects to convert many mp3 downloaded from [xeno-canto](https://xeno-canto.org).
            
        Wav files with fixed sampling frequency are easier to handle in ML projects with Python/Pytorch.
            
        ''')





    