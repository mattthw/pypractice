#1/usr/bin/env pyhton
#imports
import sys

class fileOperations(object):

    def readFile(self, f):
        for x in f:
            print x

    def makeList(self, f):
        global samp_list
        samp_list = f.readlines()
        """Readlines is already a list. This means I can
        simply make my global list equal to the data of
        variable f."""

#GLOBAL SECTION

def fileCheck():
    try:
        open("sample.txt","r")
        return 1
    except IOError:
        print "sample.txt not found. Exiting program."
        return 0

if __name__ == '__main__':
    #IS FILE AVAILABLE
    if fileCheck() == 0:
        exit() #EXIT IF NOT
    #PRINT LINES IN FILE
    with open("sample.txt","r") as f:
        fileOperations().readFile(f)
    #SET LINES IN FILE TO GLOBAL LIST; PRINT LIST
    print "\nAdding Lines in ", f.name, " to new list object."
    print "-"*48
    samp_list = []
    with open("sample.txt","r") as f:
        fileOperations().makeList(f)
    for x in samp_list:
        print x,