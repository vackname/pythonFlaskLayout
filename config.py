from flask import Flask, render_template
app = Flask(__name__,
static_folder='./wwwroot/lib',static_url_path='/sclib')

class fillterMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        #阻斷 middleWare
        if(True):
            return self.app(environ, start_response)
        else:
            return None

#阻斷通道
#app.wsgi_app = fillterMiddleware(app.wsgi_app)

import os
#根目錄
rootPath = os.path.dirname(__file__)