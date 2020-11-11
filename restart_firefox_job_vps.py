from datetime import datetime
import os
import time
import json
import pytz
import win32ui

with open('config.json', 'r') as f:
    config_json = json.load(f)

restart_firefox_time =config_json['DEFAULT']['restart_firefox_time']


print("Bot Ver_1.2")




def write_log(text, file):
    f = open(file, 'a')
    tz_paris_time  = pytz.timezone('Europe/Paris')
    paris_now_time = datetime.now(tz_paris_time)
    curr_datetime=paris_now_time.strftime("%d-%m-%Y_%I-%M-%S_%p")          # 'a' will append to an existing file if it exists
    f.write(curr_datetime+"::"+"{}\n".format(text))  # write the text to the logfile and move to next line
    return 

logfile = r"mylogfile.log"  # name of my log file

def WindowExists(classname):
    try:
        win32ui.FindWindow(classname, None)
    except win32ui.error:
        return False
    else:
        return True

def resatrt_firefox():
    # currdateSTR = datetime.now().strftime("%H:%M:%S" )
    tz_paris  = pytz.timezone('Europe/Paris')
    paris_now = datetime.now(tz_paris)
    # print(paris_now)
    currdateSTR=paris_now.strftime("%H:%M:%S")
    if currdateSTR == (restart_firefox_time):#23:43:10
        print("That's awesome! now time to start kill firefox")
        # var=input("i am waiting for input")
        write_log("killing Firefox but trigger called", logfile)
        #os.system("taskkill /f /t /im Firefox.exe")
        filepath = 'close_firefox_window.exe'
        os.startfile(filepath)
		
        print("put some dealy 30sec and start firefox again.")
        time.sleep(30) # Delay for 1 minute (60 seconds).
        if WindowExists("MozillaWindowClass"):
            print("firefox is running, try again for killing firefox.")
            write_log("try again for killing Firefox but trigger called", logfile)
            #os.system("taskkill /f /t /im Firefox.exe")
            filepath = 'close_firefox_window.exe'
            os.startfile(filepath)
            print("again put some dealy 30sec and start firefox again.")
            time.sleep(30) # Delay for 1 minute (60 seconds).
        else:
            print("firefox is not running,so you can start")
        
        if WindowExists("MozillaWindowClass"):
            print("firefox still runnning so ingore this time for firefox restart")
        else:
            print("firefox is not running,so you can start")
            os.system("start Firefox.exe")
            write_log("start Firefox again", logfile)
    else:
        print(currdateSTR+"::wiating to restart firefox at desire time ....("+restart_firefox_time+")")
        # write_log("still waitiing for traiger time..", logfile)      

while True:
    resatrt_firefox()