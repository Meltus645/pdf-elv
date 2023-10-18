from app.utils.dbconf import db
from sqlalchemy import Column, VARCHAR, INT

class User(db.Model):
    id =Column(INT, primary_key =True, autoincrement=True)
    username =Column(VARCHAR)
    email =Column(VARCHAR)
    phnnumber =Column(VARCHAR)
    hcdu =Column(VARCHAR)
    password =Column(VARCHAR)