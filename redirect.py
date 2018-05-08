import flask
from werkzeug.utils import secure_filename

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
#     if flask.request.method == 'POST':
    app.logger.error('%s', flask.request)
    return flask.render_template('error.html', error=flask.request)

@app.route('/pyMesquiteBeans', methods=['POST', 'GET'])
def beans():
#     if flask.request.method == 'POST':
    app.logger.info('%s', flask.request)
    return flask.render_template('error.html', error=flask.request)
