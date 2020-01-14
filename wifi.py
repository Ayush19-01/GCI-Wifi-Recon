import subprocess
import threading
from getmac import get_mac_address
import os
os.system("clear")

def prRed(skk): return str("\033[91m{}\033[00m" .format(skk)) 
def prGreen(skk): return str("\033[92m{}\033[00m" .format(skk)) 
def prYellow(skk): return str("\033[93m{}\033[00m" .format(skk)) 
def prPurple(skk): return str("\033[95m{}\033[00m" .format(skk)) 
def prCyan(skk): return str("\033[96m{}\033[00m" .format(skk)) 

print(prYellow("Welcome to WiFi Reconnaissance tool\n"))
a=input(prRed("Press enter to scan your wifi network and get information related to device connected to it>>>"))
print(prGreen("\nScanning...\n"))
list0 = []
list1 = []
list2 = []
def recon(i):
    try:
        ip_address = '192.168.1.'+str(i)
        state = 'ping -c 1 '+ip_address
        result = subprocess.check_output(state.split()).decode().split('\n')
        
        for get in result:
            if '0% packet loss' in get: 
                list0.append(ip_address)
 
    except Exception as error:
        pass

for i in range(1, 255):
    try:
        t = threading.Thread(target=recon,args=(i, ))
        t.start()
    except Exception as error:
        print(prRed('Error Occurred!'))
        


for k in list0:
    mac = get_mac_address(ip=k)
    if mac != None:
    	list1.append(str(mac))
    	list2.append(str(k))
print(prYellow("Number of devices connected to your wifi : "),prCyan(str(len(list1))))
print()
print(prRed("         {:26}{}".format("Mac Address","Ip-Address\n")))
x=0
count=1
for l in list1:
	print("{}      {:38}{}".format(prGreen(count),prCyan(l),prPurple(list2[x])))
	print()
	x += 1
	count += 1
print(prRed("Closing..."))
