import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QDate, QTimer, QTime, Qt

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel( self)
        self.date_label = QLabel( self)
        self.timer = QTimer(self) 
        self.iniUI()

    def iniUI(self):
        self.setWindowTitle('Digital Clock')
        self.setGeometry(700, 400, 600, 200)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        vbox.addWidget(self.date_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet('color: rgb(39, 245, 115);'
                                    'background-color: black;'
                                    'border-style: solid;'
                                    'border-width: 5px;'
                                    'border-color: rgb(39, 245, 115);'
                                    'border-radius: 10px;'
                                    'font: 150px;')

        self.date_label.setAlignment(Qt.AlignCenter)
        self.date_label.setStyleSheet('color: rgb(39, 245, 115);'
                                    'background-color: black;'
                                    'border-style: solid;'
                                    'border-width: 5px;'
                                    'border-color: rgb(39, 245, 115);'
                                    'border-radius: 10px;'
                                    'font: 40px;')

        self.timer.start(1000)
        self.timer.timeout.connect(self.showTime)
        self.showTime()

    def showTime(self):
        time = QTime.currentTime().toString('hh:mm:ss')
        date = QDate.currentDate().toString('dddd, MMMM d, yyyy')
        self.time_label.setText(time)
        self.date_label.setText(date)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())