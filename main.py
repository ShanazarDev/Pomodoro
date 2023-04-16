from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from pydub import AudioSegment
from pydub.playback import play
import sys
import time


# If you have "TSCu_Comic" font on your PC. PLease rename font "Times New Roman" to "TSCu_Comic" for more cute application

class Threading(QtCore.QThread):

    def __init__(self, window, parent=None):
        super().__init__(parent)
        self.counts = 0
        self.WINDOW = window
        self.min_5_count = [] 
        self.min_10_count = []
        self.min_15_count = []
        self.sound_signal = []
        self.pomodoro_count = []
        self.break_down_song = AudioSegment.from_file("audio/pomodoro_end.mp3")

    # Countdown timer runner function
    def run(self):
        self.WINDOW.start_time.setDisabled(True)
        min_25 = 60 * 25  # 25 minutes
        while min_25 > 0:
            min_25 -= 1
            self.minutes, self.seconds = divmod(min_25, 60)
            self.WINDOW.countdown_timer.setText(
                f'{self.minutes:02d}:{self.seconds:02d}')
            time.sleep(1)

        for i in self.sound_signal:
            print(i)
            if i == True:
                play(self.break_down_song)
            elif i == False:
                pass

        if self.min_5_count:
            for i in self.min_5_count:
                if i == 5:
                    print('start_5min')
                    min_5 = 60 * 5
                    while min_5 > 0:
                        min_5 -= 1
                        self.minutes, self.seconds = divmod(min_5, 60)
                        self.WINDOW.countdown_timer.setText(
                            f'{self.minutes:02d}:{self.seconds:02d}')
                        time.sleep(1)
                    self.WINDOW.min_5.setDisabled(False)
                    self.WINDOW.min_10.setDisabled(False)
                    self.WINDOW.min_15.setDisabled(False)

        elif self.min_10_count:
            for i in self.min_10_count:
                if i == 10:
                    print('start_10min')
                    min_10 = 60 * 10
                    while min_10 > 0:
                        min_10 -= 1
                        self.minutes, self.seconds = divmod(min_10, 60)
                        self.WINDOW.countdown_timer.setText(
                            f'{self.minutes:02d}:{self.seconds:02d}')
                        time.sleep(1)
                    self.WINDOW.min_5.setDisabled(False)
                    self.WINDOW.min_10.setDisabled(False)
                    self.WINDOW.min_15.setDisabled(False)

        else:
            for i in self.min_15_count:
                if i == 15:
                    print("start_15min")
                    min_15 = 60 * 15
                    while min_15 > 0:
                        self.minutes, self.seconds = divmod(min_15, 60)
                        self.WINDOW.countdown_timer.setText(
                            f'{self.minutes:02d}:{self.seconds:02d}')
                        time.sleep(1)
                    self.WINDOW.min_5.setDisabled(False)
                    self.WINDOW.min_10.setDisabled(False)
                    self.WINDOW.min_15.setDisabled(False)

        self.counts += 1

        self.pomodoro_count.append(self.counts)

        self.WINDOW.start_time.setDisabled(False)

        for i in self.pomodoro_count:
            if i > 0:
                self.WINDOW.pomodors.setVisible(True)
                self.WINDOW.pomodors.setText(f"Pomodors: {i}")
            else:
                self.WINDOW.pomodors.setVisible(False)

