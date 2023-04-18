
# Interface 
- Light theme (to change theme tap to moon icon)
![Pomodoro Light theme](/img/Light_theme.png)
- Dark theme (to change theme tap to sun icon)
![Pomodoro Dark theme](/img/Dark_theme.png)
- Special Pomodoro theme (to change theme tap to Pomodoro icon)
![Pomodoro theme](/img/Pomodoro_theme.png)

After the Pomodoro, a sound plays at the end that successfully indicates that the time is up.



 # Usage
  
  ```bash
  IF YOU DON'T HAVE FFMPEG PLEASE INSTALL IT FIRSTLY
  - pip install -r requirements.txt
  - Run main.py file.
  ```` 
  
If you want to change the timer, change the number 25 to any other, the main point 25 is minutes, which means that the number that you insert there will already be in minutes!
  
```python
min_25 = 60 * 25  # 25 minutes 
```
In the same way you can change the minutes of break time.

```python
min_5 = 60 * 5 # 5 minutes break 
min_10 = 60 * 10 # 10 minutes break
min_15 = 60 * 15 # 15 minutes break
```

# If you don't have ffmpeg or you don't need the sound delete that lines of code
```python
        self.sound_signal = []

        self.break_down_song = AudioSegment.from_file("audio/pomodoro_end.mp3")
        
        for i in self.sound_signal:
            print(i)
            if i == True:
                play(self.break_down_song)
            elif i == False:
                pass
 
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
        
        self.sound_on_button.raise_()
        self.sound_off_button.raise_()
        
        # Sound on button visible status off
        self.sound_on_button.setVisible(False)
        # Sound on button set Disabled
        self.sound_on_button.setDisabled(True)
        
        self.sound_on_button.clicked.connect(self.hide_sound_on_button)
        self.sound_off_button.clicked.connect(self.hide_sound_off_button)
        
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
        # Addtional settings from hide_sound_on_button function
        self.thread.sound_signal.append(1)

        self.sound_on_button.setVisible(True)
        self.sound_on_button.setDisabled(False)

        self.sound_off_button.setVisible(False)
        self.sound_off_button.setDisabled(True)
```
