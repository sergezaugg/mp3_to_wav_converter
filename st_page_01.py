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

pa_temp_mp3 = 'temp_mp3'
pa_temp_wav = 'temp_wav'
pa_temp_zip = 'temp_zip'

# upload mp3 to  temp dir
uploaded_files = st.file_uploader("Choose a MP* file", accept_multiple_files=True)
for upfi in uploaded_files:
    bytes_data = upfi.read()
    # st.text(uploaded_file.name)
    # st.text(len(bytes_data))
    with open(os.path.join(pa_temp_mp3, upfi.name), "wb") as f:
        f.write(bytes_data)

for fi in [a for a in os.listdir(pa_temp_mp3) if '.mp3' in a]:
    print(fi)
    print(fi[0:-3]+'wav')
    pai = os.path.join(pa_temp_mp3, fi)
    pao = os.path.join(pa_temp_wav, fi[0:-3]+'wav')
    mp3_to_wav(patin = pai, paout = pao, target_fs = 20000)

shutil.make_archive(base_name = os.path.join(pa_temp_zip, 'aaa') , format = 'zip', root_dir = pa_temp_wav)

with open(os.path.join(pa_temp_zip, 'aaa.zip'), "rb") as f:
    st.download_button(
        label="Download",
        data=f,
        file_name='downloaded_zipped_wavs.zip'
        )



     