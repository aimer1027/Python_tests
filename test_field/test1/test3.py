#!/usr/bin/python

import sys

try:
   # open file stream
   file = open(file_name,"w")
except IOError:
   print "There was an error writting to", file_name
   sys.exit()
print "Enter '", file_finish,
print "' When finished"
while file_text != file_finish: 
   file_text = raw_input("Enter text:")
   if file_text == file_finish :
        # close the file
	file.close
	break
   file.write(file_test)
   file.write('\n')
file.close()
file_name = raw_input("Enter filename:")
if len(file_name) == 0:
   print "Next time please enter something"
   sys.exit()
file_text = file.read()
file.close()
print file_text
