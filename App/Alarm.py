
""" Alarm Clock
----------------------------------------
"""
import datetime
import time
import random
import re


from selenium import webdriver
from selenium.common.exceptions import WebDriverException,NoSuchElementException


import os
from twilio.rest import Client


TWILIO_PHONE_NUMBER = "the number youre calling from"

DIAL_NUMBERS = ["The number you want to call"]
TWIML_INSTRUCTIONS_URL = \
  "http://static.fullstackpython.com/phone-calls-python.xml"

client = Client("ACCOUNT SID", "AUTH TOKEN")







     

def getinputs():
    #user input to record the 

    
 while True:
    exit = input("Do you want to add a link (y/n)?  ")
    if exit.lower() == 'n':
            print() 
            choice = input("""
     Would you like to use system links (y/n)?
                        
                        """)
            if exit.lower() == 'n':
              
                 break
            else:
               youtube=("https://youtu.be/6CHs4x2uqcQ?list=RD6CHs4x2uqcQ")
               with open("system.txt","w") as f:
                f.write(youtube)

                

    else:

        name = input("link:")
                
        youtube_regex = (
                        r'(https?://)?(www\.)?'
                        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
                        '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')

        youtube_regex_match = re.match(youtube_regex, name)
        if youtube_regex_match:
                
            with open("youtube.txt","w") as f:
                f.write(name)
            
        else:
                print("url is not valid")
 return  False



       


#Alarm clock
def check_alarm_input(alarm_time):
     

    if len(alarm_time) == 1: # [Hour] Format

        if alarm_time[0] < 24 and alarm_time[0] >= 0:
            return True
    if len(alarm_time) == 2: # [Hour:Minute] Format
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
        alarm_time[1] < 60 and alarm_time[1] >= 0:
            return True
    elif len(alarm_time) == 3: # [Hour:Minute:Second] Format
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
        alarm_time[1] < 60 and alarm_time[1] >= 0 and \
        alarm_time[2] < 60 and alarm_time[2] >= 0:
            return True
    return False



# Get user input for the alarm time
getinputs() 
print("Set a time for the alarm (Ex. 06:30 or 18:30:00)")
while True:
    alarm_input = input(">> ")
    try:
        alarm_time = [int(n) for n in alarm_input.split(":")]
        if check_alarm_input(alarm_time):
            break
        else:
            raise ValueError
    except ValueError:
        print("ERROR: Enter time in HH:MM or HH:MM:SS format")


# Convert the alarm time from [H:M] or [H:M:S] to seconds
seconds_hms = [3600, 60, 1] # Number of seconds in an Hour, Minute, and Second
alarm_seconds = sum([a*b for a,b in zip(seconds_hms[:len(alarm_time)], alarm_time)])


#Get the current time of day in seconds
now = datetime.datetime.now()
current_time_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])

#Calculate the number of seconds until alarm goes off
time_diff_seconds = alarm_seconds - current_time_seconds

#If time difference is negative, set alarm for next day
if time_diff_seconds < 0:
    time_diff_seconds += 86400 # Number of seconds in a day






# Display the amount of time until the alarm goes off
print("Alarm set to go off in %s" % datetime.timedelta(seconds=time_diff_seconds))





def dial_numbers(numbers_list):
    """Dials one or more phone numbers from a Twilio phone number."""
    for number in numbers_list:
        print("Dialing " + number)
        # set the method to "GET" from default POST because Amazon S3 only
        # serves GET requests on files. Typically POST would be used for apps
        client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER,
                            url=TWIML_INSTRUCTIONS_URL, method="GET")








#Sleep until the alarm goes off
time.sleep(time_diff_seconds)
#Time for the alarm to go off
print("Wake Up!")



#Load list of possible video URLs


with open("system.txt", "r") as alarm_file:
    videos = alarm_file.readlines()


with open("youtube.txt", "r") as alarm_file:
    videos = alarm_file.readlines()

    
    



# Open a random video from the list
driver = webdriver.Chrome()
driver.implicitly_wait(100)

try:
    driver.get(random.choice(videos))
    
except WebDriverException as e:
    print("An error occured ", e)





if __name__ == "__main__":
    dial_numbers(DIAL_NUMBERS)
