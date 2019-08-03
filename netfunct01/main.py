#!/usr/bin/env python3
import time
def commandpush(devicecmd):
    for coffeetime in devicecmd.keys():
        print("handshaking. .. ... connecting with " + coffeetime)

        for mycmds in devicecmd[coffeetime]:
            print("attemping to send command --->" + mycmds)

        print("")
        devicereboot([coffeetime])


def devicereboot(iplist):
    for ip in iplist:
        print(f"Connecting to {ip}",)
        print("\nREBOOTING NOW\n")


def main():
    work2do = {
        "10.1.0.1":["interface eth1/2", "no shut"],
        "10.2.0.1":["interface eth1/1", "shutdown"]
        }
    print("Welcome to the network device command pusher")

    print("\nData set found\n")

    commandpush(work2do)

main()
