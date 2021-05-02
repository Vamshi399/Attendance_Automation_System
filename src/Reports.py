from PyQt5 import QtCore, QtGui, QtWidgets
from openpyxl import Workbook
import sys
from DBConnection import DBConnection
from TodayAttendance import Ui_TodayAttendance
class Ui_Reports(object):
    def __init__(self, Dialog, unm):
        self.dialog = Dialog
        self.un = unm

    def todayattnce(self):
        try:
            self.viewstdnt = QtWidgets.QDialog()
            self.ui1 = Ui_TodayAttendance()
            self.ui1.setupUi(self.viewstdnt)
            self.ui1.studentdetails()
            self.viewstdnt.show()

        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def download(self):
        try:
            mnth = self.comboBox.currentText()
            wb = Workbook()
            SQL = 'SELECT dt AS "Date",rollno AS "Student ID",name AS "Student Name",sts AS "Attendance" from  attendance'
            database = DBConnection.getConnection()
            cur = database.cursor()
            cur.execute(SQL)
            results = cur.fetchall()
            ws = wb.create_sheet(0)
            ws.title = "Attendance"
            ws.append(cur.column_names)
            for row in results:
                m = row[0].split("-")[1]
                print(m)
                print(mnth)
                if (m == mnth):
                    ws.append(row)
            workbook_name = "Reports"
            wb.save(workbook_name + ".xlsx")

            self.showMessageBox("Information", "Downloaded and save in Reports.xlsx ")

        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print("Error Line no:"+str(tb.tb_lineno)+"   PLZ close Reports.xlsx file")
            print(e)

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 800)
        Dialog.setStyleSheet("background-color: #cbdadb;")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(190, 100, 500, 101))
        self.pushButton.setStyleSheet("color:#cbdadb;\n"
"font: 16pt \"garamond\";\n"
"font-weight: bold;\n"
"background-color:rgb(0,128,128);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.todayattnce)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 250, 500, 101))
        self.label.setStyleSheet("color: rgb(0, 128 , 128);\n"
                                 "font-weight: bold;\n"
                                 "font: 16pt \"garamond\";")
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(200, 350, 171, 101))
        self.comboBox.setStyleSheet("color: rgb(0 , 128 , 128);\n"
                                    "font: 16pt \"garamond\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 510, 500, 101))
        self.pushButton_2.setStyleSheet("color: #cbdadb;\n"
"font: 16pt \"garamond\";\n"
"background-color: rgb(0,128,128);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.download)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Reports"))
        self.pushButton.setText(_translate("Dialog", "Click to view today's Attendance"))
        self.label.setText(_translate("Dialog", "Monthly Reports:"))
        self.comboBox.setItemText(0, _translate("Dialog", "01"))
        self.comboBox.setItemText(1, _translate("Dialog", "02"))
        self.comboBox.setItemText(2, _translate("Dialog", "03"))
        self.comboBox.setItemText(3, _translate("Dialog", "04"))
        self.comboBox.setItemText(4, _translate("Dialog", "05"))
        self.comboBox.setItemText(5, _translate("Dialog", "06"))
        self.comboBox.setItemText(6, _translate("Dialog", "07"))
        self.comboBox.setItemText(7, _translate("Dialog", "08"))
        self.comboBox.setItemText(8, _translate("Dialog", "09"))
        self.comboBox.setItemText(9, _translate("Dialog", "10"))
        self.comboBox.setItemText(10, _translate("Dialog", "11"))
        self.comboBox.setItemText(11, _translate("Dialog", "12"))
        self.pushButton_2.setText(_translate("Dialog", "Click to download  "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
