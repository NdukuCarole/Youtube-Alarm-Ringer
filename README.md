<h1><b>YOUTUBE RINGER ALARM CLOCK</h1>

<h2><b>Problem Definition</h2><br>
The main aim of this project is to create a command line application that takes user input of the YouTube songs links they would like, input the time (alarm) and once the countdown is done the application randomly selects from the user input links and prompts a YouTube browser where the songs are played.


<h2><b>Reason for Application</h2><br>
Instead of the usual alarms’ ringtones, Users waking up to their favorite songs might have a better effect on encouraging them to wake up.<br>

<h2><b>How it works</h2><br>
The application uses python libraries (Datetime, random) and Web driver imported from selenium to ensure the YouTube page is loaded.<br>

 <h2><b>Installation and setup</h2><br>
  
First clone this repository to your local machine using <br>
  
```
  git clone https://github.com/kahlinah/Skaehub-Project
  ```
 

Checkout into the master branch using 
```
  git checkout master
  
  ```

Create a virtualenv on your machine and install the dependencies via<br>
 ```
  pip install -r requirements.txt and activate .
  
  ```

cd into the app folder and run python<br>
``` 
  run-app.py 
  ```

<h2>Tests</h2>
  
To run test Install pytest<br>
```
  pip install pytest
  ```
To run tests :
```
  python -m pytest test_alarm.py
  ```
  
  <h2>Crediits</h2>
  <a href="https://github.com/kahlinah/">1.Caroline Katumo</a><br>
  <a href="https://skaehub.com/">2.Skaehub</a>


