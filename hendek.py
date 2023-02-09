#pip install socket
#pip install art
#pip install getpass
#bunu ben yaptım veben bir türküm mamungame
#pip install shutil
import shutil

import time
import socket
from art import tprint
from getpass import getpass
getpass("")
tprint("hendek")

print("""
[0]error
[1] port checker
[2]port scanner 
[3]Which tool should come???
[4]exit""")
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
option=int(input("option>>> "))
if (option==4):
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
    print("cupp")
    print(" Which tool should come???              ")
    print("  \            ")
    print("   \         ")
    print("    ,__,     ")        
    print("    (oo)____ ")     
    print("    (__)    )\\")
    print("       ||--|| *")
    
    print("shutil...")
    time.sleep(14)
      
else:
    print("[-] Error")
    time.sleep(5)
    exit    