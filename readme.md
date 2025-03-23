# BATCH CONVERT MP3 TO WAV

### Summary
Allows to convert many mp3 to wav while controlling the sampling frequency and number of channels. 
    
Uses [ffmpeg](https://ffmpeg.org) in the back. 
    
Only converts to wavs with a bit-depth of 16.
    
Conversion to wav will not correct mp3 artifacts.
    
Was develop for bio-acoustic projects to convert many mp3 downloaded from [xeno-canto](https://xeno-canto.org).
    
Wav files with fixed sampling frequency are easier to handle in ML projects with Python/Pytorch.


### Dependencies / Intallation
* Developed under Python 3.12.8
* Needs ffmpeg pre-installed
```
pip install -r requirements.txt
```




