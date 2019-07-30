#!/usr/bin/env python3
do_run = True

actions = [
        {
            "description": "Get IP Route",
            "command": "show ip route {}",
            "input": "Please enter an IP Address"
        },
        {
            "description": "Get IP arp entry",
            "command": "show ip arp | include {}",
            "input": "Please enter and IP Address"
        },  
        {
            "description": "Get interface config",
            "command": "show interface {}",
            "input": "Please enter an interface"
        },  
        {
            "description": "Get Module information",
            "command": "show mod",
            "input": ""
        }
    ]
while do_run:
    # Print Menu selection
    i = 0
    for action in actions:
        i+=1
        print(f"{i}: {action['description']}")


    print("\n\n\n\n0: to exit script.")
    print("=" * 50)
    user_input = input("Please make a selection: ")
    
    if user_input.isnumeric():
        user_input = int(user_input) - 1
        if user_input == -1:
            do_run = False
        elif user_input > -1 and user_input < len(actions):
            if actions[user_input]["input"]:
                user_value = input(actions[user_input]["input"])
                my_output = actions[user_input]["command"].format(user_value)
            else:
                my_output = actions[user_input]["command"]

            print("Congrats you have run the following command",my_output,sep="\n------")
        else:
            print(f"Sorry but the entry {user_input + 1} is not a valid select please open yours eyes and try again")
        
    else:
        print("Invalid Selection", user_input)

    if user_input != -1:
        input("Press Enter to continue")





