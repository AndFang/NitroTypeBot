# NitroTypeBot
A python script built using tkinter and customtkinter, selenium, and keyboard to play [Nitro Type](https://www.nitrotype.com/race) utilizing a typing bot which can type at various speeds.

## Background
What started as some Friday shenanigans quickly turn into some friendly competitiveness of seeing how fast one can type. What started out as quickly typing the alphabet on [Speed Typing Online](https://www.speedtypingonline.com/games/type-the-alphabet.php) was brought into the context of Nitro Type. From there the additions and features grew. Eventually this turned into a GUI which allowed one to log in and also control the speed at which they typed. 

## How to Use

### Getting Started
- Clone the repository or just copy 'nitrotypebot.py' and install the necessary packages by running the following command in your terminal:
    - Future versions will include a singular executable file that can be run on any computer.
```
pip install -r requirements.txt
```

### GUI
- Run the script by running the following command in your terminal:
```
python nitrotypebot.py
```
- The GUI should pop up. If it doesn't, make sure you have tkinter installed.
![GUI of application](/gui.jpg)
- Enter your username and password for Nitro Type.
    - If both fields are not filled in, the bot will play nitro type as a guest.
- Select if you want the bot to automatically go to the next race once the current one is finished.
- Select the speed at which you want to type.
    - The default speed is ~100 WPM.
    - The delays result in the following speeds
        - 0 = ~200 WPM
            - Will likely result in your account being banned.
        - 0.01 = ~150 WPM
        - 0.1 = ~100 WPM
        - 0.5 = ~50 WPM
        - 1 = ~15 WPM
- Click 'Start' to begin the bot.
- While the bot is running, you can click 'Stop' to stop the bot or you can change the speed of the bot using the slider.

### Bugs
- The bot may stop after a set amount of races. If this happens, click stop and redo the steps above. Future versions will improve the fluidity of the bot.
- The bot also occasionally makes mistakes to counter bot checkers. Future versions will allows you to change how often mistakes are made.
## Acknowledgements
- Abhiram who suggested bringing this into the context of Nitro Type.
- Tyler who introduced Nitro Type and asked to play these typing games. Check out his own typing bot at [repo](https://github.com/tylernh10)!

## Future Plans
- Create a singular executable file that can be run on any computer.
- More options for the user to control (e.g. nitro, accuracy, etc.).
- Improve fluidity of the GUI.
- Error checking for creditials of input.
