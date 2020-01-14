#Made for the sole purpose of GCI 2019
import re
import subprocess
import threading
import os
import time
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
def fetch_data():
	global list0
	global list1
	arp_out = str(subprocess.check_output(['arp','-a']))
	x=arp_out.split()
	list0=[]
	list1=[]
	for i in x:
		if ":" in i:
			list0.append(i)
		if "." in i:
			list1.append(i)
		else:
			continue
fetch_data()
time.sleep(3)
print(prYellow("Number of devices connected to your wifi : "),prCyan(str(len(list1))))
print()
print(prRed("        {:30}{}".format("Ip-Address","Mac Address\n")))
x=0
count=1
for l in list1:
	print("{}      {:38}{}".format(prGreen(count),prCyan(l),prPurple(list0[x])))
	print()
	x += 1
	count += 1
print(prRed("Closing...\n"))
