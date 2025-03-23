#--------------------             
# Author : Serge Zaugg
# Description : Utility functions used by main.py
#--------------------

import os
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit import session_state as ss
import subprocess
import os

st.cache_data
def mp3_to_wav(patin, paout, target_fs = 20000, n_chan = 1):
        """   
        """
        try:
            subprocess.call(['ffmpeg', 
                '-y', # -y overwrite without asking 
                '-i', patin, # '-i' # infile must be specifitd after -i
                '-ar', str(target_fs), # -ar rate set audio sampling rate (in Hz)
                '-ac', str(n_chan), # '1', # stereo to mono, take left channel # -ac channels set number of audio channels
                paout
                ])
        except:
            print("An exception occurred during mp3-to-wav conversion with ffmpeg!")





 
            