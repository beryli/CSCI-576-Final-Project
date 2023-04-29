import sys
import argparse
from PyQt5 import QtCore, QtGui, QtWidgets
from src.converter import rgb2avi, wav2mp3
from src.Ui_multimedia_player import Ui_MainWindow
from src.video import analyze_video

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-vi', '--input-video',
                        required=True, metavar='<input-video>', dest='v_in')
    parser.add_argument('-ai', '--input-audio',
                        required=True, metavar='<input-audio>', dest='a_in')
    parser.add_argument('-vo', '--output-video',
                        default='output.avi', metavar='<output-video>', dest='v_out')
    parser.add_argument('-ao', '--output-audio',
                        default='output.mp3', metavar='<output-audio>', dest='a_out')
    args = parser.parse_args()
    
    # rgb2avi(args.v_in, args.v_out)
    # wav2mp3(args.a_in, args.a_out)

    frames = analyze_video(args.v_out)

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, args.v_out, args.a_out, frames)
    MainWindow.show()
    sys.exit(app.exec_())