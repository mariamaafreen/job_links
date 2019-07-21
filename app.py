from flask import Flask, render_template
import os



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
class Jobs(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    company_name=db.Column(db.String(100))
    job_description=db.Column(db.String(100000))
    links=db.Column(db.String(200))



@app.route('/')
def home():
    c = Jobs.query.all()
    

    return render_template('view.html', datas = c)


if __name__ =='__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)

