from PyQt5 import QtCore, QtGui, QtWidgets
from Camera import CaptureImage
from DBConnection import DBConnection
import sys
import os
import errno

class Ui_AddStudent(object):

    sts=True
    def getCameraImage(self, event):
        try:
            CaptureImage()
            Ui_AddStudent.sts = False

            self.showMessageBox("Information", "Picture Captured..!")
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        event.accept()

    def addstudents(self):
        try:

            name = self.lineEdit.text()
            rollno = self.lineEdit_2.text()
            if name == "" or name == "null" or rollno == "" or rollno == "null":
                self.showMessageBox("Information", "Please fill out all fields")
            elif Ui_AddStudent.sts:
                self.showMessageBox("Information", "Please Take Picture")
            else:
                imgid = str(rollno) + ".jpg"
                path = "../AttendanceSystem/pictures/" +name+"_"+str(rollno)+"/"
                if not os.path.exists(os.path.dirname(path)):
                    try:
                        os.makedirs(os.path.dirname(path))
                    except OSError as exc:  # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise
                database = DBConnection.getConnection()
                cursor = database.cursor()
                cursor.execute("select count(*) from students where rollno='" + str(rollno) + "'")
                val = cursor.fetchone()[0]
                if val == 1:
                    self.showMessageBox("Information", "Student Roll no already exist..!")
                else:
                    query = "insert into students values(%s,%s,%s)"
                    values = (name, rollno, imgid)
                    cursor.execute(query, values)
                    database.commit()
                    imgdata = self.read_file("addstudentimage.png")
                    self.write_file(imgdata, imgid, path)
                    self.showMessageBox("Information", "Student Added Successfully..!")
                    self.lineEdit.setText("")
                    self.lineEdit_2.setText("")
                    Ui_AddStudent.sts=True



        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)

    def read_file(self, filename):
        with open(filename, 'rb') as f:
            img = f.read()
        return img

    def write_file(self, data, imgid, path):
        with open(path + imgid, 'wb') as f:
            f.write(data)

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 700)
        Dialog.setStyleSheet("background-color: #fff4e6;")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(300, 60, 400, 51))
        self.label.setStyleSheet("color: rgb(139, 65, 19);\n"
                                 "font-weight: bold;\n"
                                 "font: 75 24pt \"garamond\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 150, 251, 51))
        self.label_2.setStyleSheet("color: rgb(139, 69, 19);\n"
        "font: 75 18pt \"garamond\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 200, 251, 51))
        self.lineEdit.setStyleSheet("color: rgb(139, 69, 19);\n"
        "font: 75 18pt \"garamond\";")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(110, 260, 251, 51))
        self.label_3.setStyleSheet("color: rgb(139, 69, 19);\n"
        "font: 75 18pt \"garamond\";")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 320, 251, 51))
        self.lineEdit_2.setStyleSheet("color: rgb(139, 69, 19);\n"
            "font: 75 18pt \"garamond\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.camera = QtWidgets.QLabel(Dialog)
        self.camera.setGeometry(QtCore.QRect(675, 140, 171, 191))
        self.camera.setStyleSheet("image: url(../AttendanceSystem/images/addstudentimage.png);")
        self.camera.setText("")
        self.camera.setObjectName("camera")
        self.camera.mousePressEvent=self.getCameraImage
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(650, 350, 300, 41))
        self.label_5.setStyleSheet("color: rgb(139, 69, 19);\n"
                                   "font: 75 18pt \"garamond\";")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(110, 400, 300, 100))
        self.pushButton.setStyleSheet("font: 75 18pt \"garamond\";\n"
"background-color: rgb(118, 69, 40);\n"
"color: rgb(240, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.addstudents)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add Student"))
        self.label.setText(_translate("Dialog", "Student Registration"))
        self.label_2.setText(_translate("Dialog", "Student Name"))
        self.label_3.setText(_translate("Dialog", "Student ID"))
        self.label_5.setText(_translate("Dialog", "Click on Camera"))
        self.pushButton.setText(_translate("Dialog", "Add Student"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
