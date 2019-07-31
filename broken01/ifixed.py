#!/usr/bin/env python3





calc1 = 0.0
calc2 = 0.0
operation = ""

# corrected raw_input() to input

#while (calc1 != "q")
# Corrected missing :
while (calc1 != "q"):
    print("\nWhat is the first operator? Or, enter q to quit: ")
    calc1 = input()
    #if calc1 == "Q":
    # Correction to case of q and added lower
    if calc1.lower() == "q":
        break
    elif not calc1.isnumeric():
        print("not a number quiting")
        break
    calc1 = float(calc1)   
    print("\nWhat is the second operator? Or, enter q to quit: ")
    calc2 = input()
    #if calc2 == "q":
    # Corrected by adding lower()
    if calc2.lower() == "q":
        break
    elif not calc2.isnumeric():
        print("not a number quiting")
        break
    calc2 = float(calc2)
    print("Enter an operation to perform on the two operators (+ or -): ")
    operation = input()
    if operation == "+":
        #print("\n + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))
        # Corrected missing "
        print("\n" + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))

    #ifel operation == '-':
    elif operation == '-':
        print("\n" + str(calc1) + " - " + str(calc2) + " = " + str(calc1 - calc2))
    else:
        print("\n Not a valid entry. restarting...")




