#!/usr/bin/env python3

import csv
# Default Settings
CSV_FILE = "csv_users.csv"
TEMPLATE_FILE = "template.rc"
OUT_FILE_PREFIX = "admin.rc"

def set_defaults(message, var_value):
    # Will request input for default settings if user wants to change
    user_input = input(message)
    if user_input:
        var_value = user_input
    print(("-" * 10) + ">The following was set:", var_value)
    return var_value

def main():
    # Ask user if they want a different file
    print("Please set the following information in [] are the defaults....")
    TEMPLATE_FILE = set_defaults(
        f"Please enter template file and path[{TEMPLATE_FILE}]: ",
        TEMPLATE_FILE
        )
    CSV_FILE = set_defaults(
        f"Please enter CSV file and path[{CSV_FILE}]: ",
        CSV_FILE
        )
    OUT_FILE_PREFIX = set_defaults(
        f"Please enter the output file prefix[{OUT_FILE_PREFIX}]: ",
        OUT_FILE_PREFIX
        )

    # Open template file
    with open(TEMPLATE_FILE, "r") as template:
        template_contents = template.read()
    i = 0

    # Open CSV file using with no need to close
    with open(CSV_FILE, newline="") as f:
        # Read CSV file as a dictionary and loop thru rows
        csv_data = csv.DictReader(f)
        for row in csv_data:
            i += 1
            out_file_name = OUT_FILE_PREFIX + "%d"%(i, )
            # open and output file using template.
            with open(out_file_name, "w") as out_file:
                print(template_contents.format(**row), end="", file=out_file)

    print("\n")
    print(f"Created {i} files with a prefix of {OUT_FILE_PREFIX}......")

main()

