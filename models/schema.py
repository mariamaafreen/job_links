from db import db


class Jobs(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    company_name=db.Column(db.String(100))
    job_description=db.Column(db.String(100000))
    links=db.Column(db.String(200))