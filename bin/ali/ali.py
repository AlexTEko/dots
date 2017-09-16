#!/usr/bin/env python

#----------------------------------#
# ,--. ,--.         ,--.           #
# |  .'   / ,---. ,-'  '-. ,--,--. #
# |  .   ' | .-. |'-.  .-'' ,-.  | #
# |  |\   \' '-' '  |  |  \ '-'  | #
# `--' '--' `---'   `--'   `--`--' #
#            kotajacob.tk          #
# Copyright (C) 2017  Dakota Walsh #
#----------------------------------#

import os

# Open the config file - this is where I keep my alias's
f = open(os.path.expanduser('~/.zshrc'), 'r')

raw_file = f.readlines()
for line in raw_file:
    if line[:5] == "alias":
        print (line[:len(line)-1])

f.close()
