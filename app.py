from flask import Flask, request, render_template, make_response
from flask_bootstrap import Bootstrap

import os
import uuid
import base64

from PIL import Image
import warnings
warnings.simplefilter('error', Image.DecompressionBombWarning)

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def do_get():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()