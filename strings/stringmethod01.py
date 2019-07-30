#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

def main():
    # create a small string
    lilstring = "Alta3 Research offers classes on python coding"
    print(lilstring)
    newlist = lilstring.split(" ")
    print(newlist)

    # create a list of strings
    myiplist = ["192","168","0","12"]
    #set single ip as the result of the joining the list myiplist around the "."
    singleip = ".".join(myiplist)
    #Display single ip
    print(singleip)

#call out main function
main()
