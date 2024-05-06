from flask import Flask, make_response, jsonify, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import datetime
from models import db, Projects
from flask_cors import CORS

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False
CORS(app, resources={r"/*": {"origins": "*"}})

migrate = Migrate(app, db)

db.init_app(app)

#Projects
@app.get("/projects")
def get_projects():
    projects = Projects.query.all()
    return [p.to_dict() for p in projects]

if __name__ == "__main__":
    app.run(port=5555, debug=True)