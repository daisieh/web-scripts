import flask
import sys
import os
import urllib
from time import strftime, time

app = flask.Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if path == 'pyMesquiteFeedback':
        feedback()
        return flask.render_template('feedback.html')
    elif path == 'pyMesquiteFeedbackPrerelease:':
        feedback(prerelease=True)
        return flask.render_template('feedback.html')
    elif path == 'pyMesquiteStartup':
        startup()
    elif path == 'pyMesquiteBeans':
        beans()
    else:
        return flask.redirect('https://mesquiteproject.github.io')

def feedback(prerelease=False):
    if prerelease:
        filename = "feedbackPrerelease"
    else:
        filename = "feedback"
    
    ##############################################################################
    # Option A - single log file
    ##############################################################################
    # if you want one single file use this block
    
    feedbackfile = "error_" + filename + ".log"
    ##############################################################################

    ##############################################################################
    # Option B - multiple log files
    ##############################################################################
    # if you want one file for each postback use this block
    #feedbackfile = '/data/feedback/' + filename + time() + '.log'
    ##############################################################################

    FILE = open(feedbackfile, "a")

    ip = flask.request.remote_addr

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

def startup():
#<Request 'https://mesquiteproject.herokuapp.com/pyMesquiteStartup?build=	PreRelease-875	OS+%3D	Mac+OS+X	10.11.6	java+%3D	1.8.0_111	Oracle+Corporation' [GET]>
    
    ip = flask.request.remote_addr
    raw = flask.request.query_string.decode("utf-8")

    # the file we'll be appending version information to 
    feedbackfile = "version_feedback.log"

#     open the file w/ appending mode 
    FILE = open(feedbackfile, "a")

#     print the start of the line with current time
    FILE.write('[%s] - ' % strftime("%Y-%m-%d %H:%M:%S"))
    FILE.write('ip = \t%s' % (ip))
    FILE.write('\t')
           
#     split the query string by the value delimiter, &. 
    vallist = raw.split('&')

#     for each value in the query string, print it after the line start           
    for k in vallist:
        tuple = k.split('=')
        FILE.write('%s = %s, ' % (tuple[0], urllib.unquote_plus(tuple[1])))
    
#     terminate the line     
    FILE.write('\n')

#     flush and close 
    FILE.flush()
    FILE.close()
    return flask.render_template('startup.html')

def beans():
    ip = flask.request.remote_addr
    raw = flask.request.query_string.decode("utf-8")
                
    # the file we'll be appending version information to 
    beanlogfile = "beans.log"

    # open the file w/ appending mode 
    FILE = open(beanlogfile, "a")

    # split the query string by the value delimiter, &. 
    vallist = raw.split('&')

    # print the start of the line with current time
    FILE.write('[%s] - ' % strftime("%Y-%m-%d %H:%M:%S"))
    FILE.write('ip = \t%s' % (ip))
    FILE.write('\t')
           
    # for each value in the query string, print it after the line start           
    for k in vallist:
        FILE.write('%s' % (k))
        FILE.write('\t')
    
    # terminate the line     
    FILE.write('\n')

    # flush and close 
    FILE.flush()
    FILE.close()
    return flask.render_template('beans.html')
