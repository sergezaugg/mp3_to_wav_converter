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

pa_temp_mp3 = 'temp_mp3'
pa_temp_wav = 'temp_wav'
pa_temp_zip = 'temp_zip'

zip_name_temp = 'zipped_wavs_temp'
zip_name_ext = os.path.join(pa_temp_zip, zip_name_temp + '.zip')

with st.form(key = "f01", border=False, clear_on_submit=True):
    uploaded_files = st.file_uploader("Choose MP3 files", accept_multiple_files=True, type = ['mp3'])
    submitted01 = st.form_submit_button("Upload", type="primary")
    if submitted01: 
        for upfi in uploaded_files:
            bytes_data = upfi.read()
            # st.text(uploaded_file.name)
            # st.text(len(bytes_data))
            with open(os.path.join(pa_temp_mp3, upfi.name), "wb") as f:
                f.write(bytes_data)

with st.form(key = "f03", border=False): 
    submitted03 = st.form_submit_button("Convert to Wav", type="primary")
    if submitted03: 
        for fi in [a for a in os.listdir(pa_temp_mp3) if '.mp3' in a]:
            # print(fi)
            # print(fi[0:-3]+'wav')
            pai = os.path.join(pa_temp_mp3, fi)
            pao = os.path.join(pa_temp_wav, fi[0:-3]+'wav')
            mp3_to_wav(patin = pai, paout = pao, target_fs = 20000)
        # ZIP        
        if os.path.exists(zip_name_ext):
            os.remove(zip_name_ext)       
        shutil.make_archive(base_name = os.path.join(pa_temp_zip, zip_name_temp) , format = 'zip', root_dir = pa_temp_wav) 

# flush (sorry mr hankey)
col_a1, col_a2,= st.columns([0.80, 0.80])
with col_a1: 
    with st.form(key = "f10", border=False):
        submitted10 = st.form_submit_button("Flush MP3s", type="primary")
        if submitted10: 
            for fi in os.listdir(pa_temp_mp3):
                os.remove(os.path.join(pa_temp_mp3, fi))
with col_a2: 
    with st.form(key = "f11", border=False):
        submitted11 = st.form_submit_button("Flush WAVs", type="primary")
        if submitted11:
            os.remove(zip_name_ext)  
            for fi in os.listdir(pa_temp_wav):
                os.remove(os.path.join(pa_temp_wav, fi))
               
# see current contents 
col_a1, col_a2,= st.columns(2)
with col_a1: 
    st.dataframe(os.listdir(pa_temp_mp3), use_container_width = True)
with col_a2: 
    st.dataframe(os.listdir(pa_temp_wav), use_container_width = True)

# download 
if os.path.exists(zip_name_ext):
    with open(zip_name_ext, "rb") as f:
        timstamp = datetime.datetime.now().strftime('%Y%m%dT%H%M%S')   
        st.download_button(label="Download zipped wavs", data=f, file_name = timstamp + '_ziped_wavs.zip')
else:
    st.text("no zip available!")    
  




    