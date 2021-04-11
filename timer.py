import time
import winsound

def countdown(t):
    while t > 0: 
      mins = t // 60
      secs = t % 60 
      timer = "{:02d}:{:02d}".format(mins, secs) 
      print(timer, end="\r")
      time.sleep(1)
      t -= 1
    winsound.Beep(500, 1000)
    print("Time is up!\n")

#t = input("How many seconds the timer should be? ")
#countdown(int(t)) 

def define_needed_time(word):
    if word == "black tea":
        t = 240
    elif word == "green tea":
        t = 120
    elif word == "coffee":
        t = 180
    else:
        t = input("How many seconds the timer should be? ")
    return t

word = input("""\n 
What do you wanna do?\n 
black tea; green tea\n
coffee\n 
custom\n
Write your choise: """)
countdown(int(define_needed_time(word))) 