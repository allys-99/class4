#!/usr/bin/env python

import os

def hwPart1():

    myfilename="housing.data.txt"
    print("  ~  ~  ~ Part 1  ~  ~  ~")
    open('part1.txt', 'w').close()
    with open(myfilename, 'r') as file_handle:
        for line in file_handle.readlines():
            line_clean = line.replace('   ',' ').replace('  ',' ' )
            line_clean =line_clean.strip()
            values = line_clean.split(" ")
            print()
            print ("  ", end="")
            for value in values:
                if '.' not in value:
                    print(int(value), end="  ")
                else:
                    print (float(value), end="  ")
                with open("part1.txt", "a") as f2:
                    f2.write('{:>10}'.format(value))
            with open("part1.txt", "a") as f2:
                f2.write("\n")


def hwPart5():
    myfilename="housing.data.txt"
    retLine=""
    newlist = []
    print("\n  ~  ~  ~ Part 5  ~  ~  ~")
    open('part5.txt', 'w').close()
    with open(myfilename, 'r') as file_handle:
        for line in  file_handle.readlines():
            line_clean = line.replace('   ',' ').replace('  ',' ' )
            line_clean =line_clean.strip()
            values = line_clean.split(" ")
            newlist.append(values)
    listTranspose = [[row[i] for row in newlist] for i in range( len(newlist[0])  )   ]
    for idx, value in enumerate(listTranspose):
        PrintNice(value)
        #print("\n")

def PrintNice(alist):
    f5=open("part5.txt","a")
    for value in alist:
        if '.' not in value:
            print(int(value), end="  ")
        else:
            print(float(value), end=" ")
        f5.write('{:>10}'.format(value))
    f5.write("\n")
    print("\n",end=" ")

#print ("  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  M A I N  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~ ")
hwPart1()
hwPart5()



