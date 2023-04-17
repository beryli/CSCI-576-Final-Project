import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_multimedia_player import Ui_MainWindow

if __name__ == "__main__":
    # if len(sys.argv) == 3:
    #     video_file, audio_file = sys.argv[1], sys.argv[2]

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())