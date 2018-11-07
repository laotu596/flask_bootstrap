from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)



#@app.route('/')
#def hello_world():
#    return 'Hello World!'

@app.route('/bootstrap/<name>')
def bootstrap(name):
    return render_template('bootstrap.html', name = name)

if __name__ == '__main__':
    app.run()

@app.route('/moment/')
def momenttemplate():
    return render_template('moment.html',current_time = datetime.utcnow())
