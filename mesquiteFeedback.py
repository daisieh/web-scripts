#!/usr/bin/python
import sys
import os
import urllib 
from time import strftime, time

print "Content-Type: text/html"
print
print "<html>"
print "<head><title>Mesquite System Feedback</title></head>"
print "Thank you. "

##############################################################################
# Option A - single log file
##############################################################################
# if you want one single file use this block
feedbackfile = "/Library/WebServer/mesquite_logs/error_feedback.log"

FILE = open(feedbackfile, "a")
##############################################################################

##############################################################################
# Option B - multiple log files
##############################################################################
# if you want one file for each postback use this block
#feedbackdir = "/data/feedback/"
#filename = 'feedback%s.log' % (time())

#FILE = open(feedbackdir+filename, "w")
##############################################################################

# all the server values are available to us in os.environ 
for k in os.environ.items():
            if "REMOTE_ADDR" in k:            # save the IP address of the request
                ip = k[1]

raw = sys.stdin.readline()
    
vallist = raw.split('&')

banner = '#' * 80

FILE.write('\n' + banner + '\n')
FILE.write('local time is: %s\n' % (strftime("%Y-%m-%d %H:%M:%S")))

line = '-' * 80
FILE.write(line + '\n')
FILE.write(' ip: %s\n' % (ip))
FILE.write(line + '\n')
FILE.write(' body: \n')
FILE.write(line + '\n')

for k in vallist:
    tuple = k.split('=')
    value_str = urllib.unquote_plus(tuple[1])
    lines = value_str.split('\\n')
    value_str = '%s' % ''.join(['%s\n\t' % (line) for line in lines])
    FILE.write('%s = %s\n' % (tuple[0], value_str))

FILE.write(banner + '\n')
    
FILE.flush()
FILE.close()

print "</html>"



        

