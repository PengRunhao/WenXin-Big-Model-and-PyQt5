
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import requests
import json
# 获取token
token = requests.request('POST',
                    'https://wenxin.baidu.com/younger/portal/api/oauth/token',
                data={
                    'grant_type':'client_credentials',
                    'client_id':'u6HR9mt3U6uBjsnMlMxi0vRrY1eR2uRx',
                    'client_secret':'bUrBb2X5kkr1rp5WmBHSLYk6mk7aIP0U'},
                    timeout=3)
token = json.loads(token.text)['data']


#print(token)



url = "https://wenxin.baidu.com/younger/portal/api/rest/1.0/ernie/3.0/zeus"



from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):



    def setupUi(self, Dialog):
        Dialog.setObjectName("文本纠错")
        Dialog.resize(521, 651)
        palette = QtGui.QPalette()
        pix = QtGui.QPixmap("BG.jpeg")
        pix = pix.scaled(int(Dialog.width()), int(Dialog.height()))
        palette.setBrush(Dialog.backgroundRole(), QtGui.QBrush(QtGui.QPixmap(pix)))
        Dialog.setPalette(palette)
        Dialog.setAutoFillBackground(True)
        self.text1 = QtWidgets.QTextBrowser(Dialog)
        self.text1.setGeometry(QtCore.QRect(90, 70, 141, 31))
        self.text1.setObjectName("text1")
        self.text_in = QtWidgets.QPlainTextEdit(Dialog)
        self.text_in.setGeometry(QtCore.QRect(90, 120, 361, 111))
        self.text_in.setObjectName("text_in")
        self.text2 = QtWidgets.QTextBrowser(Dialog)
        self.text2.setGeometry(QtCore.QRect(90, 360, 361, 191))
        self.text2.setObjectName("text2")
        self.text_out = QtWidgets.QTextBrowser(Dialog)
        self.text_out.setGeometry(QtCore.QRect(90, 310, 141, 31))
        self.text_out.setObjectName("text_out")
        self.button_ok = QtWidgets.QPushButton(Dialog)
        self.button_ok.setGeometry(QtCore.QRect(350, 250, 93, 28))
        self.button_ok.setObjectName("button_ok")
        self.button_ok.clicked.connect(lambda:self.handleButton_ok())
        self.btn_C_to_A = QtWidgets.QPushButton(Dialog)
        self.btn_C_to_A.setGeometry(QtCore.QRect(10, 20, 93, 28))
        self.btn_C_to_A.setObjectName("button_back")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.show()

    def handleButton_ok(self):
        In=self.text_in.toPlainText()
        payload = {
            'text': '改正下面文本中的错误："'+In+'"',
            'seq_len': 64,
            'task_prompt': 'Correction',
            'dataset_prompt': '',
            'access_token': token,
            'topk': 1,
            'stop_token': ''
        }
        response = requests.request("POST", url, data=payload)

        # print(response.text)

        out = json.loads(response.text)["data"]["result"]
        self.text2.setText(out)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "空间伴侣-文本纠错"))
        self.text1.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">输入待修改文本</p></body></html>"))
        self.text_out.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">修改后的文本</p></body></html>"))
        self.button_ok.setText(_translate("Dialog", "确认"))
        self.btn_C_to_A.setText(_translate("Dialog", "返回"))




