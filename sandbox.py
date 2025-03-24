
import ffmpeg
from io import BytesIO
import pathlib
import subprocess
import ffmpeg
import streamlit as st


# pure python
pain = "C:/xc_real_projects/xc_ne_europe/downloaded_data_orig/Corvus_corax_XC212483_CORRAX_422015_011_0m_12s.mp3"

pout = "C:/Users/sezau/Downloads/aaa/should_be_a_wav_output.wav"

with open(pain, "rb") as fh:
    buf = BytesIO(fh.read())
buf = buf.read()

args = (ffmpeg
        .input('pipe:', format='mp3')
        .output('pipe:', format='wav', ar = 18400, ac = 2)
        .global_args('-loglevel', 'error')
        .get_args()
        )

proc = subprocess.Popen(['ffmpeg'] + args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

wave_bytes = proc.communicate(input=buf)
# Write the stuff
with open(pout, "wb") as f:
    f.write(wave_bytes[0])




# ---------------------------------------------
# streamlit 

uploaded_files = st.file_uploader("(1) Choose MP3 files", accept_multiple_files=True, type = ['mp3'])
buf = uploaded_files[0].read()


for uf in uploaded_files:

    pout = "C:/Users/sezau/Downloads/aaa/" + uf.name + ".wav"

    args = (ffmpeg
            .input('pipe:', format='mp3')
            .output('pipe:', format='wav', ar = 18400)
            .global_args('-loglevel', 'error')
            .get_args()
            )

    proc = subprocess.Popen(['ffmpeg'] + args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    st.text(type(proc))

    # 
    buf = uf.read()
    wave_bytes = proc.communicate(input=buf)
    # Write the stuff
    with open(pout, "wb") as f:
        f.write(wave_bytes[0])




# ['ffmpeg'] + args
# stdin=subprocess.PIPE
# stdout=subprocess.PIPE




