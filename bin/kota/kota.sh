#!/usr/bin/bash
#
# ANSI color scheme script featuring Space Invaders
#
# Original: http://crunchbang.org/forums/viewtopic.php?pid=126921%23p126921#p126921
# Modified by lolilolicon
#

f=3 b=4
for j in f b; do
  for i in {0..7}; do
    printf -v $j$i %b "\e[${!j}${i}m"
  done
done
bld=$'\e[1m'
rst=$'\e[0m'

cat << EOF

oooo    oooo               .            
`888   .8P'              .o8            
 888  d8'     .ooooo.  .o888oo  .oooo.  
 88888[      d88' `88b   888   `P  )88b 
 888`88b.    888   888   888    .oP"888 
 888  `88b.  888   888   888 . d8(  888 
o888o  o888o `Y8bod8P'   "888" `Y888""8o

nilsu.org
Copyright (C) 2017  Dakota Walsh
EOF
