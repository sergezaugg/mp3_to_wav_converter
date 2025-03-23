# BATCH CONVERT MP3 TO WAV

### Summary
A Streamlit wrapper around [ffmpeg](https://ffmpeg.org).

Allows to convert many mp3 to wav while controlling the sampling frequency and number of channels. 
      
Only converts to wavs with a bit-depth of 16.
    
Conversion to wav will not correct mp3 artifacts.
    
Was develop for bio-acoustic projects to convert many mp3 downloaded from [xeno-canto](https://xeno-canto.org).
    
Wav files with fixed sampling frequency are easier to handle in ML projects with Python/Pytorch.

Deployed version can be found [here](https://mp3-to-wav-converter.streamlit.app). 


### Dependencies / Intallation
* Developed under Python 3.12.8
* Requires ffmpeg pre-installed

```bash
pip install -r requirements.txt
```

### Usage
To  start the Steamlit dashboard

```bash
streamlit run stmain.py
```




