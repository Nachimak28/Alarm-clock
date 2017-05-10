import datetime
import time as time
from pygame import mixer
now = datetime.datetime.now().time()
mixer.init()
mixer.music.load('C:/Users/nachiket/Music/08. Mountains.mp3')


hour = int(str(now.hour))
minute = int(str(now.minute))
second = int(str(now.second))

print("Current time is: ",hour,":",minute,":",second)


ehr = int(input("Enter hours: "))
emin = int(input("Enter minutes: "))

if(ehr>23 and emin>59 and ehr<0 and emin<0 ):
    print("Enter correct time please")
else:
    print(ehr,":",emin)

hour = int(str(now.hour))
minute = int(str(now.minute))
second = int(str(now.second))

mindif = 0
hrdif = 0

if(ehr<hour):
    hrdif = (ehr+24)-hour
elif(ehr==hour):
    hrdif = 0
else:
    if((ehr-hr)==1 and minute<=59):
        mindif = 60-minute
        hrdif = 0
    else:
        hrdif = ehr-hour
    
if(emin<minute):
    mindif = (emin+60)-minute-1
elif(emin==minute):
    mindif=0
    print("Can't go back in time XD")

else:
    if((emin-minute)==1 and second<=59):
        second = 60 - second
        mindif = 0
    else:
        mindif = emin-minute-1  
print(second)
if(ehr == hour and emin == minute):
    print("Please set correct time")
else:
    minalm =(hrdif*60)+mindif
    secalm =(hrdif*3600)+(mindif*60)+(60-second)
    print(minalm," of minutes until alarm")
    print(secalm," seconds till alarm")
    time.sleep(secalm)
    print("Wakey wakey")
    #mixer.init()
    #mixer.music.load('C:/Users/nachiket/Music/08. Mountains.mp3')
    mixer.music.play()
    snooze = int(input("Do u want to snooze? press 1 for yes"))
    if(snooze==1):
        stime = int(input("Enter snooze time in mins  press 1)5 mins 2)10 mins 3)15 mins"))
        if(stime == 1):
            mixer.music.stop()
            time.sleep(300)      
            mixer.music.play()
        elif(stime == 2):
            mixer.music.stop()
            time.sleep(600)
            mixer.init()
            mixer.music.play()
        elif(stime == 3):
            mixer.sleep.stop()
            time.sleep(900)
            mixer.init()
            mixer.music.play()
        else:
            print("Good morning Starshine, the world says Hello")
    else:
        mixer.music.stop()


