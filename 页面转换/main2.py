from a import Ui_MainWindow as A_UI
from b import Ui_MainWindow as B_UI
from c import Ui_MainWindow as C_UI
from PyQt5 import QtCore, QtWidgets
import sys

# 主窗口
class AWindow(QtWidgets.QMainWindow, A_UI):
    switch_windowB = QtCore.pyqtSignal()
    switch_windowC = QtCore.pyqtSignal()

    def __init__(self):
        super(AWindow, self).__init__()
        self.setupUi(self)
        self.btn_A_to_B.clicked.connect(self.go_page_B)
        self.btn_A_to_C.clicked.connect(self.go_page_C)

    def go_page_B(self):
        self.switch_windowB.emit()

    def go_page_C(self):
        self.switch_windowC.emit()


# 页面B
class BWindow(QtWidgets.QMainWindow, B_UI):
    switch_windowA = QtCore.pyqtSignal()

    def __init__(self):
        super(BWindow, self).__init__()
        self.setupUi(self)
        self.btn_B_to_A.clicked.connect(self.go_page_A)

    def go_page_A(self):
        self.switch_windowA.emit()


# 页面C
class CWindow(QtWidgets.QMainWindow, C_UI):
    switch_windowA = QtCore.pyqtSignal()

    def __init__(self):
        super(CWindow, self).__init__()
        self.setupUi(self)
        self.btn_C_to_A.clicked.connect(self.go_page_A)

    def go_page_A(self):
        self.switch_windowA.emit()


# 控制器用于跳转窗口
class Controller:
    def __init__(self):
        pass

    def show_AWindow(self):  #默认
        self.AWindow = AWindow()
        self.AWindow.switch_windowB.connect(self.A_show_BWindow)
        self.AWindow.switch_windowC.connect(self.A_show_CWindow)
        self.AWindow.show()

    def A_show_BWindow(self):
        self.BWindow = BWindow()
        self.BWindow.switch_windowA.connect(self.B_show_AWindow)
        self.AWindow.close()
        self.BWindow.show()

    def B_show_AWindow(self):
        self.AWindow = AWindow()
        self.AWindow.switch_windowB.connect(self.A_show_BWindow)
        self.AWindow.switch_windowC.connect(self.A_show_CWindow)
        self.BWindow.close()
        self.AWindow.show()

    def A_show_CWindow(self):
        self.CWindow = CWindow()
        self.CWindow.switch_windowA.connect(self.C_show_AWindow)
        self.AWindow.close()
        self.CWindow.show()

    def C_show_AWindow(self):
        self.AWindow = AWindow()
        self.AWindow.switch_windowB.connect(self.A_show_BWindow)
        self.AWindow.switch_windowC.connect(self.A_show_CWindow)
        self.CWindow.close()
        self.AWindow.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_AWindow()  #默认展示A页面
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
