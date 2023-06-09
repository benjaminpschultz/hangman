# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hangman.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import PyQt5, random
from PyQt5 import QtCore, QtGui, QtWidgets
if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
count: int = 0
chances: int = 6
puzzle: list = []
solution: list = []
usedLetters: list = []
class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(821, 735)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.hangManGraphic = QtWidgets.QLabel(self.centralwidget)
        self.hangManGraphic.setGeometry(QtCore.QRect(220, 0, 331, 362))
        self.hangManGraphic.setMinimumSize(QtCore.QSize(331, 362))
        self.hangManGraphic.setMaximumSize(QtCore.QSize(331, 361))
        self.hangManGraphic.setAlignment(QtCore.Qt.AlignCenter)
        self.hangManGraphic.setObjectName("hangManGraphic")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(330, 590, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.submitButton.setFont(font)
        self.submitButton.setObjectName("submitButton")
        self.submitButton.clicked.connect(self.submitGuess)
        self.vgButton = QtWidgets.QRadioButton(self.centralwidget)
        self.vgButton.setGeometry(QtCore.QRect(190, 440, 151, 19))
        self.vgButton.setObjectName("vgButton")
        self.vgButton.setChecked(True)
        self.horrorButton = QtWidgets.QRadioButton(self.centralwidget)
        self.horrorButton.setGeometry(QtCore.QRect(190, 500, 101, 19))
        self.horrorButton.setObjectName("horrorButton")
        self.presidentsButton = QtWidgets.QRadioButton(self.centralwidget)
        self.presidentsButton.setGeometry(QtCore.QRect(460, 440, 88, 19))
        self.presidentsButton.setObjectName("presidentsButton")
        self.sportsButton = QtWidgets.QRadioButton(self.centralwidget)
        self.sportsButton.setGeometry(QtCore.QRect(460, 500, 88, 19))
        self.sportsButton.setObjectName("sportsButton")
        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(330, 540, 111, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.hide()
        self.solution = QtWidgets.QLabel(self.centralwidget)
        self.solution.setGeometry(QtCore.QRect(210, 379, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.solution.setFont(font)
        self.solution.setText("")
        self.solution.setAlignment(QtCore.Qt.AlignCenter)
        self.solution.setObjectName("solution")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 821, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.hangManGraphic.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt;\"> O</span></p><p><span style=\" font-size:36pt;\">/|\\</span></p><p><span style=\" font-size:36pt;\">/ \\</span></p></body></html>"))
        self.submitButton.setText(_translate("MainWindow", "Submit"))
        self.vgButton.setText(_translate("MainWindow", "Video Game Characters"))
        self.horrorButton.setText(_translate("MainWindow", "Horror Movies"))
        self.presidentsButton.setText(_translate("MainWindow", "Presidents"))
        self.sportsButton.setText(_translate("MainWindow", "Sports"))
    
        
    def submitGuess(self):
        videoGames = [['M', 'A', 'R', 'I', 'O', ' ', 'A', 'N', 'D', ' ', 'L', 'U', 'I', 'G', 'I'],
                      ['S', 'A', 'M', 'U', 'S'],
                      ['S', 'O', 'N', 'I', 'C'],
                      ['M', 'A', 'S', 'T', 'E', 'R', ' ', 'C', 'H', 'I', 'E', 'F'],
                      ['S','E', 'P', 'H', 'I', 'R', 'O', 'T', 'H'],
                      ['A', 'L', 'B', 'E', 'R', 'T', ' ', 'W', 'E', 'S', 'K', 'E', 'R']]
        horror = [['S', 'C', 'R', 'E', 'A', 'M'],
                  ['H', 'A', 'L', 'L', 'O', 'W', 'E', 'E', 'N'],
                  ['A', 'L', 'I', 'E', 'N'],
                  ['H', 'E', 'L', 'L', 'R', 'A', 'I', 'S', 'E', 'R'],
                  ['P', 'A', 'R', 'A', 'N', 'O', 'R', 'M', 'A', 'L', ' ', 'A', 'C', 'T', 'I', 'V', 'I', 'T', 'Y'],
                  ['T', 'H', 'E', ' ', 'R', 'I', 'N', 'G']]
        sports = [['H', 'O', 'C', 'K', 'E', 'Y'],
                  ['F', 'O', 'O', 'T', 'B', 'A', 'L', 'L'],
                  ['S', 'O', 'C', 'C', 'E', 'R'],
                  ['B', 'A', 'S', 'E', 'B', 'A', 'L', 'L'],
                  ['W', 'R', 'E', 'S', 'T', 'L', 'I', 'N', 'G'],
                  ['L', 'A', 'C', 'R', 'O', 'S', 'S', 'E']]
        presidents = [['J', 'O', 'E', ' ', 'B', 'I', 'D', 'E', 'N'],
                      ['H', 'E', 'R', 'B', 'E', 'R', 'T', ' ', 'H', 'O', 'O', 'V', 'E', 'R'],
                      ['G', 'E', 'O', 'R', 'G', 'E', ' ', 'W', 'A', 'S', 'H', 'I', 'N', 'G', 'T', 'O', 'N'],
                      ['A', 'B', 'E', ' ', 'L', 'I', 'N', 'C', 'O', 'L', 'N'],
                      ['H', 'A', 'R', 'R', 'Y', ' ', 'T', 'R', 'U', 'M', 'A', 'N'],
                      ['J', 'O', 'H', 'N', ' ', 'A', 'D', 'A', 'M', 'S']]
        global count
        global puzzle
        global solution
        global chances
        global usedLetters
        if count % 2 == 0:
            
            
            if self.vgButton.isChecked():
                number = random.randint(0,5)
                solution = videoGames[number]
                for i in solution:
                    if i == ' ':
                        puzzle.append('  ')
                    else:
                        puzzle.append('_ ')
            elif self.presidentsButton.isChecked():
                number = random.randint(0,5)
                solution = presidents[number]
                for i in solution:
                    if i == ' ':
                        puzzle.append('  ')
                    else:
                        puzzle.append('_ ')
            elif self.sportsButton.isChecked():
                number = random.randint(0,5)
                solution = sports[number]
                for i in solution:
                    if i == ' ':
                        puzzle.append('  ')
                    else:
                        puzzle.append('_ ')
            elif self.horrorButton.isChecked():
                number = random.randint(0,5)
                solution = horror[number]
                for i in solution:
                    if i == ' ':
                        puzzle.append('  ')
                    else:
                        puzzle.append('_ ')
            self.hangManGraphic.setText("")
            self.textEdit.show()
            self.vgButton.hide()
            self.horrorButton.hide()
            self.presidentsButton.hide()
            self.sportsButton.hide()
            count += 1
            dummy = ' '
            for x in puzzle:
                dummy = dummy + x
            self.solution.setText(dummy)
        else:
            if chances > 0 and '_ ' in puzzle:
                guess = self.textEdit.text()
                guess = guess.upper()
                if guess in usedLetters:
                    self.textEdit.setText("used letter")
                elif guess in solution:
                    for z in range(len(puzzle)):
                        if guess == solution[z]:
                            puzzle[z] = guess + ' '
                    dummy = ' '
                    for x in puzzle:
                        dummy = dummy + x
                    self.solution.setText(dummy)
                    usedLetters.append(guess)
                else:
                    chances -= 1
                    usedLetters.append(guess)
                    if chances == 5:
                        self.hangManGraphic.setText("<html><head/><body><p><span style=\" font-size:36pt;\"> O</span></p></body></html>")
                    if chances == 4:
                        self.hangManGraphic.setText("<html><head/><body><p><span style=\" font-size:36pt;\"> O</span></p><p><span style=\" font-size:36pt;\">|</span></p></body></html>")
                    if chances == 3:
                        self.hangManGraphic.setText("<html><head/><body><p><span style=\" font-size:36pt;\"> O</span></p><p><span style=\" font-size:36pt;\">/|</span></p></body></html>")
                    if chances == 2:
                        self.hangManGraphic.setText("<html><head/><body><p><span style=\" font-size:36pt;\"> O</span></p><p><span style=\" font-size:36pt;\">/|\\</span></p></body></html>")
                    if chances == 1:
                        self.hangManGraphic.setText("<html><head/><body><p><span style=\" font-size:36pt;\"> O</span></p><p><span style=\" font-size:36pt;\">/|\\</span></p><p><span style=\" font-size:36pt;\">/</span></p></body></html>")
                    if chances == 0:
                        self.hangManGraphic.setText("<html><head/><body><p><span style=\" font-size:36pt;\"> O</span></p><p><span style=\" font-size:36pt;\">/|\\</span></p><p><span style=\" font-size:36pt;\">/ \\</span></p></body></html>")
            else:
                if '_ ' not in puzzle:
                    self.hangManGraphic.setText("You Win!")
                    count += 1
                    puzzle = []
                    chances = 6
                    self.textEdit.hide()
                    self.vgButton.show()
                    self.horrorButton.show()
                    self.presidentsButton.show()
                    self.sportsButton.show()
                    self.solution.setText('')
                else:
                    self.hangManGraphic.setText("You Lose!")
                    count += 1
                    puzzle = []
                    chances = 6
                    self.textEdit.hide()
                    self.vgButton.show()
                    self.horrorButton.show()
                    self.presidentsButton.show()
                    self.sportsButton.show()
                    self.solution.setText('')
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
