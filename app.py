from flask import Flask, render_template
from sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
db.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
class Jobs(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    company_name=db.Column(db.String(100))
    job_description=db.Column(db.String(100000))
    links=db.Column(db.String(200))



@app.route('/')
def home():
    c = jobs.query.all()
    

    return render_template('view.html', datas = c)

if __name__ =='__main__':
    app.run(debug=True)
