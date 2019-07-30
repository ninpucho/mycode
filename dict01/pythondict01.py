#!/usr/bin/env python3

## Create a dictionary
switch = \
    {
        "hostname": "sw1",
        "ip": "10.0.1.1",
        "version": "1.2",
        "vendor": "cisco"
     }   

#display parts of the dictionary

print(switch["hostname"])

print(switch["ip"])

## Request a fake key

#print(switch["fake"])

## Request Fake ley with .get() method

print("First test - .get()")
print(switch.get("lynx","THE KEY IS IN ANOTHER CASTLE"))

print("Third test - .get()")
print(switch.get("version"))


print("Forth test - keys()")
print(switch.keys())

print("Fifth test - values()")
print(switch.values())


print("Sixth Test - pop()")
switch.pop("version")
print("keys():", switch.keys())

print("values():",switch.values())

print("Eith test - ADD a new value")
switch["password"] = "qwerty"

print("keys():",switch.keys())
print("values:",switch.values())

