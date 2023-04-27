#!/usr/bin/python3

import sys

import serial

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import ( QApplication, QMainWindow, QPushButton, QLabel, QDialog, QVBoxLayout, QWidget )



# Subclass QMainWindow to customize your application's main window                      
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Demo")
        self.setFixedSize(QSize(400, 300))
        
        layout = QVBoxLayout()
        
        text_1 = QLabel("GT1")
        text_2 = QLabel("GT2")
        
        button = QPushButton("Clear")

        button.clicked.connect(self.the_button_was_clicked)

        layout.addWidget(text_1)
        layout.addWidget(text_2)
        layout.addWidget(button)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        
    def the_button_was_clicked(self):
        print("Clicked!")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()


