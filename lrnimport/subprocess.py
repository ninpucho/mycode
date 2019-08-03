#!/usr/bin/env python3

from subprocess import call

call(["ip","link", "show", "up"])
#print(x)
print("this program will check your interface.")
interface = input("Enter an interface, like, ens3: ")
call(["ip","link", "show", "up"])
call(["ip","link", "show", "up"])

