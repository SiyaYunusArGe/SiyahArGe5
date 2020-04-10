#!/usr/bin/env python

import os
os.system("apt.get install figlet")
os.system("clear")
print("""
  _  __             ____                 _  __  _    _  __      __ __      __  ______   _______ 
 | |/ /     /\     |  _ \      /\       | |/ / | |  | | \ \    / / \ \    / / |  ____| |__   __|
 | ' /     /  \    | |_) |    /  \      | ' /  | |  | |  \ \  / /   \ \  / /  | |__       | |   
 |  <     / /\ \   |  _ <    / /\ \     |  <   | |  | |   \ \/ /     \ \/ /   |  __|      | |   
 | . \   / ____ \  | |_) |  / ____ \    | . \  | |__| |    \  /       \  /    | |____     | |   
 |_|\_\ /_/    \_\ |____/  /_/    \_\   |_|\_\  \____/      \/         \/     |______|    |_|   

print("""

1)...FTP...
2)...SSH...
3)...MySQL...

""")
islemno = raw_input("Islem Numarasi: ")
hedefip = raw_input("Hedef Ip")
kady = raw_input("Kullanici Adi Dosya Yolu: ")
sifre = raw_input("Sifre: ")

if(islemno == "1"):
	os.system("nrack -P.21 -u " + kady + " -P" + sifre + " " + hedefip)
	
elif(islemno == "2"):
	os.system("nrack -P.22 -u " + kady + " -P" + sifre + " " + hedefip)
	
else: 
	print("Boyle Bir Sey Yok")
