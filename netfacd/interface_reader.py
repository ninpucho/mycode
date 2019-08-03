#!/usr/bin/env python3
import netifaces

def getip(iface, info):
    #netifaces.interfaces()
    #print(i)
    try:
        if info.lower() == "ip":
            return netifaces.ifaddresses(iface)[netifaces.AF_INET][0]["addr"]
        elif info.lower() == "mac":
            return netifaces.ifaddresses(iface)[netifaces.AF_LINK][0]["addr"]
        else:
            return f"ERROR: please enter a valid request (IP/MAC) {info}"
    except :
        return f"ERROR: An error occured please review values iterface {iface}, type {info}"

print(netifaces.interfaces())

for i in netifaces.interfaces():
    try:
        print(("*" * 10) + "Details of Interface - " + i + ("*" * 10))
        print("MAC:",(netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]["addr"])
        print("IP:",netifaces.ifaddresses(i)[netifaces.AF_INET][0]["addr"])
    except:
        print("Could not collect adapter information")

print(getip("ens3","ip"))

iface = input("Please enter an interface: ")
info = input("Please tell me why info you want [IP/MAC]: ")

print(getip(iface,info))

