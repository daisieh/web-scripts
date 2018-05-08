from flask import Flask
from flask import request
from flask import make_response
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'To validate a file, send a POST request with the file as "multipart/form-data" to https://validatemyfile.herokuapp.com/validate. You can do this with curl from the command line: curl https://validatemyfile.herokuapp.com/validate  -F "file=@test.fasta"'

@app.route('/pyMesquiteFeedback', methods=['POST'])
def feedback():
    if request.method == 'POST':
        print(request)
        return request
