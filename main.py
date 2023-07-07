# 静态载入
import sys
from functools import partial

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication

from ui_mainwindow import Ui_MainWindow


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.is_first_move = True

        # 大概是继承了 Ui_MainWindow 的缘故，这里直接使用 setupUI()
        self.setupUi(self)

        # 图像显示窗口内控件
        self.class_page_widget = [[self.widget_p1], [self.widget_p2, self.widget_p3],
                                   [self.widget_p4, self.widget_p5, self.widget_p6, self.widget_p7],
                                   [self.widget_p9, self.widget_p10, self.widget_p11, self.widget_p12, self.widget_p13,self.widget_p14, self.widget_p15, self.widget_p16, self.widget_p17]]
        self.class_page_openGLWidget = [[self.openGLWidget_p1], [self.openGLWidget_p2, self.openGLWidget_p3],
                                         [self.openGLWidget_p4, self.openGLWidget_p5, self.openGLWidget_p6,self.openGLWidget_p7],
                                         [self.openGLWidget_p9, self.openGLWidget_p10, self.openGLWidget_p11,self.openGLWidget_p12, self.openGLWidget_p13,self.openGLWidget_p14, self.openGLWidget_p15, self.openGLWidget_p16,self.openGLWidget_p17]]
        self.class_page_label = [[self.label_p1], [self.label_p2, self.label_p3],
                                   [self.label_p4, self.label_p5, self.label_p6, self.label_p7],
                                   [self.label_p9, self.label_p10, self.label_p11, self.label_p12, self.label_p13,self.label_p14, self.label_p15, self.label_p16, self.label_p17]]
        self.class_page_btn = [[[self.pushButton_p1_1,self.pushButton_p1_2,self.pushButton_p1_3]],[[self.pushButton_p2_1,self.pushButton_p2_2,self.pushButton_p2_3],[self.pushButton_p3_1,self.pushButton_p3_2,self.pushButton_p3_3]],
                               [[self.pushButton_p4_1,self.pushButton_p4_2,self.pushButton_p4_3],[self.pushButton_p5_1,self.pushButton_p5_2,self.pushButton_p5_3],[self.pushButton_p6_1,self.pushButton_p6_2,self.pushButton_p6_3],[self.pushButton_p7_1,self.pushButton_p7_2,self.pushButton_p7_3]],
                               [[self.pushButton_p9_1,self.pushButton_p9_2,self.pushButton_p9_3],[self.pushButton_p10_1,self.pushButton_p10_2,self.pushButton_p10_3],[self.pushButton_p11_1,self.pushButton_p11_2,self.pushButton_p11_3],[self.pushButton_p12_1,self.pushButton_p12_2,self.pushButton_p12_3],[self.pushButton_p13_1,self.pushButton_p13_2,self.pushButton_p13_3],[self.pushButton_p14_1,self.pushButton_p14_2,self.pushButton_p14_3],[self.pushButton_p15_1,self.pushButton_p15_2,self.pushButton_p15_3],[self.pushButton_p16_1,self.pushButton_p16_2,self.pushButton_p16_3],[self.pushButton_p17_1,self.pushButton_p17_2,self.pushButton_p17_3]]]

        self.signal()

        self.show()

        # 使用functools.partial创建一个带有参数的函数
        # partial_function = partial(self.resizeGL, 3)
        # 使用QTimer.singleShot()方法在100毫秒后执行partial_function函数
        QTimer.singleShot(100, self.resizeGL)

    def signal(self):
        self.ptn_ok.clicked.connect(self.composeOk)
        # self.toolButton_4.clicked.connect(MainWindow.ProfectManagement)
        # self.pushButton_11.clicked.connect(MainWindow.Run)
        # self.pushButton_12.clicked.connect(MainWindow.Stop)
        # self.pushButton_13.clicked.connect(MainWindow.ShowCompose)
        # self.pushButton_p1_1.clicked.connect(MainWindow.ShowOpencv)
        # self.pushButton_p1_2.clicked.connect(MainWindow.Full)
        # self.pushButton_p1_3.clicked.connect(MainWindow.RunOpencv)

    def resizeGL(self):
        '''设置图像显示窗口内控件大小位置'''
        self.comboBox_type = int(self.comboBox.currentIndex())
        for i in range(len(self.class_page_widget[self.comboBox_type])):
            parentWidth = self.class_page_widget[self.comboBox_type][i].width()
            parentHeight = self.class_page_widget[self.comboBox_type][i].height()
            if parentWidth >= parentHeight * 1.5:
                expectedWidth =  int(parentHeight * 1.5)
                expectedHeight = parentHeight
                self.class_page_openGLWidget[self.comboBox_type][i].setGeometry(int((parentWidth - expectedWidth) / 2), 0, expectedWidth, expectedHeight)
            else:
                expectedWidth = parentWidth
                expectedHeight = int(parentWidth / 1.5)
                self.class_page_openGLWidget[self.comboBox_type][i].setGeometry(0, int((parentHeight - expectedHeight) / 2), expectedWidth, expectedHeight)

            self.class_page_label[self.comboBox_type][i].move(10, 10)
            self.class_page_btn[self.comboBox_type][i][0].move(self.class_page_widget[self.comboBox_type][i].width() - 130, 0)
            self.class_page_btn[self.comboBox_type][i][1].move(self.class_page_widget[self.comboBox_type][i].width() - 70, 0)
            self.class_page_btn[self.comboBox_type][i][2].move(self.class_page_widget[self.comboBox_type][i].width() - 30, 0)

    def composeOk(self):
        '''切换图像显示模块的排版'''
        self.comboBox_type = int(self.comboBox.currentIndex())
        self.stackedWidget_3.setCurrentIndex(self.comboBox_type)
        self.resizeGL()

    def resizeEvent(self, event):
        if self.is_first_move:
            # 在第一次移动时执行特定的代码逻辑
            self.is_first_move = False
            return
        self.resizeGL()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())