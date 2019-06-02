
from datetime import date #import datetime

def ticket(speed, birthday): 
    if(birthday == True):
        speed = speed-5
    if(speed <= 60):
        return 'No Ticket'
    elif(speed>60 and speed<=80):
        return 'Small Ticket'
    else:
        return 'Big Ticket'

speed = int(input('Enter your speed(in km/h)::')) 
birthday = input('Enter your birthday in the format "YYYY-MM-DD"::') # input should be in YYYY-MM-DD format
today = str(date.today()) 

if(birthday == today):
    tkt = ticket(speed, True)
else:
    tkt = ticket(speed, False)
   
print('You are given - ', tkt)
