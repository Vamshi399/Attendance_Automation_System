from PyQt5 import QtCore, QtGui, QtWidgets
from Register import Ui_Register
from FacultyHome import Ui_FacultyHome
from DBConnection import DBConnection
import sys
class Ui_Faculty(object):
    def __init__(self, Dialog):
        self.dialog = Dialog

    def register(self, event):
        try:
            self.reg = QtWidgets.QDialog()
            self.ui = Ui_Register(self.reg)
            self.ui.setupUi(self.reg)
            self.reg.show()
            event.accept()
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def facultylogin(self):
        try:
            database = DBConnection.getConnection()
            cursor = database.cursor()
            unm = self.lineEdit.text()
            pwd = self.lineEdit_2.text()
            if unm == "" or unm == "null" or pwd == "" or pwd == "null":
                self.showMessageBox("Information", "Please fill out all fields")
            else:
                sql = "select count(*) from faculty where factid='" + unm + "' and pwd='" + pwd + "'"
                cursor.execute(sql)
                res = cursor.fetchone()[0]
                if res > 0:
                    self.fachome = QtWidgets.QDialog()
                    self.ui1 = Ui_FacultyHome(self.fachome, unm)
                    self.ui1.setupUi(self.fachome)
                    self.fachome.show()
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
        Dialog.resize(1100, 650)
        Dialog.setStyleSheet("background-color:rgb(192,192,192);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 1000, 101))
        self.label.setStyleSheet("font: 25pt \"garamond\";\n"
                                 "font-weight: bold;\n"
"color:	rgb(255,69,0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(400, 50, 500, 51))
        self.label_2.setStyleSheet("color:	rgb(139,69,19);\n"
                                   "font-weight: bold;\n"
"font: 75 18pt \"garamond\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(400, 120, 251, 51))
        self.lineEdit.setStyleSheet("color:	rgb(139,69,19);\n"
                                    "font-weight: bold;\n"
 "font: 75 12pt \"garamond\";")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(400, 190, 221, 51))
        self.label_3.setStyleSheet("color:	rgb(139,69,19);\n"
                                   "font-weight: bold;\n"
"font: 75 18pt \"garamond\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(400, 260, 251, 51))
        self.lineEdit_2.setStyleSheet("color: rgb(139,69,19);\n"
            "font: 75 12pt \"garamond\";")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(400, 350, 260, 100))
        self.pushButton.setStyleSheet("background-color: rgb(255,165,0);\n"
"font: 75 18pt \"garamond\";\n"
"font-weight: bold;\n"
"color: rgb(139,69,19);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.facultylogin)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(0, 50, 400, 291))
        self.label_4.setStyleSheet("image: url(../AttendanceSystem/images/facultylogin.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.register_2 = QtWidgets.QLabel(Dialog)
        self.register_2.setGeometry(QtCore.QRect(690, 400, 400, 291))
        self.register_2.setStyleSheet("image: url(../AttendanceSystem/images/register-now.png);")
        self.register_2.setText("")
        self.register_2.setObjectName("register_2")
        self.register_2.mousePressEvent = self.register

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Faculty Login"))
       # self.label.setText(_translate("Dialog", "        Faculty Login"))
        self.label_2.setText(_translate("Dialog", "Faculty ID"))
        self.label_3.setText(_translate("Dialog", "Password"))
        self.pushButton.setWhatsThis(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">ASASA</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Login"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
