

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from Camera1 import CaptureImage
from DBConnection import DBConnection
from Predict_KNN import face_recognition,predict,show_prediction_labels_on_image,train
import sys
from Mail import mailsend
import os
import datetime

class Ui_Attendances(object):
    unmlist = []

    def __init__(self, Dialog, unm):
        self.dialog = Dialog
        self.un = unm

    def getCameraImage(self, event):
        try:
            CaptureImage()
            self.showMessageBox("Information", "Picture Captured..!")
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        event.accept()

    def browse_file(self,event):
        try:
            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File")
            img =self.read_file(fileName)
            self.write_file(img)
            self.showMessageBox("Information", "Picture Loaded..!")

        except Exception as e:
            print("error",e)
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            event.accept()


    def read_file(self, filename):
        with open(filename, 'rb') as f:
            img = f.read()
        return img

    def write_file(self,data):
        with open("../AttendanceSystem/test/cameraimg.jpg", 'wb') as f:
            f.write(data)

    def submit(self):
        try:
            namelist = []
            namelist.clear()

            print("Training KNN classifier...")
            classifier = train("../AttendanceSystem/pictures", model_save_path="trained_knn_model.clf", n_neighbors=1)
            print("Training complete!")

            # STEP 2: Using the trained classifier, make predictions for unknown images
            for image_file in os.listdir("../AttendanceSystem/test"):
                full_file_path = os.path.join("../AttendanceSystem/test", image_file)

                print("Looking for faces in {}".format(image_file))

                # Find all people in the image using a trained classifier model
                # Note: You can pass in either a classifier file name or a classifier model instance
                predictions = predict(full_file_path, model_path="trained_knn_model.clf")

                # Print results on the console
                for name, (top, right, bottom, left) in predictions:

                    namelist.append(name.split("_")[1])
                    print("- Found {} at ({}, {})".format(name, left, top))

                # Display results overlaid on an image
                show_prediction_labels_on_image(os.path.join("../AttendanceSystem/test", image_file), predictions)

            print(namelist)
            # self.setNames(namelist)
            database = DBConnection.getConnection()
            cursor = database.cursor()
            for nm in namelist:
                sql = "insert into temp values('" + str(nm) + "')"
                cursor.execute(sql)
                database.commit()
            self.showMessageBox("Information", "Submited picture..!")

        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)

    def closed(self):
        try:
            unmlist = []
            unmlist.clear()
            abstlist=""
            #abstlist.clear()
            database = DBConnection.getConnection()
            cursor = database.cursor()

            cursor.execute("select stdntrno from temp")
            rows = cursor.fetchall()
            for r in rows:
                unmlist.append(r[0])

            cursor.execute("select name,rollno from students")
            row = cursor.fetchall()
            for r in row:
                nm = r[0]
                rno=r[1]
                if rno in unmlist:

                    sql = "insert into attendance values(%s,%s,%s,%s)"
                    values = (r[1], nm, str(datetime.datetime.now().date()), "P")
                    cursor.execute(sql, values)
                    database.commit()
                    # print("p"+str(r[0]))
                else:
                    abstlist=abstlist+str(r[0])+"\n"
                    sql = "insert into attendance values(%s,%s,%s,%s)"
                    values = (r[1], nm, str(datetime.datetime.now().date()), "A")
                    cursor.execute(sql, values)
                    database.commit()
                    # print("A"+str(r[0]))
            cursor.execute("delete from temp")
            database.commit()
            cursor.execute("select email from faculty where factid='"+self.un+"' ")
            email = cursor.fetchone()[0]
            mailsend(email, abstlist)
            self.showMessageBox("Information", "Attendance Submitted and Email Sent..!")



        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
            print(e)

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setNames(self, nmlist):
        self.unmlist = nmlist

    def getNames(self):
        self.unmlist

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 800)
        Dialog.setStyleSheet("color: rgb(250, 242, 230);\n"
                             "background-color: rgb(102, 131, 169);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(430, 50, 400, 51))
        self.label.setStyleSheet("color: rgb(250, 242, 230);\n"
            "font: 75 25pt \"garamond\";")
        self.label.setObjectName("label")
        self.camera = QtWidgets.QLabel(Dialog)
        self.camera.setGeometry(QtCore.QRect(370, 170, 161, 200))
        self.camera.setStyleSheet("image: url(../AttendanceSystem/images/camera4.png);")
        self.camera.setText("")
        self.camera.setObjectName("camera")
        self.camera.mousePressEvent = self.getCameraImage
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(350, 400, 281, 51))
        self.label_5.setStyleSheet("color:rgb(250, 242, 230);\n"
            "font: 75 14pt \"garamond\";")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(500 , 500, 251, 61))
        self.pushButton.setStyleSheet("font: 75 16pt \"garamond\";\n"
"background-color: rgb(85, 170, 127);\n"
"color: rgb(250, 242, 230);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.submit)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 600, 251, 61))
        self.pushButton_2.setStyleSheet("font: 75 16pt \"garamond\";\n"
"background-color: rgb(138, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.closed)
        self.camera_2 = QtWidgets.QLabel(Dialog)
        self.camera_2.setGeometry(QtCore.QRect(700, 170, 161, 200))
        self.camera_2.setStyleSheet("image: url(../AttendanceSystem/images/gal2.png);")
        self.camera_2.setText("")
        self.camera_2.setObjectName("camera_2")
        self.camera_2.mousePressEvent = self.browse_file
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(730, 400, 281, 51))
        self.label_6.setStyleSheet("color: rgb (250, 242, 230);\n"
            "font: 75 14pt \"garamond\";")
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Take Attendance"))
        self.label.setText(_translate("Dialog", "Capture Attendance"))
        self.label_5.setText(_translate("Dialog", "Click on the Camera"))
        self.pushButton.setText(_translate("Dialog", "Submit"))
        self.pushButton_2.setText(_translate("Dialog", "Send an email"))
        self.label_6.setText(_translate("Dialog", "Browse an image"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Attendances()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

