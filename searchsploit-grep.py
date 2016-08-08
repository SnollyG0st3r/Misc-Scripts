#!/usr/bin/python
import sys
import os
import re
x = 0

winRemote = ["/usr/share/exploitdb/platforms/windows/remote","/usr/share/exploitdb/platforms/win32/remote"] 
winLocal = ["/usr/share/exploitdb/platforms/windows/local","/usr/share/exploitdb/platforms/win32/local"]
winWebApps = ["/usr/share/exploitdb/platforms/windows/webapps","/usr/share/exploitdb/platforms/win32/webapps"]
linuxRemote = ["/usr/share/exploitdb/platforms/linux/remote","/usr/share/exploitdb/platforms/lin_x86/remote","/usr/share/exploitdb/platforms/unix/remote"]
linuxLocal = ["/usr/share/exploitdb/platforms/linux/local","/usr/share/exploitdb/platforms/lin_x86/local","/usr/share/exploitdb/platforms/unix/local"]
linuxWebApps = ["/usr/share/exploitdb/platforms/linux/webapps","/usr/share/exploitdb/platforms/lin_x86/webapps"]
multipleWebApps = ["/usr/share/exploitdb/platforms/multiple/webapps","/usr/share/exploitdb/platforms/php/webapps","/usr/share/exploitdb/platforms/perl/webapps","/usr/share/exploitdb/platforms/jsp/webapps","/usr/share/exploitdb/platforms/cgi/webapps","/usr/share/exploitdb/platforms/asp/webapps","/usr/share/exploitdb/platforms/python/webapps","/usr/share/exploitdb/platforms/xml/webapps","/usr/share/exploitdb/platforms/cfm/webapps"]
while x == 0:
	print "Selection: "
	print "1.  Windows Remote"
	print "2.  Windows Local"
	print "3.  Windows Web Apps"
	print "4.  Linux Remote"
	print "5.  Linux Local"
	print "6.  Linux Web Apps"
	print "7.  Multiple Web Apps (php,perl,python,jsp,etc..)"
	print "99. Exit"
	exploitType = raw_input("Selection: ")

	if exploitType == "1":
	    targetOS = winRemote
	elif exploitType == "2":
	    targetOS = winLocal
	elif exploitType == "3":
	    targetOS = winWebApps
	elif exploitType == "4":
	    targetOS = linuxRemote
	elif exploitType == "5":
	    targetOS = linuxLocal
	elif exploitType == "6":
	    targetOS = linuxWebApps
	elif exploitType == "7":
	    targetOS = multipleWebApps
	elif exploitType == "99":
	    sys.exit()
	searchPhrase = raw_input("Search phrase: ")

	for searchPath in targetOS:    
	  for filename in os.listdir(searchPath):
	    currentFile = os.path.join(searchPath, filename)
	    searchfile = open(currentFile, "r")
	    for line in searchfile:
		if re.search(searchPhrase, line, re.IGNORECASE):
		    print currentFile + "\n  " + line
	    searchfile.close()
