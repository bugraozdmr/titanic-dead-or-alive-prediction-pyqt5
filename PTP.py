import sys

from app import Ui_mainDialog
from extra_window import Ui_Dialog

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication,QDialog,QWidget,QStackedWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QButtonGroup

import predict


class infoscreen(QDialog,Ui_Dialog):
    def __init__(self,parent=None):
        super(infoscreen, self).__init__(parent)
        #loadUi(r"C:\Users\bugra\OneDrive\Masaüstü\python_titanic_prediction_pyqt5\extra_window.ui", self)
        self.setupUi(self)


        self.back.clicked.connect(self.go_backk)

    def go_backk(self):

        backscreen = ana()
        widget.addWidget(backscreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

# loadUI degisti cunku setup yapilacak bu dosya duzgun calissin diye
class ana(QDialog,Ui_mainDialog):
    def __init__(self,parent=None):
        super(QDialog,self).__init__(parent)
        #loadUi(r"C:\Users\bugra\OneDrive\Masaüstü\python_titanic_prediction_pyqt5\app.ui",self)

        self.setupUi(self)



        # bazi onemli seyler biliyorsunuz iste

        # info page yeri altta olmali yoksa __init__ ile karisir
        self.open_extra_window_button.clicked.connect(self.infopage)


    # # # # # # # # # # # # # # # # # # # # # #

        self.spin_box_value = 0  # Başlangıç değeri
        self.spinBox_2.valueChanged.connect(self.spin_box_changed)

        ##send
        self.pushButton.clicked.connect(self.send)


        # Sınıf RadioButton'ları için bir grup
        self.sinif_group = QButtonGroup()
        self.sinif_group.addButton(self.radioButton_3)
        self.sinif_group.addButton(self.radioButton_4)
        self.sinif_group.addButton(self.radioButton_5)

        # Yalnız mı RadioButton'ları için bir grup
        self.alone_group = QButtonGroup()
        self.alone_group.addButton(self.radioButton)
        self.alone_group.addButton(self.radioButton_2)

        self.sinif = 0
        self.al0ne = -1


        # Sınıf ve Ders RadioButton'larının sinyallerini bağlayın
        self.sinif_group.buttonClicked.connect(self.sinif_secildi)
        self.alone_group.buttonClicked.connect(self.alone)

    def sinif_secildi(self, sınıf_button):
        if sınıf_button is self.radioButton_3:
            self.sinif = 1
            print(sınıf_button.text())
        elif sınıf_button is self.radioButton_4:
            self.sinif = 2
            print(sınıf_button.text())
        elif sınıf_button is self.radioButton_5:
            self.sinif = 3
            print(sınıf_button.text())

    def alone(self, alone_button):
        # veri setinde yalniz olanlar 0 dost olanlar 1
        if alone_button is self.radioButton:
            self.al0ne = 0
            print(alone_button.text())
        elif alone_button is self.radioButton_2:
            self.al0ne = 1
            print(alone_button.text())


    # spinbox degeri
    def spin_box_changed(self, value):
        # Spin Box değeri değiştiğinde tetiklenir

        # age degeri
        self.spin_box_value = value


    # extra_window

    def infopage(self):
        info = infoscreen()
        widget.addWidget(info)
        widget.setCurrentIndex(widget.currentIndex() + 1)


    # model kurucam gelcem

    def send(self):
        x = self.sinif
        y = self.spin_box_value
        z = self.al0ne

        if((x==0) and (y==0) and (z==-1)):
            self.label_4.setText("Bilgi gir")
        elif((x==0) or (y==0) or (z == -1)):
            self.label_4.setText("Girilmeyen bilgi/ler var")

        else:
            print(x, y, z)

            # yazdirlacak degere bakalim
            if (predict.dondur(x, y, z) == 1):
                self.label_4.setText("MUHTEMELEN YAŞIYOR")
            else:
                self.label_4.setText("MUHTEMELEN ÖLDÜ")




app = QApplication(sys.argv)
ana1 = ana()
widget = QStackedWidget()
widget.addWidget(ana1)
widget.setWindowTitle("Titanic Predict")
widget.setWindowIcon(QIcon(r"C:\Users\bugra\OneDrive\Masaüstü\python_titanic_prediction_pyqt5\titanic.png"))
widget.setFixedWidth(1200)
widget.setFixedHeight(800)
widget.show()



try:
    print("working ...")
    sys.exit(app.exec_())
except:
    print("exiting ...")




# parametreleri degistirip daha yuksek oranlar bulabilirsiniz.

# su anlik koddaki tum hatalari vs olasiliklari dusundum gibi