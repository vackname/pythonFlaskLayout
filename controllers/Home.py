import config
@config.app.route('/')
def WuIndex():
    return config.render_template('home/index.html',title="數位大學")