from flask import Flask, render_template
import os
from models.schema import *



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


@app.route('/')
def home():
    c = Jobs.query.all()
    

    return render_template('view.html', datas = c)


if __name__ =='__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)

