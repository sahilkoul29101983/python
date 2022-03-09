#!/usr/bin/env python3
'''Sahil
    For - Looping across a file opened with 'with'
         while also being gentle on memory consumption.
         Sort domains ending in .org and .com into files
         org-domain.txt and com-domain.txt.'''

def main():

    # Open file in read mode
    with open("dnsservers.txt", "r") as dnsfile:  # "r" is read modes
        # indent to keep the dnsfile object open
        # Loop accross the line in the file
        for svr in dnsfile:
            svr = svr.rstrip('\n') # remove newline char if exists
                                    # would exist on all but the last line

            # IF the string svr ends with 'org'
            if svr.endswith('org'):
                with open("org-domain.txt", "a") as srvfile: # 'a' is append mode
                    srvfile.write(svr + "\n")

            # Else-IF the string svr ends with'com'
            elif svr.endswith('com'):
                with open("com-domain.txt", "a") as srvfile:
                    srvfile.write(svr + "\n")

main()



    
