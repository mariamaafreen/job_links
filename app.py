#from flask import Flask, render_template
#from flask_sqlalchemy import SQLAlchemy
#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:minu2010@localhost/job'
#db = SQLAlchemy(app)

#class Link(db.Model):
#    Sno = db.Column(db.Integer, promary_key=True)
 #   Companyname = db.Column(db.String(100))
  #  JobDescription = db.Column(db.String(10000))
   # JobLink = db.Column(db.String(200))


#@app.route('/')
#def home():
   #c = conn.execute("select * from job")

    #return render_template('view.html', datas = c.fetchall())

#if __name__ =="__main__":
 #   app.run(debug=True)







from flask import Flask, render_template
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(
            host = "localhost",
            database = "job",
            user = "postgres",
            password = "minu")


@app.route('/')
def home():
    c = conn.cursor()
    c.execute("select * from jobs")

    return render_template('view.html', datas = c.fetchall())

if __name__ =='__main__':
    app.run(debug=True)
