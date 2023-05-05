import os
import sys
import argparse
from PyQt5 import QtCore, QtGui, QtWidgets
from src.converter import rgb2avi, wav2mp3
from src.Ui_multimedia_player import Ui_MainWindow
from src.video import analyze_video

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-vi', '--input-video',
                        required=True, help='input video filename (.rgb or .avi)', dest='v_in')
    parser.add_argument('-ai', '--input-audio',
                        required=True, help='input audio filename (.wav or .mp3)', dest='a_in')
    parser.add_argument('-vo', '--output-video',
                        default='', help='output video filename (.avi)', dest='v_out')
    parser.add_argument('-ao', '--output-audio',
                        default='', help='output audio filename (.mp3)', dest='a_out')
    parser.add_argument('-nc', '--no-conversion',
                        action='store_true', help='disable video & audio conversion', dest='no_conversion')
    args = parser.parse_args()

    v_name, v_ext = os.path.splitext(args.v_in)
    a_name, a_ext = os.path.splitext(args.a_in)

    video_target = args.v_in
    audio_target = args.a_in

    if args.v_out or v_ext != '.avi':
        video_target = args.v_out if args.v_out else v_name + '.avi'
        rgb2avi(args.v_in, video_target)
    if args.v_out or a_ext != '.mp3':
        audio_target = args.a_out if args.a_out else a_name + '.mp3'
        wav2mp3(args.a_in, args.a_out)

    frames = analyze_video(video_target)

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, video_target, audio_target, frames)
    MainWindow.show()
    sys.exit(app.exec_())
