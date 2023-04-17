# Video & Audio

## Prerequisites
Install required packages by running:
```sh
$ python -m pip install -r requirements.txt
```

## Usage
### Play Audio
```python
import time
import audio

audio.init()
audio.load(filename)

audio.play(start)   # plays audio at `start` seconds (float number), default: 0.0

# true if audio is playing, false otherwise
while audio.get_busy():
    time.sleep(0.05)

audio.unload()
```
### Convert .rgb to .avi (w/ audio)
[FFmpeg 6.0](https://ffmpeg.org/download.html) must be installed on your local machine before running the following code.
```python
import video
video.rgb2avi(video_in, audio_in, video_out)
```