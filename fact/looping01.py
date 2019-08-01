#!/usr/bin/env python3
import uuid
iplist = ["10.1.1.1","10.2.2.2","10.3.3.3"]

for ip in iplist:
    print(ip)

print("="*100)


dnsfile = open("dnsservers.txt")

dnslist = dnsfile.readlines()
print(dnsfile.read())
for svr in dnslist:
    print(svr, end="")

dnsfile.close()


print("="*100)


howmany = int(input("How many UUIDS should be generated> "))

print("Generating UUIDS...")

for rando in range(howmany):
    print(uuid.uuid4())



