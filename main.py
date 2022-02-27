# File name : QR_CodeGenerator
# Author : HTMLDigger
# Date : Fab 27th 2022
# ## ############################################
#    Main Script.
# ## ############################################

import qrcode
import sys
import os
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PIL.ImageQt import ImageQt

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(372, 327)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.frame_01 = QtWidgets.QFrame(Form)
        self.frame_01.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_01.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_01.setObjectName("frame_01")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_01)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_02 = QtWidgets.QFrame(self.frame_01)
        self.frame_02.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.frame_02.setStyleSheet("background-color: rgb(49, 49, 49);\n"
"border-radius: 5px;")
        self.frame_02.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_02.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_02.setObjectName("frame_02")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_02)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame = QtWidgets.QFrame(self.frame_02)
        self.frame.setStyleSheet("QFrame {\n"
"    border-radius: 5px;\n"
"    border: 2px solid #73AD21;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.QrCode = QtWidgets.QLabel(self.frame)
        self.QrCode.setAlignment(QtCore.Qt.AlignCenter)
        self.QrCode.setObjectName("QrCode")
        self.verticalLayout.addWidget(self.QrCode)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_url = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_url.setStyleSheet("QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding: 0 8px;\n"
"    background: rgb(85, 85, 127);\n"
"    selection-background-color: darkgray;\n"
"}")
        self.lineEdit_url.setObjectName("lineEdit_url")
        self.horizontalLayout.addWidget(self.lineEdit_url)
        self.pushButton_generate = QtWidgets.QPushButton(self.frame)
        self.pushButton_generate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_generate.setStyleSheet("QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 3px;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #B0B3BC, stop: 1 #878DA0);\n"
"    min-width: 80px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #878DA0, stop: 1 #B0B3BC);\n"
"}\n"
"\n"
"QPushButton:flat {\n"
"    border: none; /* no border for a flat push button */\n"
"}\n"
"\n"
"QPushButton:default {\n"
"    border-color: navy; /* make the default button prominent */\n"
"}")
        self.pushButton_generate.setObjectName("pushButton_generate")
        self.horizontalLayout.addWidget(self.pushButton_generate)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_5.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_02, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_01, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.pushButton_generate.released.connect(self.qr_code)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def retranslateUi(self, Form):
        username = os.getlogin()
        # build = 'HTMLDigger'
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "QrCode v1.0.5 using by ({x})").format(x=username))
        self.QrCode.setText(_translate("Form", ""))
        self.pushButton_generate.setText(_translate("Form", "Generate"))

    def qr_code(self):
        url = self.lineEdit_url.text()
        img = qrcode.make(f'{url}')
        GQrCode = img.save('gQrcode_.png')
        pixmap = QPixmap('gQrcode_.png') 
        self.QrCode.setPixmap(pixmap)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

