#!/usr/bin/env python3
''' Sahil Koul
    For - Using a files's lines as a source for the for-loop'''

def main():
    dnsfile = open("dnsservers.txt", "r") # open file in read mode

    #create list of lines
    dnslist = dnsfile.readlines()

    #loop over lines
    for svr in dnslist:
        #print and end without a newline
        print(svr, end="") # the line we read ALREADY contains a \n (newline)

        # close the file (we created the list of lines)
        dnsfile.close() # best practice to cose your file

main()
