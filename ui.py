import sys

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QPushButton, QLabel, QVBoxLayout, QHBoxLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('TICTACTOE')
        self.setFixedSize(300,400)
        self.setStyleSheet('background: lightblue;')
        
        self.btns = list()
        self.turn = 0
        self.turn_count = 0

        for _ in range(3):
            row = list()
            for _ in range(3):
                row.append(QPushButton(self))
            self.btns.append(row)

        for i in range(3):
            for j in range(3):
                self.btns[i][j].setGeometry(90*i+20, 90*j+20, 80, 80)
                self.btns[i][j].clicked.connect(self.on_click)

        self.info_label = QLabel('Turn X', self)
        self.info_label.setStyleSheet('font-size: 50px')
        self.info_label.setGeometry(85,300,270,90)

    def on_click(self):
        self.turn_count += 1    

        btn = self.sender()
        btn.setEnabled(False)

        if self.turn == 0:
            btn.setStyleSheet('color: blue; font-size: 50px;')

            btn.setText("X")
            self.turn = 1
            self.info_label.setText('Turn O')
        else:
            btn.setStyleSheet('color: red ; font-size: 50px')
            btn.setText("O")
            self.turn = 0
            self.info_label.setText('Turn X') 

        winner = self.check_win()

        if winner:
            if self.turn == 0:
                self.info_label.setText('Win O') 
                self.exit = ExitWin('Win O', self)
                self.exit.show()
            else:
                self.info_label.setText('Win X') 
                self.exit = ExitWin('Win X', self)
                self.exit.show()
            self.closeBtn()

        elif self.turn_count == 9:
            self.info_label.setText('Draw') 
            self.exit = ExitWin('Draw', self)
            self.exit.show()
            self.closeBtn()

    
    def closeBtn(self):
        for i in range(3):
            for j in range(3):
                self.btns[i][j].setEnabled(False)
# githubdan ozgartirdim

    def check_win(self):
        
        for i in range(3):
            if self.btns[i][0].text() == self.btns[i][1].text() and self.btns[i][0].text() == self.btns[i][2].text() and self.btns[i][0].text() != '':
                return True

        for i in range(3):
            if self.btns[0][i].text() == self.btns[1][i].text() and self.btns[0][i].text() == self.btns[2][i].text() and self.btns[0][i].text() != '':
                return True
        
        if self.btns[0][0].text() == self.btns[1][1].text() and self.btns[0][0].text() == self.btns[2][2].text() and self.btns[0][0].text() != '':
                return True

        if self.btns[0][2].text() == self.btns[1][1].text() and self.btns[0][2].text() == self.btns[2][0].text() and self.btns[0][2].text() != '':
                return True

        return False

class ExitWin(QWidget):
    def __init__(self, text, win) -> None:
        super().__init__()
        self.win = win
        self.setFixedSize(200,100)
        self.v_box = QVBoxLayout()
        self.h_box = QHBoxLayout()

        self.info_label = QLabel(text)

        self.v_box.addWidget(self.info_label)

        self.new_game_btn = QPushButton('New game')
        self.exit_btn = QPushButton('Exit')

        self.h_box.addWidget(self.new_game_btn)
        self.h_box.addWidget(self.exit_btn)

        self.new_game_btn.clicked.connect(self.newGame)
        self.exit_btn.clicked.connect(self.exit1)

        self.v_box.addLayout(self.h_box)

        self.setLayout(self.v_box)

    def exit1(self):
        self.win.close()
        self.close()

    def newGame(self):
        self.exit1()
        self.win = Window()
        self.win.show()
    

app = QApplication([])
win = Window()
win.show()
sys.exit(app.exec_())

# push qil
