#!/usr/bin/env python3

hostname = "MTG"

if hostname == "MTG":
    print("The hostname was found to be " + hostname)



hostname = input("What value should we set for hostname?")

if hostname.lower() == "mtg":
    print("The hostname was found to be " + hostname)
    print("hostname matches expected config.")
else:
    print(hostname + " Not Found")

print("exiting script")
