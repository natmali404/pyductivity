# pyDuctivity
## a Python-based productivity tool


pyDuctivity is a simple, GUI-based software that aids you in basic productivity-related tasks. It is still in the early development stage, as it is a coursework project for the "Scripting Languages" course, aimed at demonstrating proficiency in Python programming and GUI application development. It serves as a practical application of skills learned throughout the course, showcasing the ability to create functional software that meets specific project requirements.


## Tech
pyDuctivity was created in Python 3.12.2 with the help of [PySide6] for GUI support.


## Features


- widget-based, user-friendly interface - add, remove, reorder widgets as you wish
- customization features - display your name on the dashboard, change color motives!
- data saving - your widgets are saved in a JSON format and loaded on app launch


## Currently supported widgets:
- pomodoro - customizable timer aiding in managing your work and rest time durations
- notes - capture your thoughts on the go, never miss a memo
- checklist - stay organized and keep track of your tasks with ease
- website blocker - stay productive by blocking off distracting websites with just a click of a button
- quotes - add your own motivational quotes and change them whenever you want


## Requirements
The project is currently uncompiled. To run it, please make sure you have installed the following components:
- Python 3.12.2
- PySide6

**IMPORTANT: Please make sure you have administrator priviledges to run the software. Otherwise, the website blocker feature is not going to work.**


## Starting the app
To start the app, make sure you have PySide6 installed, either globally or in your virtual environment:
```sh
pip install pyside6
```
Then you can run the following commands in the command line - nagivate to the project directory and start the main.py script:
```sh
cd project_directory
python main.py
```
Remember to allow admin priviledges to use the website blocker.


## Deleting data, restarting the configuration
To remove existing data and start over, navigate to the 'userdata' folder and remove the two JSON data files, then remove the contents of the 'widget_data' folder.


## Screenshots of the app

![App launch](https://github.com/404nat/pyductivity/assets/58657829/2a57487e-65c9-49b9-b8aa-00ada33b6369)
![Adding a widget](https://github.com/404nat/pyductivity/assets/58657829/5dea3238-6de6-49d5-9a99-a45b510c613e)
![App interface](https://github.com/404nat/pyductivity/assets/58657829/455baa82-045e-4afc-8a50-e42daa876d0e)
![App experience](https://github.com/404nat/pyductivity/assets/58657829/06297ecc-f485-4ce2-b4af-165597664de1)


## Future development
More widgets and functionalities are being planned!


[PySide6]: <https://pypi.org/project/PySide6/>


