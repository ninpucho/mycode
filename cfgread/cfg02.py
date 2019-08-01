#!/usr/bin/env python3

# Explore Read
# create file object in r read mode
configfile = open("vlanconfig.cfg","r")

configblob = configfile.read()

configlist = configblob.splitlines()
print(configlist)


print(len(configlist))


# interate through configlist
#for x in configlist:
#    print(x)

# Close
configfile.close()

