in order to make setup file first we need to change ui type to .py


pyuic5 app.ui -o app.py 
pyuic5 extra_window.ui -o extra_window.py 


# here is the code
# loadUI degisti cunku setup yapilacak bu dosya duzgun calissin diye
class ana(QDialog,Ui_mainDialog):
    def __init__(self,parent=None):
        super(QDialog,self).__init__(parent)
        #loadUi(r"C:\Users\bugra\OneDrive\Masaüstü\python_titanic_prediction_pyqt5\app.ui",self)

        self.setupUi(self)