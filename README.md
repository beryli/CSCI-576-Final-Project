- [CSCI-576 Final Project](#csci-576-final-project)
  - [Summary](#summary)
  - [Prerequisites](#prerequisites)
    - [FFmpeg 6.0](#ffmpeg-60)
    - [Virtual Environment](#virtual-environment)
  - [Usage](#usage)


# CSCI-576 Final Project
contributed by < `beryli`, `NTUT-Vincent`, `haojungc` >

## Summary
This is the final project for CSCI-576 Multimedia Systems Design course at University of Southern California. It is a video player with GUI that analyzes an input video and labels frames with different frame types, `SCENE`, `SHOT`, and `SUBSHOT`. Aside from `Play`, `Pause`, and `Stop`, it also supports random access to each scene, shot, and subshot.

<!-- <center><video width="500" height="300" controls>
  <source src="[assets/demo.mp4](https://github.com/beryli/CSCI-576-Final-Project/assets/41893853/42a327ac-f31c-424a-b008-ba462f45af07)" type="video/mp4">
Your browser does not support the video tag.
</video></center> -->

<center>
<video src='https://github.com/beryli/CSCI-576-Final-Project/assets/41893853/42a327ac-f31c-424a-b008-ba462f45af07' width=250/> | <video src='https://github.com/beryli/CSCI-576-Final-Project/assets/41893853/a677cdb7-fe3e-4461-8dce-67c9dfe82d7a' width=250/>
</center>

<!-- https://github.com/beryli/CSCI-576-Final-Project/assets/41893853/42a327ac-f31c-424a-b008-ba462f45af07 -->
<!-- https://github.com/beryli/CSCI-576-Final-Project/assets/41893853/a677cdb7-fe3e-4461-8dce-67c9dfe82d7a -->




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
$ source venv/bin/activate
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
```sh
$ python main.py -vi <input-video> [-vo <output-video>] \
                 -ai <input-audio> [-ao <output-audio>]
```
Please view [main.py](main.py) for details.
