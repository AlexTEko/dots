#!/usr/bin/env python3
"""
bright

========================================
oooo    oooo               .            
`888   .8P'              .o8            
 888  d8'     .ooooo.  .o888oo  .oooo.  
 88888[      d88' `88b   888   `P  )88b 
 888`88b.    888   888   888    .oP"888 
 888  `88b.  888   888   888 . d8(  888 
o888o  o888o `Y8bod8P'   "888" `Y888""8o
               @nilsu.org               
=== Copyright (C) 2017  Dakota Walsh ===
"""

# imports
import os
import argparse

# constants
MAX     = '/sys/class/backlight/intel_backlight/max_brightness'
CURRENT = '/sys/class/backlight/intel_backlight/brightness'

def getMaxBright():
    f = open(MAX, 'r')
    maxBright = f.readline()
    f.close()

    maxBright = int(maxBright)
    return(maxBright)

def getCurrentBright():
    f = open(CURRENT, 'r')
    currentBright = f.readline()
    f.close()

    currentBright = int(currentBright)
    return(currentBright)

def getBright():
    percentBright = (getCurrentBright() / getMaxBright()) * 100
    return(percentBright)

def setBright(setAmount):
    maxBright = getMaxBright()
    if (setAmount <= 100):
        setAmount = setAmount / 100
        newBright = maxBright * setAmount

        f = open(CURRENT, 'w')
        f.write(str(int(newBright)))
        f.close()
    else:
        sys.exit("Enter a value between 0-100 dammit")

def addBright(addAmount):
    maxBright = getMaxBright()
    currentBright = getCurrentBright()
    addAmount = (currentBright / maxBright) * addAmount * 100

    if (((addAmount + currentBright) <= maxBright) and ((addAmount + currentBright) > 0)):
        newBright = addAmount + currentBright
    elif ((addAmount + currentBright) > maxBright):
        newBright = 100
    else:
        newBright = 0

    f = open(CURRENT, 'w')
    f.write(str(int(newBright)))
    f.close()

def getArgs():
    # get the passed arguments
    description = "bright"
    arg = argparse.ArgumentParser(description=description)

    arg.add_argument("-g", action="store_true",
            help="Get current brightness percent")

    arg.add_argument("-s",
            help="Set current brightness percent")

    arg.add_argument("-a",
            help="Add to current brightness percent")

    return arg.parse_args()

def main():
    # get the arguments
    arguments = getArgs()

    if arguments.g:
        # print the current brightness as a percent
        print(getBright())

    if arguments.s:
        # set the current brightness as a percent
        setAmount = arguments.s
        setBright(int(setAmount))

    if arguments.a:
        # add to the current brightness as a percent
        addAmount = arguments.a
        addBright(int(addAmount))

if __name__ == '__main__':
    main()
