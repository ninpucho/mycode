#!/usr/bin/env python3

# Explore Read
# create file object in r read mode
configfile = open("vlanconfig.cfg","r")

## display file to the screen - .read()
print(configfile.read())

## close file

configfile.close()



## Export Readlines
## Re-Create file object
configfile = open("vlanconfig.cfg","r")

# Make a list of file lines - .readlines()
configlist = configfile.readlines()
print(configlist)

# interate through configlist
for x in configlist:
    print(x.strip())

# Close
configfile.close()

