#pip install socket
#pip install art
#pip install getpass
#bunu ben yaptım veben bir türküm mamungame
#pip install shutil

import shutil
import random
import time
import socket
from art import tprint
from getpass import getpass
getpass("")
tprint("hendek")

print("""
[0]not exit!!!
[1]port checker
[2]port scanner 
[3]password checker
[4]password scanner
[5]exit""")
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
option=int(input("option>>> "))
if (option==5):
    print("exit")
    exit
elif(option==1):
    targeT=input("[+]targetwbesite / ıp>>> ")
    porT=int(input("[+] port>>> "))
    try:
        s.connect((targeT,porT))
        print("[+] PORT OPEN>>> ",str(porT))
        time.sleep(14)
    except:
        
        print("[-] PORT CLOES>>> "+str(porT))
        time.sleep(14)
elif(option==2):
    targeT=input("[+] Target webste/ıp>> ")
    miN=int(input("[+] minport>>> "))
    maX=int(input("[+] maxport>>> "))
    for porT in range(miN,maX+1):
        try:
            s.connect((targeT,porT))
            print("[+]Port open>>> ",str(porT))
            time.sleep(14)
            break
        except:
            print("[-] port close>>> ",str(porT))
            time.sleep(14)
elif (option==3):
    a_a12=int(input("lenght"))
    owet="qwertyuıopğüasdfghjklşiçömnbvcxz"
    
    upper_lower="qwertyuıopğüasdfghjklşiçömnbvcxz"
    NUMPERS="0123456789"
    strings=owet+upper_lower+NUMPERS
    length=a_a12
    password="".join(random.sample(strings,length))
    print("[+]password: ",password)
    time.sleep(1)
elif (option==4):
    mİN=int(input("min"))
    mAx=int(input("max"))
    a_a12=int(input("lenght"))
    length=a_a12
    for i in range(mİN,mAx+1):
       
        owet="qwertyuıopğüasdfghjklşiçömnbvcxz"
        upper_lower="qwertyuıopğüasdfghjklşiçömnbvcxz"
        NUMPERS="0123456789"
        strings=owet+upper_lower+NUMPERS
        
        password="".join(random.sample(strings,length))
        print("[+]password: ",password)
        time.sleep(1)
else:
    print("[-] Error")
    time.sleep(5)
    exit    