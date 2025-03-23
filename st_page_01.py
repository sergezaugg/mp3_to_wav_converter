#--------------------             
# Author : Serge Zaugg
# Description : Streamlit page 
#--------------------

import streamlit as st
from streamlit import session_state as ss
import os
from utils import mp3_to_wav
import streamlit as st
import shutil
import datetime
import pandas as pd

pa_temp_mp3 = 'temp_mp3'
pa_temp_wav = 'temp_wav'
pa_temp_zip = 'temp_zip'

zip_name_temp = 'zipped_wavs_temp'
zip_name_ext = os.path.join(pa_temp_zip, zip_name_temp + '.zip')



@st.fragment
def frag_do_download():
    # download 
    if os.path.exists(zip_name_ext):
        with open(zip_name_ext, "rb") as f:
            timstamp = datetime.datetime.now().strftime('%Y%m%dT%H%M%S')   
            st.download_button(label="Download zipped wavs", data=f, file_name = timstamp + '_ziped_wavs.zip')
    else:
        st.text("No zip available for download!")    

@st.fragment
def frag_see_content():
    col_a1, col_a2,= st.columns(2)
    with col_a1: 
        x_mp3 = os.listdir(pa_temp_mp3)
        n = len(x_mp3)
        df_mp3 = pd.DataFrame(x_mp3, columns =["N = " + str(n) + " mp3 files available for conversion"])
        st.dataframe(df_mp3, use_container_width = True, hide_index = True)
    with col_a2: 
        x_wav = os.listdir(pa_temp_wav)
        n = len(x_wav)
        df_wav = pd.DataFrame(x_wav, columns =["N = " + str(n) + " wav files available for download"])
        st.dataframe(df_wav, use_container_width = True, hide_index = True)


def do_upload():
    with st.form(key = "f01", border=False, clear_on_submit=True):
        uploaded_files = st.file_uploader("Choose MP3 files", accept_multiple_files=True, type = ['mp3'])
        submitted01 = st.form_submit_button("Upload", type="primary")
        if submitted01: 
            for upfi in uploaded_files:
                bytes_data = upfi.read()
                with open(os.path.join(pa_temp_mp3, upfi.name), "wb") as f:
                    f.write(bytes_data)


def convert_wav_and_zip(fs, nch):
    with st.form(key = "f03", border=False): 
        submitted03 = st.form_submit_button("Convert to Wav", type="primary")
        if submitted03: 
            for fi in [a for a in os.listdir(pa_temp_mp3) if '.mp3' in a]:
                pai = os.path.join(pa_temp_mp3, fi)
                pao = os.path.join(pa_temp_wav, fi[0:-4] + "_ch_{:01n}".format(nch) + "_fs_{:01n}".format(fs) + '.wav')
                mp3_to_wav(patin = pai, paout = pao, target_fs = fs, n_chan = nch)
            # ZIP        
            if os.path.exists(zip_name_ext):
                os.remove(zip_name_ext) 
            if len(os.listdir(pa_temp_wav))>0:          
                shutil.make_archive(base_name = os.path.join(pa_temp_zip, zip_name_temp), format = 'zip', root_dir = pa_temp_wav) 




@st.fragment
def flush():
    col_a1, col_a2,= st.columns([0.80, 0.80])
    with col_a1: 
        with st.form(key = "f10", border=False):
            submitted10 = st.form_submit_button("Flush MP3s", type="primary")
            if submitted10: 
                for fi in os.listdir(pa_temp_mp3):
                    os.remove(os.path.join(pa_temp_mp3, fi))
                st.rerun()    
    with col_a2: 
        with st.form(key = "f11", border=False):
            submitted11 = st.form_submit_button("Flush WAVs", type="primary")
            if submitted11:
                if os.path.exists(zip_name_ext):
                    os.remove(zip_name_ext)  
                for fi in os.listdir(pa_temp_wav):
                    os.remove(os.path.join(pa_temp_wav, fi))
                st.rerun()        



ca1, ca2, ca3 = st.columns([0.25, 0.25, 0.50])

with ca1:
    do_upload()

with ca2:
    sampl_freq = st.number_input("Sampling frequency of wav files", min_value=1, max_value=100000, value=24000, step=1) 
    num_ch = selection = st.pills("Nb channels of wave files", [1,2], default = 1)
    a1, a2 = st.columns([0.25, 0.25])
    with a1:
        st.text("Sel: ch={:01n}".format(num_ch) + " fs={:01n}".format(sampl_freq) )  
    with a2:             
        convert_wav_and_zip(fs = sampl_freq, nch = num_ch)

with ca3:
    frag_do_download()

frag_see_content()

flush()
























# # see current contents 
# col_a1, col_a2,= st.columns(2)
# with col_a1: 
#     st.dataframe(os.listdir(pa_temp_mp3), use_container_width = True)
# with col_a2: 
#     st.dataframe(os.listdir(pa_temp_wav), use_container_width = True)


# # download 
# if os.path.exists(zip_name_ext):
#     with open(zip_name_ext, "rb") as f:
#         timstamp = datetime.datetime.now().strftime('%Y%m%dT%H%M%S')   
#         st.download_button(label="Download zipped wavs", data=f, file_name = timstamp + '_ziped_wavs.zip')
# else:
#     st.text("No zip available for download!")    
  
# freg_do_download()






    