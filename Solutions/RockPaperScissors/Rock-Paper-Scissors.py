# Added by Joe Roybal
# See full project at: https://github.com/JoeRoybal/Rock-Paper-Scissors-Game
# Have fun!

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QTimer
from random import randint

textFont = QFont("Times", 14)
rollFont = QFont("Arial", 24)
buttonFont = QFont("Arial", 12)
computerScore = 0
playerScore = 0


class Window (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock Paper Scissors Game")
        self.setGeometry(1000, 150, 550, 500)
        self.UI()

    def UI(self):
        ##################### SCORES #####################
        self.scoreComputerText = QLabel(
            "Computer Score : {}".format(computerScore), self)
        self.scoreComputerText.move(30, 20)
        self.scoreComputerText.setFont(textFont)
        self.scorePlayerText = QLabel(
            "Player Score : {}".format(playerScore), self)
        self.scorePlayerText.move(330, 20)
        self.scorePlayerText.setFont(textFont)

        ##################### Roll ######################
        self.imageComputer = QLabel("ROCK          ", self)
        self.imageComputer.move(50, 100)
        self.imageComputer.setFont(rollFont)
        self.imagePlayer = QLabel("ROCK           ", self)
        self.imagePlayer.move(330, 100)
        self.imagePlayer.setFont(rollFont)

        #################### Buttons ####################
        btnStart = QPushButton("Start", self)
        btnStart.setFont(buttonFont)
        btnStart.move(180, 250)
        btnStart.clicked.connect(self.start)
        btnStop = QPushButton("Stop", self)
        btnStop.setFont(buttonFont)
        btnStop.clicked.connect(self.stop)
        btnStop.move(270, 250)

        #################### Timer ######################
        self.timer = QTimer(self)
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.playGame)

        self.show()

    def playGame(self):
        self.rndComputer = randint(1, 3)
        if self.rndComputer == 1:
            self.imageComputer.setText("ROCK")
        elif self.rndComputer == 2:
            self.imageComputer.setText("PAPER")
        else:
            self.imageComputer.setText("SCISSORS")

        self.rndPlayer = randint(1, 3)
        if self.rndPlayer == 1:
            self.imagePlayer.setText("ROCK")
        elif self.rndPlayer == 2:
            self.imagePlayer.setText("PAPER")
        else:
            self.imagePlayer.setText("SCISSORS")

    def start(self):
        self.timer.start()

    def stop(self):
        global computerScore
        global playerScore
        self.timer.stop()
        ### TIE ###
        if self.rndComputer == self.rndPlayer:
            mbox = QMessageBox.information(self, "Results", "Draw Game")
        ### PLAYER WINS ###
        elif self.rndComputer == 1 and self.rndPlayer == 2:
            mbox = QMessageBox.information(self, "Results", "You Win")
            playerScore += 1
            self.scorePlayerText.setText(
                "Player Score : {}".format(playerScore))
        elif self.rndComputer == 2 and self.rndPlayer == 3:
            mbox = QMessageBox.information(self, "Results", "You Win")
            playerScore += 1
            self.scorePlayerText.setText(
                "Player Score : {}".format(playerScore))
        elif self.rndComputer == 3 and self.rndPlayer == 1:
            mbox = QMessageBox.information(self, "Results", "You Win")
            playerScore += 1
            self.scorePlayerText.setText(
                "Player Score : {}".format(playerScore))
        ### COMPUTER WINS ###
        elif self.rndComputer == 2 and self.rndPlayer == 1:
            mbox = QMessageBox.information(self, "Results", "Computer Wins")
            computerScore += 1
            self.scoreComputerText.setText(
                "Computer Score : {}".format(computerScore))
        elif self.rndComputer == 3 and self.rndPlayer == 2:
            mbox = QMessageBox.information(self, "Results", "Computer Wins")
            computerScore += 1
            self.scoreComputerText.setText(
                "Computer Score : {}".format(computerScore))
        elif self.rndComputer == 1 and self.rndPlayer == 3:
            mbox = QMessageBox.information(self, "Results", "Computer Wins")
            computerScore += 1
            self.scoreComputerText.setText(
                "Computer Score : {}".format(computerScore))

        if computerScore == 3:
            mbox = QMessageBox.information(self, "GAMEOVER", "Computer Wins")
            sys.exit()
        if playerScore == 3:
            mbox = QMessageBox.information(self, "GAMEOVER", "Computer Wins")
            sys.exit()


def main():
    App = QApplication(sys.argv)
    window = Window()
    window.start()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
