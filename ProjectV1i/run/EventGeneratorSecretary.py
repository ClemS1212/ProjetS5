from logging.config import DEFAULT_LOGGING_CONFIG_PORT
import random as rd
import time
import os

events=['absent', 'pause', 'consultation', 'surgery', 'emergency']
doctor = ''


def event_generator(doctor,temps):
    """if doctor=='consultation':
        fichier = open("commandflow", "a")
        fichier.write("(assert (stop consultation))\n")
        fichier.close
        print('stop consultation')
    elif doctor=='surgery':
        fichier = open("commandflow", "a")
        fichier.write("(assert (stop surgery))\n")
        fichier.close
        print('stop surgery')"""
    
    #for t in range(1440):
    if 0<=temps<480:              #morning between 0000 and 0800
        t=temps
        doctor = 'absent'
        temps+=30
        return doctor, temps, temps-t

    elif 480<=temps<720:         #morning between 0800 and 1200
       p=rd.random()
       if p <= 0.6:
           t=temps
           doctor='admission'    #60% to be in consultation
           temps+=30
           return doctor, temps, temps-t
       elif 0.6<p<=0.85:         #20% to be in surgery
           doctor = 'pause-cafe'
           k=rd.random()          #long, medium or short surgery
           if k<=0.4:
               t=temps
               temps+=60
               return doctor, temps, temps-t
           elif 0.4<k<=0.6:
               t=temps
               temps+=120
               return doctor, temps, temps-t
           elif 0.6<k<=0.75:
               t=temps
               temps+=180
               return doctor, temps, temps-t
           elif 0.75<k<=0.85:
               t=temps
               temps+=240
               return doctor, temps, temps-t
           elif 0.85<k<=0.90:
               t=temps
               temps+=300
               return doctor, temps, temps-t
           elif 0.90<k<=0.95:
               t=temps
               temps+=360
               return doctor, temps, temps-t
           elif 0.95<k<=0.975:
               t=temps
               temps+=480
               return doctor, temps, temps-t
           elif 0.975<k<=0.99:
               t=temps
               temps+=600
               return doctor, temps, temps-t
           else:
               t=temps
               temps+=720
               return doctor, temps, temps-t
       else:
            doctor = 'pause'        #20% to be on pause
            t=temps
            temps+=30
            return doctor, temps, temps-t

    elif 720<=temps<810:     #midday pause
        doctor= 'pause'
        t=temps
        temps+=30
        return doctor, temps, temps-t

    elif 810<=temps<1110:            #afternoon between 1330 and 1830
        p=rd.random()
        if doctor=='pause-cafe':       # pause after surgery if lunchpause 
            doctor='pause'
            t=temps
            temps+=30
            return doctor, temps, temps-t
        elif p<=0.6:
           doctor='admission'    #60% to be in consultation
           t=temps
           temps+=30
           return doctor, temps, temps-t
        elif 0.6<p<=0.85:         #20% to be in surgery
           doctor = 'pause-cafe'
           k=rd.random()          #long, medium or short surgery
           if 0.4<k<=0.6 and temps+120<1440:
               t=temps
               temps+=120
               return doctor, temps, temps-t
           elif 0.6<k<=0.75 and temps+180<1440:
               t=temps
               temps+=180
               return doctor, temps, temps-t
           elif 0.75<k<=0.85 and temps+240<1440:
               t=temps
               temps+=240
               return doctor, temps, temps-t
           elif 0.85<k<=0.90 and temps+300<1440:
               t=temps
               temps+=300
               return doctor, temps, temps-t
           elif 0.90<k<=0.95 and temps+360<1440:
               t=temps
               temps+=360
               return doctor, temps, temps-t
           elif 0.95<k<=0.975 and temps+480<1440:
               t=temps
               temps+=480
               return doctor,temps, temps-t
           elif 0.975<k<=0.99 and temps+600<1440:
               t=temps
               temps+=600
               return doctor, temps, temps-t
           elif k>0.99 and temps+720<=1440:
               t=temps
               temps+=720
               return doctor, temps, temps-t
           else:
               t=temps
               temps+=60
               return doctor,temps, temps-t
        else:
            doctor = 'pause'        #20% to be on pause
            t=temps
            temps+=30
            return doctor,temps, temps-t
        
    elif temps>1110 and doctor=='pause':
        doctor='absent'
        t=temps
        temps+=30
        return doctor, temps, temps-t
    elif temps>1110 and doctor=='absent':
        t=temps
        temps+=30
        return doctor, temps, temps-t
    else:
        doctor='pause'
        t=temps
        temps+=30
        return doctor, temps, temps-t



#def multiple(k,n):
#    if n%k==0:
#       return True
#    return False


temps=0
d=0
print('im a secretary')
fichier = open("commandflow", "a")
fichier.write("(load rules)\n")
fichier.write("(load-facts facts)\n")
fichier.write("(watch rules)\n")
fichier.write("(watch facts)\n")
fichier.write("(assert (job secretary))\n")
fichier.close

while d<1:
    result=event_generator(doctor, temps-d*1440)
    #print('activity :', result[0],'/ day :',d+1,'/ end hour :', result[1]/60,'/ duration :', result[2]/60)
    fichier = open("commandflow", "a")
    fichier.write("(assert (event (type "+str( result[0])+") (priority 5)))\n")
    fichier.write("(run)\n")
    if result[0] =='admission':
        fichier = open("commandflow", "a")
        fichier.write("(assert (stop admission))\n")
        fichier.close
        print('stop admission')
    elif result[0] =='pause-cafe':
        fichier = open("commandflow", "a")
        fichier.write("(assert (stop pause-cafe))\n")
        fichier.close
        print('stop pause-cafe')

    #os.system('echo (assert (event (type +str( result[0])+) (priority 5)))\n')
    fichier.write("(run)\n")
    fichier.close
    print( '(assert (event (type ', result[0],') (priority 5))')
    temps=result[1]+d*1440
    doctor=result[0]
    time.sleep(result[2]/15)
    if temps%1440==0: 
        d+=1





    
    
