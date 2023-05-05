- [CSCI-576 Final Project](#csci-576-final-project)
  - [Usage with UI](#usage-with-ui)
  - [Prerequisites](#prerequisites)
    - [FFmpeg 6.0](#ffmpeg-60)
    - [Virtual Environment](#virtual-environment)
  - [Usage](#usage)


# CSCI-576 Final Project
This is an integration branch for GUI and video analyzer. All codes must be integrated in this branch before merging into the main branch.

## Usage with UI
-  Go to the directory of InputVideo.rgb and InputAudio.wav (and output.avi and output.mp3). 
```
cd data-directory 
```
- Run code
```
python code-directory\main.py -vi InputVideo.rgb -ai InputAudio.wav
```


## Prerequisites
### FFmpeg 6.0
[FFmpeg 6.0](https://ffmpeg.org/download.html) must be installed on your local machine before running the following code.

### Virtual Environment
Create a virual environment:
```sh
$ python -m venv venv
```

Activate the virtual environment:
- **Linux and MacOS**
```sh
source venv/bin/activate
```
- **Windows**
```sh
.\venv\Scripts\activate
```

Install packages:
```sh
$ python -m pip install -r requirements.txt
```

## Usage
Please view [src/main.py](src/main.py) for details.

```sh
$ python main.py -vi <input-video> [-vo <output-video>] \
                 -ai <input-audio> [-ao <output-audio>]
```
