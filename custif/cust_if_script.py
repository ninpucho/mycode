#!/usr/bin/env python3

def ip_check(s):

    ip_list = s.split(".")
    ip = ""
    status = True
    error_message = "What? Seriously you think {} is an IPv4 address? Try again...".format(s)
    if len(ip_list) == 4:
        for x in ip_list:
            if x.isnumeric():
                #print(f"{x}")
                if int(x) >= 0 and int(x) <= 255:
                    pass
                else:
                    return {"status": status, "response": error_message}
            else:
                return {"status": False, "response": error_message}
    else:
        return {"status": False, "response": error_message}

    return {"status":True, "response": s}

def main():
    do_run = True

    actions = [
            {
                "description": "Get IPv4 Route",
                "command": "show ip route {}",
                "input": "Please enter an IPv4 Address: ",
                "type": "ipv4"
            },
            {
                "description": "Get IPv4 arp entry",
                "command": "show ip arp | include {}",
                "input": "Please enter and IPv4 Address: ",
                "type": "ipv4"
            },  
            {
                "description": "Get interface config",
                "command": "show interface {}",
                "input": "Please enter an interface: ",
                "type": ""
            },  
            {
                "description": "Get Module information",
                "command": "show mod",
                "input": "",
                "type": ""
            }
        ]
    while do_run:
        # Print Menu selection
        print("\n" * 3)
        print("=" * 50)
        print("My custom if app")
        print("-" * 50)
        my_output = "" 
        i = 0
        for action in actions:
            i+=1
            print(f"{i}: {action['description']}")


        print("\n\n\n\n0: to exit script.")
        print("=" * 50)
        user_input = input("Please make a selection: ")
        success_message = "Congragulations you have sent the following command \n{}\n" + ("bla " * 25)
    
        if user_input.isnumeric():
            user_input = int(user_input) - 1
            if user_input == -1:
                do_run = False
            elif user_input > -1 and user_input < len(actions):
                if actions[user_input]["input"]:
                    exit_check = True
                    while exit_check:
                        user_value = input(actions[user_input]["input"])
                        if actions[user_input]["type"] == "ipv4":
            #                exit_check = True
            #            while exit_check:
                            ip = ip_check(user_value)
                            if ip["status"]:
                                my_output = "Congragulations you have sent the following command \n" + actions[user_input]["command"].format(user_value) + "\n" + ("bla " * 25)
                                exit_check = False
                            elif user_value.lower() == "exit":
                                exit_check = False
                                my_output = "User has exited IPv4 checks"
                            else:
                                print("ERROR: ", ip["response"])
                                print("Type EXIT to quit IPv4 Checks")
                        else:
                            my_output = success_message.format(actions[user_input]["command"].format(user_value))
                            exit_check = False
                else:
                    my_output = success_message.format(actions[user_input]["command"].format(user_value))

                print(my_output,sep="\n------")
            else:
                print(f"What? {user_input + 1} is not even in the list try again")
        
        else:
            print(f"What are you thinking {user_input} is not in the list of options....")

        if user_input != -1:
            input("Press Enter to continue")


main()


