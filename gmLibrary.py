#!/usr/bin/env pyhton
from csv import DictWriter
from gmusicapi import Mobileclient
from operator import itemgetter


def login():
    logged_in = api.login('account@gmail.com', 'password')
        # IMPORTANT: If you use secondary authentication for gogle music
        # you need to generate an app specific password!
    return logged_in

def songList():
    global count
    tempList = api.get_all_songs()
    for x in range(len(tempList)):
        gatherList = {
            "album":    tempList[x].get('album').encode('utf-8'),
            "artist":    tempList[x].get('artist').encode('utf-8'),
            "name":    tempList[x].get('title').encode('utf-8'),
            "trackNumber":    tempList[x].get('trackNumber')
            }
        count += 1
        content.append(gatherList)
    return content

def writeToFile():
    temp = sorted(content, key=itemgetter('trackNumber'))
    temp = sorted(temp, key=itemgetter('album'))
    temp = sorted(temp, key=itemgetter('artist'))
    with open('musiclibrary.csv','w') as outfile:
        # outfile.write(u'\ufeff'.encode('utf-8'))
        writer = DictWriter(outfile, ('artist','album','trackNumber','name'))
        writer.writeheader()
        writer.writerows(temp)

#GLOBAL VARS
api = Mobileclient()
content = []
count = 0

def main():
    print 'Logging in...'
    newObj = login()
    if newObj == False:
        print "Login Failed. Check credintials!"
    else:
        print 'Logged in.'
    songList()
    writeToFile()
    print count


if __name__ == '__main__':
    main()