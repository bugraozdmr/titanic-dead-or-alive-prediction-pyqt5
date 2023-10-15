### Disaster of Titanic
The Titanic, a British passenger liner that set sail on its maiden voyage in 1912, is most famous for its tragic sinking after colliding with an iceberg. This disaster resulted in one of the deadliest peacetime maritime tragedies, claiming the lives of over 1,500 passengers and crew members. The sinking of the Titanic serves as a poignant reminder of the vulnerability of even the most advanced technological achievements when faced with the forces of nature.

I used XGB machine learning algorithm to predict.That gave me 63% ratio which is pretty low.If you want to change parametres I used go ahead.I may find some other parametres in time and after that I can update my code.For now thats all.I may seem like obsessed with Titanic but I really like history of it.







# Things can help you to understand some details

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
