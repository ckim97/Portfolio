from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, ForeignKey
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.sql import func
from datetime import datetime


# Definitions of tables and associated schema constructs
metadata = MetaData()

# A Flask SQLAlchemy extension
db = SQLAlchemy(metadata=metadata)

class Projects(db.Model, SerializerMixin):
    __tablename__ = 'projects_table'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    link = db.Column(db.String)
    description = db.Column(db.String)
    stack = db.Column(db.String)