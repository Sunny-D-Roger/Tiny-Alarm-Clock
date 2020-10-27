from tkinter import *
import multiprocessing
import sys
import keyboard
"""play sound as background process """
from playsound import playsound
import datetime
import  time


def alarm(set_alarm_timer, set_alarm_date):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%-I:%-M") # use %H for 24 hour format
        now_with_OOformat = current_time.strftime("%I:%M") # will use in both conditional statement
        date = current_time.strftime("%d/%m/%y")
        date_with_OOOOformat = current_time.strftime("%d/%m/%Y") # will use in elif statement (Notice capital "Y" here)
        print("===========================================================================")
        print(f"Current Date is: {date}, and time is {time.strftime('%H:%M:%S')}")
        print(f"Alarm set date is: {set_alarm_date} and time is {set_alarm_timer}")
        print("===========================================================================")
        if now == set_alarm_timer and date == set_alarm_date:
            print("Time to wake up idiot")
            p = multiprocessing.Process(target=playsound, args=("audio.mp3", ))
            p.start()
            print("Press 'q' to stop the alarm")
            if keyboard.read_key() == "q":
                print("\n\n\nSTOPPINGGGGG THIS UGLY ALARM!!!\n\n\n")
                print("Now you can re-use the application")
            p.terminate()
            break

        elif now_with_OOformat == set_alarm_timer and date_with_OOOOformat == set_alarm_date:
            print("Time to wake up idiot")
            p = multiprocessing.Process(target=playsound, args=("audio.mp3",))
            p.start()
            print("Press 'q' to stop the alarm")
            if keyboard.read_key() == "q":
                print("\n\n\nSTOPPINGGGGG THIS UGLY ALARM!!!\n\n\n")
                print("Now you can re-use the application")
            p.terminate()
            break

        elif now_with_OOformat == set_alarm_timer and date == set_alarm_date:
            print("Time to wake up idiot")
            p = multiprocessing.Process(target=playsound, args=("audio.mp3",))
            p.start()
            print("Press 'q' to stop the alarm")
            if keyboard.read_key() == "q":
                print("\n\n\nSTOPPINGGGGG THIS UGLY ALARM!!!\n\n\n")
                print("Now you can re-use the application")
            p.terminate()
            break

        elif now == set_alarm_timer and date_with_OOOOformat == set_alarm_date:
            print("Time to wake up idiot")
            p = multiprocessing.Process(target=playsound, args=("audio.mp3",))
            p.start()
            print("Press 'q' to stop the alarm")
            if keyboard.read_key() == "q":
                print("\n\n\nSTOPPINGGGGG THIS UGLY ALARM!!!\n\n\n")
                print("Now you can re-use the application")
            p.terminate()
            break

def actual_time():
    set_alarm_timer = f"{hour.get()[:2]}:{min.get()[:2]}"
    set_alarm_date = f"{day.get()[:2]}/{mon.get()[:2]}/{year.get()[:2]}"
    alarm(set_alarm_timer, set_alarm_date)

def quit_clock():
    sys.exit()

clock = Tk()
clock.title("Tiny Alarm Clock")
clock.geometry("400x160")
clock.wm_maxsize(400,160) # Constant window size
clock.configure(bg='#5f4b8b')

setYourAlarm = Label(clock,text = "When to wake you up?",fg="#ec9688",bg="#5f4b8b",font=("Helevetica",10,"bold"),width = 19).place(x=105, y=5)
alarm_time = Label(clock,text = "Hour   Min",fg= "#ec9688",bg= "#5f4b8b",font =("Helevetica",10,"bold")).place(x=55,y=35)

addDate = Label(clock, text = "Day    Mon   Year", font =("Helevetica",10,"bold"),fg= "#ec9688",bg= "#5f4b8b").place(x=219,y=35)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()

# The Variables we require to set the alarm date:
day = StringVar()
mon = StringVar()
year = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 5).place(x=55,y=55)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 5).place(x=100,y=55)

#Date required to set the alarm clock:
dayOfAlarm = Entry(clock, textvariable = day,bg= "pink",width= 5).place(x= 220, y=55)
monOfAlarm = Entry(clock, textvariable = mon,bg= "pink",width= 5).place(x = 265, y = 55)
yearOfAlarm = Entry(clock, textvariable = year,bg= "pink",width= 5).place(x = 310,y = 55)
#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command =actual_time).place(x =90,y=95)

quit_alarm = Button(clock,text= "Quit", command=quit_clock,width= "8").place(x=200, y=95)

#OPTIONAL:
# Display current time and date on existing clock:
#current_clock = Label(clock, font=('times', 20, 'bold'))
#current_date = Label(clock, font= ('times', 20, 'bold'))
#time1 = ''
#current_clock.pack()
#current_date.pack()

#def tick():
#    global time1
#    time2 = time.strftime("%H:%M:%S")
#    if time2 != time1:
#        time1 = time2
#        current_clock.config(text= time2)
    # calls itself after every 200ms seconds
    # to update and display correct time
#    current_clock.after(200, tick)

#def display_Current_date():
#    date1 = datetime.datetime.now().strftime("%d/%m/%Y")
#    current_date.config(text= date1)
#    current_date.after(1000, display_Current_date) # Update date every sec even tho it's not required lol

#tick()
#display_Current_date()



clock.mainloop()

#WARNING: Once a wrong time is set you will need to force quit the application
#         since the process of alarm starts it ends up freezing other process until 
#         the alarm rings once rang it would allow you to re-use the application
#         I roamed the internet never found a good alarm clock made using tkinter.
#         So this was the maximum time I gave to this tiny application and tkinter
#         lacks many things I mean you can create more functional clock from this point
#         but I am stopping here since making a more functional clock would be better
#         if I use PyQT(Portability has it's own benefits).
#Anyways feel free to add more features and experiment with it.
#I am stopping making it more functional because I got some other work to do.