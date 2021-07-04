# Skaehub-Project
YOUTUBE RINGER ALARM CLOCK

Problem Definition
The main aim of this project is to create a command line application that takes user input of the YouTube songs links they would like, input the time (alarm) and once the countdown is done the application randomly selects from the user input links and prompts a YouTube browser where the songs are played.

Reason for Application
Instead of the usual alarms’ ringtones, Users waking up to their favorite songs might have a better effect on encouraging them to wake up.

How it works
The application uses python libraries (Datetime, Time, random) and Web driver imported from selenium to ensure the YouTube page is loaded.

Installation and setup
First clone this repository to your local machine using 
https://github.com/kahlinah/Skaehub-Project

Checkout into the master branch using 
git checkout master

Create a virtualenv on your machine and install the dependencies via
 pip install -r requirements.txt and activate it.

cd into the app folder and run python
 run-app.py 
If you get a similar window it shows your application is okey.


 
Tests
To run test Install pytest
pip install pytest
To run tests :
python -m pytest test_alarm.py


