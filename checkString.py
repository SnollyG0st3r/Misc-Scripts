#!/usr/bin/python
# Checks a memory address for any bad characters specified in badChars.txt
# Usage: ./checkAddress.py memory_address
#  ex. ./checkAddress.py 0x6d37370e

import sys,re

if len(sys.argv) < 2:
    print "Usage: %s address" % sys.argv[0]
    sys.exit(1)

checkString = sys.argv[1]
isBad = 0
badChars = []
arrayString = []
x = 0
y = 2

# Split the address string into 2 characters and add each pair to array
while x < (len(checkString) - 1):
    newString = checkString[x:y]
    arrayString.append(newString)    
    x += 2
    y += 2
            
for entry in arrayString:
    badFile = open("badChars.txt", "r")
    for line in badFile:
        if re.search(entry, line, re.IGNORECASE):
            print "Bad character found: %s" % entry
            isBad = 1
            badChars.append(entry)
    badFile.close()

if isBad == 0:
    print "No bad characters found!"
else:
    print "Bad characters found: %s" % badChars
