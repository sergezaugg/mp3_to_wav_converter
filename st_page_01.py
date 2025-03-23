#--------------------             
# Author : Serge Zaugg
# Description : Streamlit page 
#--------------------

import streamlit as st
from streamlit import session_state as ss
import os
from utils import mp3_to_wav
import shutil
import datetime
import pandas as pd

# define the temp paths and file names
pa_temp_mp3 = 'temp_mp3'
pa_temp_wav = 'temp_wav'
pa_temp_zip = 'temp_zip'
zip_name_temp = 'zipped_wavs_temp'
zip_name_ext = os.path.join(pa_temp_zip, zip_name_temp + '.zip')

# initialize session state 
if 'ffmpeg' not in ss:
    ss['ffmpeg'] = {}
    ss['ffmpeg']['fs'] = 24000
    ss['ffmpeg']['nch'] = 1



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


def do_upload(he1, he2):
    with st.form(key = "f01", border=False, clear_on_submit=True):
        with st.container(height=he1, border=True):
            uploaded_files = st.file_uploader("Choose MP3 files", accept_multiple_files=True, type = ['mp3'])
        with st.container(height=he2, border=True):
            submitted01 = st.form_submit_button("Upload", type="secondary")
            if submitted01: 
                for upfi in uploaded_files:
                    bytes_data = upfi.read()
                    with open(os.path.join(pa_temp_mp3, upfi.name), "wb") as f:
                        f.write(bytes_data)

@st.fragment
def prepare_params_for_ffmpeg():
    ss['ffmpeg']['fs']  = st.number_input("Sampling frequency of wav", min_value=1, max_value=200000, value=24000, step=1) 
    a1, a2 = st.columns([0.25, 0.25])
    with a1:
        ss['ffmpeg']['nch'] = st.radio("N channels of wav", options = [1,2], horizontal=True)  
    with a2:   
        st.text("Sel: ch={:01n}".format(ss['ffmpeg']['nch']) + " fs={:01n}".format(ss['ffmpeg']['fs']) ) 


def convert_wav_and_zip():
    with st.form(key = "f03", border=False): 
        submitted03 = st.form_submit_button("Convert to wav", type="secondary")
        if submitted03: 
            for fi in [a for a in os.listdir(pa_temp_mp3) if '.mp3' in a]:
                pai = os.path.join(pa_temp_mp3, fi)
                pao = os.path.join(pa_temp_wav, fi[0:-4] + "_ch_{:01n}".format(ss['ffmpeg']['nch']) + "_fs_{:01n}".format(ss['ffmpeg']['fs']) + '.wav')
                mp3_to_wav(patin = pai, paout = pao, target_fs = ss['ffmpeg']['fs'], n_chan = ss['ffmpeg']['nch'])
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
            submitted10 = st.form_submit_button("Flush MP3s", type="secondary")
            if submitted10: 
                for fi in os.listdir(pa_temp_mp3):
                    os.remove(os.path.join(pa_temp_mp3, fi))
                st.rerun()    
    with col_a2: 
        with st.form(key = "f11", border=False):
            submitted11 = st.form_submit_button("Flush WAVs", type="secondary")
            if submitted11:
                if os.path.exists(zip_name_ext):
                    os.remove(zip_name_ext)  
                for fi in os.listdir(pa_temp_wav):
                    os.remove(os.path.join(pa_temp_wav, fi))
                st.rerun()        



ca1, ca2, ca3 = st.columns([0.25, 0.25, 0.50])

with ca1:
    do_upload(190, 70)

with ca2:
    with st.container(height=190, border=True):
        prepare_params_for_ffmpeg()
    with st.container(height=70, border=True):   
        convert_wav_and_zip()

with ca3:
    with st.container(height=190, border=True):
        print("ha")
    with st.container(height=70, border=True):     
        frag_do_download()

frag_see_content()

flush()


 