# Ui class
class Ui_MainWindow(object):

    # Ui setup function
    def setupUi(self, MainWindow):
        # Main Window and window size
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)

        # Size policy are fixed to more visibility
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())

        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(
            640, 480))      # Maximum Window size
        MainWindow.setMaximumSize(QtCore.QSize(
            640, 480))      # Minimum Window size

        # To centring all elements
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        # Fonts
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        font.setPointSize(20)
        font.setFamily("Times New Roman")

        # Shadow effect for Pomodoro label
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)

        # Pomodoro title
        self.topText = QtWidgets.QLabel(self.centralwidget)
        self.topText.setGeometry(QtCore.QRect(100, 20, 450, 50))
        self.topText.setFont(font)
        self.topText.setTextFormat(QtCore.Qt.RichText)
        self.topText.setAlignment(QtCore.Qt.AlignCenter)
        self.topText.setObjectName("topText")
        self.topText.setGraphicsEffect(shadow)
        self.topText.setStyleSheet("""
                                        QLabel
                                        {
                                            color: black;
                                            border-radius: 20px;
                                        }
                                    """)

        # Fonts
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(30)
        font.setFamily("Times New Roman")

        # Shadow effect for countdown timer
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)

        # Main countdown timer
        self.countdown_timer = QtWidgets.QLabel(self.centralwidget)
        self.countdown_timer.setGeometry(QtCore.QRect(220, 85, 200, 200))
        self.countdown_timer.setFont(font)
        self.countdown_timer.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.countdown_timer.setObjectName("countdown_timer")
        self.countdown_timer.setAlignment(QtCore.Qt.AlignCenter)
        self.countdown_timer.setGraphicsEffect(shadow)
        self.countdown_timer.setStyleSheet("""
                                                QLabel
                                                {
                                                    color: black;
                                                    border: 1px solid black;
                                                    border-radius: 100px; 
                                                }
                                            """)

        # All buttons are connected to there style
        self.styleButtons = """
                                QPushButton
                                {
                                    background-color: white;
                                    border: 1px solid black;
                                    border-radius: 15px;
                                    font-family: Times New Roman;
                                }
                                QPushButton:hover
                                {  
                                    background-color: #82E0AA;
                                }
                                QPushButton:focus
                                {
                                    background-color: #F4D03F;
                                }
                            """

        # Fonts for label
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)

        # Break time info label
        self.break_time = QtWidgets.QLabel(self.centralwidget)
        self.break_time.setGeometry(QtCore.QRect(200, 320, 250, 20))
        self.break_time.setFont(font)
        self.break_time.setAlignment(QtCore.Qt.AlignCenter)
        self.break_time.setObjectName("break_time")

        # Start Pomodoro button
        self.start_time = QtWidgets.QPushButton(self.centralwidget)
        self.start_time.setGeometry(QtCore.QRect(276, 410, 90, 50))
        self.start_time.setObjectName("start_time")
        self.start_time.setStyleSheet("""
                                        QPushButton
                                        {
                                            border-radius: 17px;
                                            font-family: Times New Roman;
                                            border: 1px solid black;
                                        }
                                        QPushButton:hover
                                        {
                                            background-color: yellow;
                                        }
                                        """)
        self.start_time.setIcon(QtGui.QIcon("img/play.png"))        # Start ico

        # Pomodors counter label
        self.pomodors = QLabel(self.centralwidget)
        self.pomodors.setGeometry(QtCore.QRect(283, 388, 210, 20))
        self.pomodors.setObjectName("pomodors")
        self.pomodors.setStyleSheet("""
                                            QLabel
                                            {
                                                font-family: Times New Roman;
                                            }
                                            """)

        # 5 minutes break buttons
        self.min_5 = QtWidgets.QPushButton(self.centralwidget)
        self.min_5.setGeometry(QtCore.QRect(180, 350, 80, 30))
        self.min_5.setObjectName("min_5")
        self.min_5.setStyleSheet(self.styleButtons)

        # 10 minutes break button
        self.min_10 = QtWidgets.QPushButton(self.centralwidget)
        self.min_10.setGeometry(QtCore.QRect(280, 350, 80, 30))
        self.min_10.setObjectName("min_10")
        self.min_10.setStyleSheet(self.styleButtons)

        # 15 minutes break buttton
        self.min_15 = QtWidgets.QPushButton(self.centralwidget)
        self.min_15.setGeometry(QtCore.QRect(380, 350, 80, 30))
        self.min_15.setObjectName("min_15")
        self.min_15.setStyleSheet(self.styleButtons)

        # Light theme button
        # Light theme ico
        ico = QtGui.QIcon("img/sun.png")
        self.light_theme = QtWidgets.QPushButton(self.centralwidget)
        self.light_theme.setGeometry(QtCore.QRect(40, 414, 40, 40))
        self.light_theme.setObjectName("light_theme")
        self.light_theme.setStyleSheet("border-radius: 20px;")
        self.light_theme.setIcon(ico)
        self.light_theme.setIconSize(QtCore.QSize(40, 40))

        # Dark theme button
        # Dark theme ico
        ico = QtGui.QIcon("img/half-moon.png")
        self.dark_theme = QtWidgets.QPushButton(self.centralwidget)
        self.dark_theme.setGeometry(QtCore.QRect(40, 414, 40, 40))
        self.dark_theme.setObjectName("dark_theme")
        self.dark_theme.setStyleSheet("border-radius: 20px;")
        self.dark_theme.setIcon(ico)
        self.dark_theme.setIconSize(QtCore.QSize(40, 40))

        # Pomodoro theme button
        # Pomodoro theme ico
        ico = QtGui.QIcon("img/tomato.png")
        self.pomodoro_theme = QtWidgets.QPushButton(self.centralwidget)
        self.pomodoro_theme.setGeometry(QtCore.QRect(91, 413, 40, 40))
        self.pomodoro_theme.setObjectName("pomodoro_theme")
        self.pomodoro_theme.setStyleSheet("border-radius: 20px;")
        self.pomodoro_theme.setIcon(ico)
        self.pomodoro_theme.setIconSize(QtCore.QSize(40, 40))

        # Close button
        self.colse_button = QtWidgets.QPushButton(self.centralwidget)
        self.colse_button.setGeometry(QtCore.QRect(520, 420, 80, 30))
        self.colse_button.setObjectName("close_button")
        self.colse_button.setStyleSheet("""
                                        QPushButton
                                        {
                                            background-color: #adadff;
                                            border: 1px solid black;
                                            font-family: Times New Roman;
                                            border-radius: 15px;
                                        }
                                        QPushButton:hover
                                        {
                                            background-color: #C0392B;
                                            border: 1px solid white;
                                        }
                                        """)

        # Sound on button
        ico = QtGui.QIcon("img/sound_on.png")                   # Sound on ico
        self.sound_on_button = QPushButton(self.centralwidget)
        self.sound_on_button.setGeometry(138, 417, 40, 40)
        self.sound_on_button.setObjectName("sound_on_button")
        self.sound_on_button.setStyleSheet("border-radius: 20px;")
        self.sound_on_button.setIcon(ico)
        self.sound_on_button.setIconSize(QtCore.QSize(40, 40))

        # Sound off button
        ico = QtGui.QIcon("img/sound_off.png")                  # Sound off ico
        self.sound_off_button = QPushButton(self.centralwidget)
        self.sound_off_button.setGeometry(137, 417, 40, 40)
        self.sound_off_button.setObjectName("sound_off_button")
        self.sound_off_button.setStyleSheet("border-radius: 20px;")
        self.sound_off_button.setIcon(ico)
        self.sound_off_button.setIconSize(QtCore.QSize(40, 40))

        # Background
        self.background = QtWidgets.QGraphicsView(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, -6, 645, 491))
        self.background.setObjectName("background")
        self.background.setStyleSheet(f"background-color: #f4f4f8;")

        # Raise all elements for backgorund
        self.background.raise_()
        self.min_5.raise_()
        self.min_10.raise_()
        self.min_15.raise_()
        self.topText.raise_()
        self.pomodors.raise_()
        self.break_time.raise_()
        self.start_time.raise_()
        self.dark_theme.raise_()
        self.pomodoro_theme.raise_()
        self.light_theme.raise_()
        self.colse_button.raise_()
        self.countdown_timer.raise_()
        self.sound_on_button.raise_()
        self.sound_off_button.raise_()

        # Sound on button visible status off
        self.sound_on_button.setVisible(False)
        # Sound on button set Disabled
        self.sound_on_button.setDisabled(True)
        # Dark theme Button visible status off
        self.dark_theme.setVisible(False)
        # Dark theme button set Disabled
        self.dark_theme.setDisabled(True)

        # Buttons with signals to function
        self.dark_theme.clicked.connect(self.dark)
        self.pomodoro_theme.clicked.connect(self.pomodoro)
        self.light_theme.clicked.connect(self.light)
        self.colse_button.clicked.connect(self.closeApp)
        self.min_5.clicked.connect(self.disable_minutes_10_15)
        self.min_10.clicked.connect(self.disable_minutes_5_15)
        self.min_15.clicked.connect(self.disable_minutes_5_10)
        self.start_time.clicked.connect(self.startFunction_Thread)
        self.sound_on_button.clicked.connect(self.hide_sound_on_button)
        self.sound_off_button.clicked.connect(self.hide_sound_off_button)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Threading for countdown timer without it ui are freeze
        # Window take one argument it is Self argument for get access to ui components
        self.thread = Threading(window=self)

    # Function to start countdown timer when start button have signal from user
    def startFunction_Thread(self):
        self.thread.start()

    # Hide Sound on button when sound on mode selected
    def hide_sound_on_button(self):
        # From Threading class to sound_signal list append 1 to activate mode
        self.thread.sound_signal.append(0)

        self.sound_on_button.setVisible(False)
        self.sound_on_button.setDisabled(True)

        # To set visible status sound_off_button
        self.sound_off_button.setVisible(True)
        # To set off disabled status sound_off_button
        self.sound_off_button.setDisabled(False)

    # Hide Sound off button when sound off mode selected
    def hide_sound_off_button(self):
        # Additional settings from hide_sound_on_button function
        self.thread.sound_signal.append(1)

        self.sound_on_button.setVisible(True)
        self.sound_on_button.setDisabled(False)

        self.sound_off_button.setVisible(False)
        self.sound_off_button.setDisabled(True)

    # Disable 10 and 15 minutes when selected 5 minutes break time
    def disable_minutes_10_15(self):
        self.break_time.setText("Selected 5 minutes relax")
        # Append to min_5 list 5 to activate 5 minutes break time
        self.thread.min_5_count.append(5)
        self.min_5.setDisabled(True)
        self.min_10.setDisabled(True)
        self.min_15.setDisabled(True)
        print(self.thread.min_5_count)

    # Disable 5 and 15 minutes when selected 10 minutes break time
    def disable_minutes_5_15(self):
        self.break_time.setText("Selected 10 minutes relax")
        # Append to min_10 list 10 to activate 10 minutes break time
        self.thread.min_10_count.append(10)
        self.min_5.setDisabled(True)
        self.min_10.setDisabled(True)
        self.min_15.setDisabled(True)
        print(self.thread.min_10_count)
    # Disable 5 and 10 minutes when selected 15 minutes break time

    def disable_minutes_5_10(self):
        self.break_time.setText("Selected 15 minutes relax")
        # Append to min_15 list 15 to activate 15 minutes break time
        self.thread.min_15_count.append(15)
        self.min_5.setDisabled(True)
        self.min_10.setDisabled(True)
        self.min_15.setDisabled(True)
        print(self.thread.min_15_count)

    # Dark theme function
    def dark(self):
        self.light_theme.setVisible(True)
        self.light_theme.setDisabled(False)
        self.dark_theme.setVisible(False)
        self.dark_theme.setDisabled(True)
        self.background.setStyleSheet("background-color: #1B2631;")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(30)
        shadow.setColor(QtCore.Qt.gray)
        self.countdown_timer.setGraphicsEffect(shadow)

        self.countdown_timer.setStyleSheet("""
                                            QLabel
                                            {
                                                background-color: rgba(211, 218, 226, 10);
                                                color: #fffff1;
                                                border: 2px solid #000000;
                                                border-radius: 100px;
                                            }
                                            """)
        self.topText.setStyleSheet("""
                                    QLabel
                                    {
                                        color: #AEB6BF;
                                        border-radius: 20px;
                                    }
                                    """)
        self.break_time.setStyleSheet("""
                                        QLabel
                                        {
                                            color: #AEB6BF;
                                        }
                                    """)
        self.styleButtons = """
                            QPushButton
                            {
                                background-color: #1B2631;
                                color: #AEB6BF;
                                border: 2px solid #ABB2B9;
                                border-radius: 15px;
                                font-family: Times New Roman;
                            }
                            QPushButton:hover
                            {  
                                background-color: #82E0AA;
                                color: black;
                            }
                            QPushButton:focus
                            {
                                background-color: #F4D03F;
                                color: black;
                            }
                            """
        self.pomodors.setStyleSheet("""
                                                QLabel
                                                {
                                                    color: #AEB6BF;
                                                    font-family: Times New Roman;
                                                }
                                            """)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(30)
        shadow.setColor(QtCore.Qt.gray)
        self.topText.setGraphicsEffect(shadow)
        shadow_3 = QGraphicsDropShadowEffect()
        shadow_3.setBlurRadius(25)
        shadow_3.setColor(QtCore.Qt.gray)
        self.break_time.setGraphicsEffect(shadow_3)
        self.start_time.setStyleSheet(self.styleButtons)
        self.min_5.setStyleSheet(self.styleButtons)
        self.min_10.setStyleSheet(self.styleButtons)
        self.min_15.setStyleSheet(self.styleButtons)

    # Light theme function
    def light(self):
        self.light_theme.setVisible(False)
        self.light_theme.setDisabled(True)
        self.dark_theme.setVisible(True)
        self.dark_theme.setDisabled(False)

        self.background.setStyleSheet(f"background-color: #f4f4f8;")
        shadow_1 = QGraphicsDropShadowEffect()
        shadow_1.setBlurRadius(25)
        self.countdown_timer.setGraphicsEffect(shadow_1)

        shadow_2 = QGraphicsDropShadowEffect()
        shadow_2.setBlurRadius(25)
        self.topText.setGraphicsEffect(shadow_2)

        self.countdown_timer.setStyleSheet("""
                                                QLabel
                                                {
                                                    background-color: rgba(48, 48, 48, 15);
                                                    color: black;
                                                    border: 3px solid black;
                                                    border-radius: 100px;
                                                }
                                            """)
        self.topText.setStyleSheet("""
                                        QLabel
                                        {
                                            color: black;
                                            border-radius: 20px;
                                        }
                                    """)
        self.styleButtons = """
                            QPushButton
                            {
                                background-color: rgba(64, 71, 69, 20);
                                border: 1px solid black;
                                border-radius: 15px;
                                font-family: Times New Roman;
                            }
                            QPushButton:hover{  
                                background-color: #82E0AA;
                            }
                            QPushButton:focus{
                                background-color: #F4D03F;
                            }
                            """
        self.pomodors.setStyleSheet("""
                                        QLabel
                                        {
                                            color: black;
                                            font-family: Times New Roman;
                                        }
                                    """)
        self.break_time.setStyleSheet('color: black;')
        shadow_3 = QGraphicsDropShadowEffect()
        shadow_3.setBlurRadius(25)
        shadow_3.setColor(QtCore.Qt.black)
        self.break_time.setGraphicsEffect(shadow_3)
        self.start_time.setStyleSheet(self.styleButtons)
        self.min_5.setStyleSheet(self.styleButtons)
        self.min_10.setStyleSheet(self.styleButtons)
        self.min_15.setStyleSheet(self.styleButtons)

    # Special Pomodoro theme
    def pomodoro(self):
        self.background.setStyleSheet(f"background-color: #5A002C;")
        shadow_1 = QGraphicsDropShadowEffect()
        shadow_1.setBlurRadius(18)
        shadow_1.setColor(QtCore.Qt.black)
        self.countdown_timer.setGraphicsEffect(shadow_1)

        shadow_2 = QGraphicsDropShadowEffect()
        shadow_2.setBlurRadius(25)
        shadow_2.setColor(QtCore.Qt.green)
        self.topText.setGraphicsEffect(shadow_2)

        self.countdown_timer.setStyleSheet("""
                                                QLabel
                                                {
                                                    background-color: rgba(10, 243, 95, 15);
                                                    color: #6DC809;
                                                    border: 3px solid #00A300;
                                                    border-radius: 100px;
                                                }
                                            """)
        self.topText.setStyleSheet("""
                                        QLabel
                                        {
                                            color: black;
                                            border-radius: 20px;
                                        }
                                    """)
        self.styleButtons = """
                            QPushButton
                            {
                                background-color: #5A002C;
                                border: 1px solid black;
                                border-radius: 15px;
                                font-family: Times New Roman;
                            }
                            QPushButton:hover{  
                                background-color: #82E0AA;
                            }
                            QPushButton:focus{
                                background-color: #F4D03F;
                            }
                            """
        self.pomodors.setStyleSheet("""
                                        QLabel
                                        {
                                            color: black;
                                            font-family: Times New Roman;
                                        }
                                    """)
        shadow_3 = QGraphicsDropShadowEffect()
        shadow_3.setBlurRadius(25)
        shadow_3.setColor(QtCore.Qt.green)
        self.break_time.setStyleSheet('color: black;')
        self.break_time.setGraphicsEffect(shadow_3)
        self.start_time.setStyleSheet(self.styleButtons)
        self.min_5.setStyleSheet(self.styleButtons)
        self.min_10.setStyleSheet(self.styleButtons)
        self.min_15.setStyleSheet(self.styleButtons)

    # Function to close app
    def closeApp(self):
        sys.exit()

    # Translator to promote all labels text
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Pomodoro timer - by ShanazarDev   v1.1"))
        MainWindow.setWindowIcon(QtGui.QIcon("img/tomato.png"))
        self.topText.setText(_translate("MainWindow", "Pomodoro timer"))
        self.countdown_timer.setText(_translate("MainWindow", "25:00"))
        self.break_time.setText(_translate("MainWindow", "Select break time:"))
        self.start_time.setText(_translate("MainWindow", "Start"))
        self.min_5.setText(_translate("MainWindow", "5 min"))
        self.min_10.setText(_translate("MainWindow", "10 min"))
        self.min_15.setText(_translate("MainWindow", "15 min"))
        self.colse_button.setText(_translate("MainWindow", "Exit"))


# Run point
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.light()              # For activate light theme previously
    MainWindow.show()
    sys.exit(app.exec_())
