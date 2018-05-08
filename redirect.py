import flask
from werkzeug.utils import secure_filename

app = flask.Flask(__name__)

@app.route('/')
def homepage():
    return 'To validate a file, send a POST request with the file as "multipart/form-data" to https://validatemyfile.herokuapp.com/validate. You can do this with curl from the command line: curl https://validatemyfile.herokuapp.com/validate  -F "file=@test.fasta"'

@app.route('/pyMesquiteFeedback', methods=['POST'])
def feedback():
#     if flask.request.method == 'POST':
    app.logger.info('%s', flask.request)
    return flask.render_template('error.html', error=flask.request)

@app.route('/pyMesquiteStartup', methods=['POST', 'GET'])
def feedback():
#     if flask.request.method == 'POST':
    app.logger.info('%s', flask.request)
    return flask.render_template('error.html', error=flask.request)

@app.route('/pyMesquiteBeans', methods=['POST', 'GET'])
def feedback():
#     if flask.request.method == 'POST':
    app.logger.info('%s', flask.request)
    return flask.render_template('error.html', error=flask.request)
