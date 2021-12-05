from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\Users\vinic\PycharmProjects\pythonProject\BrunoSilvaFelix-p7info-poo\atividade-avaliação\Avaliação_06\notaFiscal.db'
app.debug = True

db = SQLAlchemy(app)
