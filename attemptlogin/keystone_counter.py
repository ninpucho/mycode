#!/usr/bin/env python3
loginfail = 0
logins = 0
ks_file = open("keystone.common.wsgi","r")
ks_lines = ks_file.readlines()
search_string = "Authorization failed"
for line in ks_lines:
    if search_string in line:
        print(line)
        loginfail += 1
    #elif 
print(f"number for failed login attempts {loginfail}")
