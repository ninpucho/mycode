#!/usr/bin/env python3

import csv
# Default Settings
csv_file = "csv_users.csv"
template_file = "template.rc"
out_file_prefix = "admin.rc"

def set_defaults(message,var_value):
    # Will request input for default settings if user wants to change
    user_input = input(message)
    if len(user_input.strip()) > 0:
        var_value = user_input
    print(("-" * 10) + ">The following was set:",var_value)
    return var_value


# Ask user if they want a different file
print("Please set the following information in [] are the defaults....")
template_file = set_defaults(f"Please enter template file and path[{template_file}]: ",template_file)
csv_file = set_defaults(f"Please enter CSV file and path[{csv_file}]: ",csv_file)
out_file_prefix = set_defaults(f"Please enter the output file prefix[{out_file_prefix}]: ",out_file_prefix)

# Open template file
template = open(template_file,"r")
template_contents = template.read()
i = 0

# Open CSV file using with no need to close
with open(csv_file,newline="") as f:
    # Read CSV file as a dictionary and loop thru rows
    for row in csv.DictReader(f):
        i+=1
        out_file_name = out_file_prefix + "%d"%(i,)
        # open and output file using template.
        with open(out_file_name,"w") as out_file:
            print(template_contents.format(**row),end="",file=out_file)
# Closing template file as it was not opened using with
template.close()