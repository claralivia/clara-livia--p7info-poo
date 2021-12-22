from flask import Flask
from flask_sqlalchemy import SQLAlchemy

tela = Flask(__name__)
tela.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
tela.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./notafiscalbd.db'
tela.debug = True

bancodados = SQLAlchemy(tela)