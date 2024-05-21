from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu,QPushButton,QWidget
#from PyQt5 import QtGui
import sys

def window():
    app =QApplication(sys.argv)
    w = QWidget()
    b = QPushButton(w)
    b.setText("Hello World!")
    b.move(50,20)
    w.setGeometry(1100,410,300,200)
    w.setWindowTitle('PyQt')
    w.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
 window()
