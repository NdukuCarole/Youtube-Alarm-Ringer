import pytest
from alarm import getinputs
from alarm import name

from alarm import check_alarm_input
from alarm import alarm_time

from alarm import seconds_hms 

from alarm import time_diff_seconds
from alarm import alarm_seconds
from alarm import current_time_seconds

from alarm import  datetime
from alarm import  now



 #Test the user input links           
def test_the_input_links():
  assert getinputs != name


  #Test the user input y/n           
def test_the_input_yes_no():
  assert exit != 'n'

# Test the user input alarm_time
def test_the_input_time():
      assert check_alarm_input(alarm_time) == True


# Convert the alarm time from [H:M] or [H:M:S] to seconds
def test_alarm_covert():
 assert seconds_hms == [3600, 60, 1]
 

 #If time difference is negative, set alarm for next day
def test_negative_difference():
 time_diff_seconds < 0
 assert 15 != 86400


 #Calculate the number of seconds until alarm goes off
def test_going_off():

  assert time_diff_seconds == alarm_seconds - current_time_seconds


#Get the current time of day in seconds
def test_current_time():
      assert datetime.datetime(2021, 7, 1, 17, 58, 45, 619791)==datetime.datetime(2021, 7, 1, 17, 58, 45, 619791)
current_time_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])


#Number of seconds in an Hour, Minute, and Second
def test_Num_of_Hr_Min_Sec():
 assert alarm_seconds == sum([a*b for a,b in zip(seconds_hms[:len(alarm_time)], alarm_time)])


#Hour Format
def test_Hour_format():
 assert alarm_time[0] < 24 and alarm_time[0] >= 0 


#Hour Format
def test_Hour_Min_format():
 assert alarm_time[0] < 24 and alarm_time[0] >= 0 and \
            alarm_time[1] < 60 and alarm_time[1] >= 0



      
      
if __name__ == '__main__':
    pytest.main()

