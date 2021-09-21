import PyQt5 # PyQt5 = library
from PyQt5.QtWidgets import*
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import* # QtCore = module
from PyQt5.QtGui import* # QtGui = user interface
import sys # sys = system

# create class Window
class Window (QMainWindow): # applications used from QMainWindow #QMainWindow = parent function
    def __init__ (self): # self - pointing to the current object
        super(). __init__() 
        # setting the title
        self.setWindowTitle('stopwatch')
        # setting geometry
        self.setGeometry(100,100,400,500)
        # calling method
        self.UiComponents()
        # showing all widgets
        self.show()
    def UiComponents(self):
        self.count = 0 #starting with 0
        #creating flag
        self.flag = False 
        # creating a label for showing time
        self.label = QLabel(self)
        # setting geometry of the label
        self.label.setGeometry(75,100,250,70)
        # adding border to the label
        self.label.setStyleSheet('border: 4px solid black;')
        # setting text to the label
        self.label.setText(str(self.count))
        # setting font for label
        self.label.setFont(QFont('Arial', 24))
        # setting alignment of text of label
        self.label.setAlignment(Qt.AlignCenter)
        # creating start button
        start = QPushButton('START', self)
        start.setGeometry(125, 250, 150, 40)
        # add action to the method
        start.pressed.connect(self.Start)
        # creating pause button
        pause = QPushButton('PAUSE', self)
        pause.setGeometry(125, 300, 150, 40)
        # add action to the method
        pause.pressed.connect(self.Pause)
        # creating reset button
        reset = QPushButton('RESET', self)
        reset.setGeometry(125,350,150,40)
        # add action to the method
        reset.pressed.connect(self.Re_set)
        # creating a timer object
        timer = QTimer(self) # self as it is a timer, no need of label
        timer.timeout.connect(self.showTime)
        # updating timer every 10 seconds
        timer.start(100) # 100 milliseconds
    # method called by timer
    def showTime(self):
        if self.flag:
            self.count +=1 # adding increments of 1
        # getting text from count
        text = str(self.count/10)
        # showing text
        self.label.setText(text)
    def Start(self):
        self.flag = True # making flag = true, starting the timer
    def Pause(self):
        self.flag = False # pausing the timer
    def Re_set(self):
        self.flag = False
        self.count = 0 # timer goes back to 0
        self.label.setText(str(self.count)) 
# creaing PyQt5 app
app = QApplication(sys.argv) 
# create an instant window
window = Window()
sys.exit(app.exec()) # to close app by closing GUI 
