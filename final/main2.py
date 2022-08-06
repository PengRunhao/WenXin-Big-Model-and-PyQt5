from A import Ui_MainWindow as A_UI
from C import Ui_Dialog as C_UI
from B import Ui_Dialog as B_UI
from D import Ui_MainWindow as D_UI
from PyQt5 import QtCore, QtWidgets
import sys


# 主窗口
class AWindow(QtWidgets.QMainWindow, A_UI):
    switch_windowB = QtCore.pyqtSignal()
    switch_windowC = QtCore.pyqtSignal()
    switch_windowD = QtCore.pyqtSignal()
    def __init__(self):
        super(AWindow, self).__init__()
        self.setupUi(self)
        self.btn_A_to_B.clicked.connect(self.go_page_B)
        self.btn_A_to_C.clicked.connect(self.go_page_C)
        self.btn_A_to_D.clicked.connect(self.go_page_D)

    def go_page_B(self):
        self.switch_windowB.emit()

    def go_page_C(self):
        self.switch_windowC.emit()

    def go_page_D(self):
        self.switch_windowD.emit()


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


# 页面D
class DWindow(QtWidgets.QMainWindow, D_UI):
    switch_windowA = QtCore.pyqtSignal()

    def __init__(self):
        super(DWindow, self).__init__()
        self.setupUi(self)
        self.btn_D_to_A.clicked.connect(self.go_page_A)

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
        self.AWindow.switch_windowD.connect(self.A_show_DWindow)
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
        self.AWindow.switch_windowD.connect(self.A_show_DWindow)
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
        self.AWindow.switch_windowD.connect(self.A_show_DWindow)
        self.CWindow.close()
        self.AWindow.show()

    def A_show_DWindow(self):
        self.DWindow = DWindow()
        self.DWindow.switch_windowA.connect(self.D_show_AWindow)
        self.AWindow.close()
        self.DWindow.show()

    def D_show_AWindow(self):
        self.AWindow = AWindow()
        self.AWindow.switch_windowB.connect(self.A_show_BWindow)
        self.AWindow.switch_windowC.connect(self.A_show_CWindow)
        self.AWindow.switch_windowD.connect(self.A_show_DWindow)
        self.DWindow.close()
        self.AWindow.show()



def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_AWindow()  #默认展示A页面
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
