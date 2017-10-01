#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""
bat

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

# constants
AC   = '/sys/class/power_supply/AC'
BAT0 = '/sys/class/power_supply/BAT0'
BAT1 = '/sys/class/power_supply/BAT1'

# get battery charge amounts
f = open(os.path.join(BAT0, 'energy_full'), 'r')
bat0Max = f.readline()
f.close()

f = open(os.path.join(BAT0, 'energy_now'), 'r')
bat0 = f.readline()
f.close()

f = open(os.path.join(BAT1, 'charge_full'), 'r')
bat1Max = f.readline()
f.close()

f = open(os.path.join(BAT1, 'charge_now'), 'r')
bat1 = f.readline()
f.close()

f = open(os.path.join(AC, 'online'), 'r')
ac = f.readline()
f.close()

# convert ac to boolean
if (int(ac) == 0):
    ac = False
else:
    ac = True

# convert to percent

bat0Percent = (int(bat0) / int(bat0Max)) * 100
bat1Percent = (int(bat1) / int(bat1Max)) * 100

batPercent = (bat0Percent + bat1Percent) / 2

# printing prefix

prefix = '?'
if (ac == True):
    prefix = '' # charging symbol
else:
    if (int(batPercent) <= 33):
        prefix = '' # empty battery symbol
    elif (int(batPercent) > 33 and int(batPercent) <= 66):
        prefix = '' # low battery symbol
    if (int(batPercent) > 66):
        prefix = '' # full battery symbol

print(" " + prefix + " " + str(int(batPercent)))
