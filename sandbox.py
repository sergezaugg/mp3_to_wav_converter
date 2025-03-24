
import ffmpeg
from io import BytesIO
import pathlib
import subprocess
import ffmpeg
import streamlit as st


pa = "C:/xc_real_projects/xc_ne_europe/downloaded_data_orig/Corvus_corax_XC212483_CORRAX_422015_011_0m_12s.mp3"
pout = "C:/Users/sezau/Downloads/aaa/should_be_a_wav_output.wav"



# with open(pa, "rb") as fh:
#     buf = BytesIO(fh.read())
# buf = buf.read()


uploaded_files = st.file_uploader("(1) Choose MP3 files", accept_multiple_files=True, type = ['mp3'])
buf = uploaded_files[0].read()

st.text(type(buf))

# print('convert_mp3_to_wav_ffmpeg_bytes2bytes')
args = (ffmpeg
        .input('pipe:', format='mp3')
        .output('pipe:', format='wav')
        .global_args('-loglevel', 'error')
        .get_args()
        )

['ffmpeg'] + args

stdin=subprocess.PIPE
stdout=subprocess.PIPE

proc = subprocess.Popen(['ffmpeg'] + args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

st.text(type(proc))

aaa = proc.communicate(input=buf)


len(aaa)

# Write the stuff
with open(pout, "wb") as f:
    f.write(aaa[0])








