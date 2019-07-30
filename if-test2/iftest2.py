#!/usr/bin/env python3

#part 1
ipchk = "192.168.0.1"
if ipchk:
    print("Looks like the ip was set: " + ipchk)


#part 2
ipchk = input("Apply and IP address: ")
if ipchk:
    print("Looks like the ip was set: " + ipchk)

else:
    print("Ip was not set..")

#par3
ipchk = input("Apply and IP address: ")
if ipchk =="192.168.70.1":
    print("Looks like the gateway is set to: " + ipchk)

elif ipchk:
    print("Looks like the ip was set: " + ipchk)
else:
    print("Ip was not set..")
    
