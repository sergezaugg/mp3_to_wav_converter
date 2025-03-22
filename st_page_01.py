#--------------------             
# Author : Serge Zaugg
# Description : Streamlit page 
#--------------------

import streamlit as st
from streamlit import session_state as ss
import subprocess
import os
from utils import mp3_to_wav

pa_in = 'temp_data/Corvus_corax_XC334273_160408_125949_Corvus_corax_tingitanus_R.mp3'

pa_out = 'temp_out'

finam = st.text_input("give file name", "aaa.wav")
pa_out_full = os.path.join(pa_out, finam)

mp3_to_wav(patin = pa_in, paout = pa_out_full, target_fs = 20000)

# if st.button('Download wav'):
  
with open(pa_out_full, "rb") as f:
    st.download_button(
        label="Download report",
        data=f,
        file_name="downloaded_aa.wav")



     