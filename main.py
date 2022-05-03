import os
import sys

from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QFileDialog, QWidget


# os.system(os.getcwd() + "/ffmpeg/ffmpeg.exe -h")

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Media Converter By Ali Alhashim")
        # get current working directory
        self.BASE_DIR = os.getcwd()
        # Creating Button for select Media
        self.SelectMediaBtn = QtWidgets.QPushButton("Select Media File")
        self.SelectMediaBtn.setStyleSheet("padding:10px")
        # Creating Text Line Edit
        self.textLineSelectedMedia = QtWidgets.QLineEdit()
        self.textLineSelectedMedia.setReadOnly(True)
        self.textLineSelectedMedia.setStyleSheet("padding:8px")
        # defining layout
        self.layoutForSelect = QtWidgets.QHBoxLayout(self)
        self.layoutForOptions = QtWidgets.QHBoxLayout(self)
        # adding widget to layout for select media
        self.layoutForSelect.addWidget(self.SelectMediaBtn)
        self.layoutForSelect.addWidget(self.textLineSelectedMedia)
        # Click Action for Button
        self.SelectMediaBtn.clicked.connect(self.selectMediaFile)

    @QtCore.Slot()
    def selectMediaFile(self):
        print("you call def function selectMediaFile ")

        filename = QFileDialog.getOpenFileName(self, 'Open file', self.BASE_DIR, "Media files (*)")
        self.textLineSelectedMedia.setText(filename[0])


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 200)
    widget.show()

    sys.exit(app.exec())
