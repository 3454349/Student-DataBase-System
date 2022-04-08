
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog
from PyQt5 import QtGui
from demo import Ui_MainWindow
from student import Student
class MyStudent(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MyStudent, self).__init__()
        self.setupUi(self)
        # self.connecter()
        self.show()
        self.student = Student()

        self.lineEdit_N.setText(str(self.student.N))



    # def connecter(self):
    #     self.pushButton_add_info.clicked.connect(self.add_info)
    #     self.pushButton_clear.clicked.connect(self.clear_list)
    #     self.pushButton_find.clicked.connect(self.find)
    #     self.pushButton_add_photh.clicked.connect(self.load_photo)
    #     self.pushButton_close.clicked.connect(self.close)
    #     self.pushButton_delete.clicked.connect(self.delete)
    def quit(self):
        quit()
    def find(self):
        xm = self.lineEdit_find.text()
        xm1= self.student.indexOf(xm)
        self.lineEdit_fingxm.setText(str(xm1[0]))
        self.lineEdit_findxh.setText(str(xm1[1]))
        self.lineEdit_findsr.setText(str(xm1[2]))
        self.lineEdit_findxb.setText(str(xm1[3]))
        # 在label控件上显示选择的图片
        self.label_image2.setPixmap(self.student.img)

    def delete(self):
        i = int(self.lineEdit_delete.text())
        self.student.remove(i)

        self.lineEdit_N.setText(str(self.student.N))
    def clear_list(self):
        self.student.clear()

        self.lineEdit_N.setText(str(self.student.N))


    def add_info(self):
        sr = self.lineEdit_sr.text()
        xh = self.lineEdit_xh.text()
        xm = self.lineEdit_xm.text()
        xb = self.comboBox_xb.currentText()
        i = int(self.lineEdit_index.text())
        print(sr,xh,xm,xb,i)
        self.student.insert(i, xm, xb, xh, sr, jpg)

        self.lineEdit_N.setText(str(self.student.N))

    def load_photo(self):  # 选择本地图片上传
        imgName, imgType = QFileDialog.getOpenFileName(self.pushButton_add_photh, "打开图片", "",
                                                       "*.jpg;;*.png;;All Files(*)")  # 弹出一个文件选择框，第一个返回值imgName记录选中的文件路径+文件名，第二个返回值imgType记录文件的类型
        global jpg
        jpg = QtGui.QPixmap(imgName).scaled(self.label_image1.width(),
                                            self.label_image1.height())  # 通过文件路径获取图片文件，并设置图片长宽为label控件的长款
        self.label_image1.setPixmap(jpg)  # 在label控件上显示选择的图片
        self.student.img = jpg


def main():
    app = QApplication(sys.argv)  # 建立QApplication对象并且放入系统传入参数
    Window = MyStudent()  # 建立MainWindow对象
    sys.exit(app.exec_())  # 进入app.exec_事件循环当退出循环后系统整体退出

#
if __name__ == "__main__":  # 当运行本文件时运行以下内容
    main()
