from app import app

@app.route('/index')
def index():
    return 'It works!'