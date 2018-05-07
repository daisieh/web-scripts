#!/usr/bin/python
import sys
import os
import urllib 
from time import strftime, time

# browsers will get angry if we don't give them something in return
print "Content-Type: text/html"
print
print "<html>"
print "<head><title>Mesquite Version Feedback</title></head>"
print "Mesquite sent your Mesquite version number, operating system version and Java version to its server to record version usage.  No other information was sent. "

# all the server values are available to us in os.environ 
for k in os.environ.items():
            if "QUERY_STRING" in k:             # find the query string containing GET data
                raw = k[1]                      # save query string data from GET data
            elif "REMOTE_ADDR" in k:            # save the IP address of the request
                ip = k[1]
                
# the file we'll be appending version information to 
feedbackfile = "/Library/WebServer/mesquite_logs/version_feedback.log"

# open the file w/ appending mode 
FILE = open(feedbackfile, "a")

# split the query string by the value delimiter, &. 
vallist = raw.split('&')

# print the start of the line with current time
FILE.write('[%s] - ' % strftime("%Y-%m-%d %H:%M:%S"))
FILE.write('ip = \t%s' % (ip))
FILE.write('\t')
           
# for each value in the query string, print it after the line start           
for k in vallist:
    tuple = k.split('=')
    FILE.write('%s = %s, ' % (tuple[0], urllib.unquote_plus(tuple[1])))
    
# terminate the line     
FILE.write('\n')

# flush and close 
FILE.flush()
FILE.close()

print "</html>"
