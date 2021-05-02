from PyQt5 import QtCore, QtGui, QtWidgets
from AdminHome import Ui_AdminHome
import sys
class Ui_Admin(object):
    def __init__(self, Dialog):
        self.dialog = Dialog

    def logincheck(self):
        try:
            unm = self.lineEdit.text()
            pwd = self.lineEdit_2.text()
            if unm == "" or unm == "null" or pwd == "" or pwd == "null":
                self.showMessageBox("Information", "Please fill out all fields")
            else:
                if unm == "admin" and pwd == "admin":
                    self.home = QtWidgets.QDialog()
                    self.ui = Ui_AdminHome(self.home,unm)
                    self.ui.setupUi(self.home)
                    self.home.show()
                    self.dialog.hide()

                else:
                    self.showMessageBox("Information", "Invalid Credentials..!")
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1300, 900)
        Dialog.setStyleSheet("background-color: rgb(69, 69, 69);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(450, 50, 751, 100))
        self.label.setStyleSheet("font: 30pt \"garamond\";\n"
"color: rgb(255, 127, 80);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(300, 150, 551, 100))
        self.label_2.setStyleSheet("color: rgb(255,127,80);\n"
"font: 75 18pt \"garamond\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(300, 250, 521, 51))
        self.lineEdit.setStyleSheet("color: rgb(255,255, 255);\n"
"font: 75 18pt \"garamond\";")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(300, 330, 551, 31))
        self.label_3.setStyleSheet("color: rgb(255,127,80);\n"
"font: 75 18pt \"garamond\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(300, 380, 521, 51))
        self.lineEdit_2.setStyleSheet("color: rgb(255,255, 255);\n"
"font: 75 18pt \"garamond\";")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(300, 500, 300, 100))
        self.pushButton.setStyleSheet("background-color: rgb(128, 128, 128);\n"
"font: 75 20pt \"garamond\";\n"
"font-weight: bold;\n"
"color: rgb(255, 127 , 80);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.logincheck)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(900, 160, 281, 351))
        self.label_4.setStyleSheet("image: url(../AttendanceSystem/images/admin2.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Admin Login"))
        self.label.setText(_translate("Dialog", " Admin Login"))
        self.label_2.setText(_translate("Dialog", "User Name"))
        self.label_3.setText(_translate("Dialog", "Password"))
        self.pushButton.setWhatsThis(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">ASASA</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Admin()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

