import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Hello World')
        self.setGeometry(100, 100, 600, 600)
        self.setWindowIcon(QIcon('C:/Users/hanoi/OneDrive/Pictures/Wallpaper/CUTE-FACE-WALLPAPER-PC-4K.jpg'))

        label = QLabel('Porn Hub', self)
        label.setFont(QFont('Roboto', 20, QFont.Bold))
        label.setGeometry(200, 200, 200, 50)
        label.setStyleSheet('color: orange;'
                            'background-color: black;'
                            'border-style: solid;'
                            'border-width: 2px;'
                            'border-color: orange;'
                            'border-radius: 10px;')
        label.setAlignment(Qt.AlignCenter)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) # to keep the window open

if __name__ == '__main__':
    main()