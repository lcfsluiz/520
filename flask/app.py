from flask import Flask, jsonify, render_template
from pymongo import MongoClient


import requests

con = MongoClient()
db = con['projeto']

app = Flask(__name__)

@pp.route('/')
def index():
    mensagem = {'mensagem': " minha primeira api rest"}
    return jsonify(mensagem)

@pp.route('/usuarios')
def usuarios():
    usuarios = []
    for x in db.usuarios.find():
        usuarios.append(x)
    return jsonify(usuarios)


if __name__ == '__main__':
    aap.run(host='0.0.0.0', port=5000, debug=True)