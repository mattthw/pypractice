#!/usr/bin/env python
# import modules used here
import sys
import os

data = []

class Storage(object):

    def store(self, *args):
        global data
        data.append(args[0])

    def retrieve(self):
        global data
        return data

class Dialogue(object):

    def welcome(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print 'Hello. Plase select an option.'
        message = {1: 'add new text',2: 'view text',3: 'exit'}
        for x in range(1,4):
            print repr(x).rjust(2), 'to %s.'.rjust(3) % (message[x])

        return raw_input(': ')

    def list(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print 'The following strings are in storage:'
        global data
        for x in range(len(data)):
            print '|'.rjust(1), repr(x).rjust(2), data[x].rjust(3)
        print 'type 1 to return or any other key to exit.'
        if raw_input(': ') == str(1):
            main()
        else:
            exit()

    def new_string(self):
        print 'You may type your string in below'
        return raw_input(': ')

def _return():
    main()

def main():
    selec = Dialogue().welcome()
    if int(selec) == '':
        _return()

    if int(selec) == 1: #store new string
        Storage().store(Dialogue().new_string())
        main() #return to menu
    elif int(selec) == 2: #view stored string
        # print Storage().retrieve()
        Dialogue().list()
    else: #exit on bad response or quit
        sys.exit()

if __name__ == '__main__': #call main func after module fully loads
    main()