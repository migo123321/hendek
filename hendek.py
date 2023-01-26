#pip install socket
#pip install art
#pip install colorama
import time
import colorama 
from colorama import Fore
import socket
from art import tprint
tprint("hendeks")

print("""
[1] port checker
[2]port scanner 
[3]exit""")
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
option=int(input("option>>> "))
if (option==3):
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
else:
    print("[-] Error")
    time.sleep(5)
    exit    