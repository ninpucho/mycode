#!/usr/bin/env python3

out_file_name = "admin.rc"
out_file = open(out_file_name,"a")


file_template = [
        "export OS_AUTH_URL={}",
        "export OS_PROJECT_NAME={}",
        "export OS_PROJECT_DOMAIN_NAME={}",
        "export OS_USERNAME={}",
        "export OS_USER_DOMAIN_NAME={}",
        "export OS_PASSWORD={}"
    ]


for i in file_template:
    message = i.replace("export ","").replace("={}","")
    input_string = input("What is the " +  message + "? ")
    print(i.format(input_string),file=out_file)

out_file.close()
