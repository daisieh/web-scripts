import flask
from werkzeug.utils import secure_filename
import sys
import os
import urllib
from time import strftime, time

app = flask.Flask(__name__)

@app.route('/')
def homepage():
    return 'To validate a file, send a POST request with the file as "multipart/form-data" to https://validatemyfile.herokuapp.com/validate. You can do this with curl from the command line: curl https://validatemyfile.herokuapp.com/validate  -F "file=@test.fasta"'

@app.route('/pyMesquiteFeedback', methods=['POST', 'GET'])
def feedback():
#     if flask.request.method == 'POST':
    app.logger.error('%s', flask.request)
    return flask.render_template('error.html', error=flask.request)

@app.route('/pyMesquiteStartup', methods=['POST', 'GET'])
def startup():
#<Request 'https://mesquiteproject.herokuapp.com/pyMesquiteStartup?build=	PreRelease-875	OS+%3D	Mac+OS+X	10.11.6	java+%3D	1.8.0_111	Oracle+Corporation' [GET]>
    
    ip = flask.request.remote_addr
    raw = flask.request.query_string.decode("utf-8")
    app.logger.error('%s', raw)

    # the file we'll be appending version information to 
    feedbackfile = "version_feedback.log"

#     open the file w/ appending mode 
    FILE = open(feedbackfile, "a")

#     print the start of the line with current time
    FILE.write('[%s] - ' % strftime("%Y-%m-%d %H:%M:%S"))
    FILE.write('ip = \t%s' % (ip))
    FILE.write('\t')
           
#     split the query string by the value delimiter, &. 
    vallist = urllib.parse.parse_qs(raw)

#     for each value in the query string, print it after the line start           
    for key, value in vallist.items():
        FILE.write('%s = %s, ' % (key, value))

#     terminate the line     
    FILE.write('\n')

#     flush and close 
    FILE.flush()
    FILE.close()
    return flask.render_template('startup.html')

@app.route('/pyMesquiteBeans', methods=['POST', 'GET'])
def beans():
#     if flask.request.method == 'POST':
    app.logger.info('%s', flask.request)
    return flask.render_template('error.html', error=flask.request)
