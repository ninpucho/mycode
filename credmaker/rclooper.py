#!/usr/bin/env python3

import csv

input_file = input("Please enter CSV file and path: ")

f = open(input_file,"r")
i = 1


file_template = [
        "export OS_AUTH_URL={}",
        "export OS_IDENTITY_API_VERSION=3",
        "export OS_PROJECT_NAME={}",
        "export OS_PROJECT_DOMAIN_NAME={}",
        "export OS_USERNAME={}",
        "export OS_USER_DOMAIN_NAME={}",
        "export OS_PASSWORD={}"
    ]


for row in csv.reader(f):
    out_file_name = "admin.rc%d"%(i,)
    out_file = open(out_file_name,"w")
    #print(row)
    #print(out_file_name)
    x = 0
    for line in file_template:
        if "{}" in line:
            print(line.format(row[x]),file=out_file)
            x+=1
        else:
            print(line,file=out_file)
        #pass
    out_file.close()
    i+=1

f.close()
