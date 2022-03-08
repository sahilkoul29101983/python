#!/usr/bin/env python3

ipchk = input("Apply an IP address: ") # This line is now prompt for input

def main():
    #ifuser set IP of Gateway
    if ipchk == "192.168.70.1":
        print("Looks like the IP address of the Gateway was set: " + ipchk + "This is not recommended")
        
    elif ipchk: # if any data is provided, this will test true
        print("Looks like the IP address was set: " + ipchk)

    else: # if data is not provided
        print("You did not provide input.")

main()
