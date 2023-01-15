import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets

from videos_to_images import videosToImages

class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()



    def initUI(self):
        # self.setObjectName("Videos_to_images")
        # self.resize(294, 239)
        
        #label 1 
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 10, 251, 31))
        self.label.setObjectName("label")

        ##select videos ====
        #text
        self.pathvideo = QtWidgets.QLineEdit(self)
        self.pathvideo.setEnabled(True)
        self.pathvideo.setGeometry(QtCore.QRect(20, 40, 221, 21))
        self.pathvideo.setObjectName("pathvideo")
        #button
        self.selectButton = QtWidgets.QPushButton(self)
        self.selectButton.setGeometry(QtCore.QRect(260, 40, 21, 21))
        self.selectButton.setObjectName("selectButton")
        self.selectButton.clicked.connect(self.selectPath) 

        # label 2
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 251, 31))
        self.label_2.setObjectName("label_2")

        ##save images
        #button save
        self.saveButton = QtWidgets.QPushButton(self)
        self.saveButton.setGeometry(QtCore.QRect(260, 100, 21, 21))
        self.saveButton.setObjectName("saveButton")
        self.saveButton.clicked.connect(self.savePath) 
        #text
        self.pathsave = QtWidgets.QLineEdit(self)
        self.pathsave.setEnabled(True)
        self.pathsave.setGeometry(QtCore.QRect(20, 100, 221, 21))
        self.pathsave.setObjectName("pathsave")

        ## label 3
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 251, 31))
        self.label_3.setObjectName("label_3")

        ##select  second
        self.spinBox = QtWidgets.QSpinBox(self)
        self.spinBox.setGeometry(QtCore.QRect(120, 130, 42, 22))
        self.spinBox.setObjectName("spinBox")

        #button for confirmed
        self.convertButton = QtWidgets.QPushButton(self)
        self.convertButton.setGeometry(QtCore.QRect(60, 200, 161, 31))
        self.convertButton.setObjectName("convertButton")
        self.convertButton.clicked.connect(self.videoToImages)

        self.progressBar = QtWidgets.QProgressBar(self)
        self.progressBar.setGeometry(QtCore.QRect(0, 160, 301, 23))
        self.progressBar.setMinimum(0)
        # self.progressBar.setProperty("value", 12)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setFormat("%p%")
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)


        #intialiaze path
        self.pathvideo.setText('C:/')
        self.pathsave.setText('C:/')

    # funtion for select path that contain videos
    def selectPath(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        folder_path = str(QFileDialog.getExistingDirectory(self, options=options))
        self.pathvideo.setText(folder_path)

    # funtion for select path for save images
    def savePath(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        folder_path = str(QFileDialog.getExistingDirectory(self, options=options))
        self.pathsave.setText(folder_path)
    
    #function for convert videos to images
    def videoToImages(self):
        pathvideos = self.pathvideo.text()
        pathsave = self.pathsave.text()
        second = self.spinBox.value()
        print(pathsave,pathvideos,second)
        videosToImages(pathvideos, pathsave,second)


    def retranslateUi(self, Videos_to_images):
        _translate = QtCore.QCoreApplication.translate
        Videos_to_images.setWindowTitle(_translate("Videos_to_images", "Form"))
        self.label.setText(_translate("Videos_to_images", "Select path of your videos:"))
        self.selectButton.setText(_translate("Videos_to_images", "..."))
        self.label_2.setText(_translate("Videos_to_images", "Select path when you want to save your videos:"))
        self.saveButton.setText(_translate("Videos_to_images", "..."))
        self.label_3.setText(_translate("Videos_to_images", "Select image/second:"))
        self.convertButton.setText(_translate("Videos_to_images", "Convert"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
