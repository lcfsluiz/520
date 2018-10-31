from pymongo import MongoClient
from pprint import pprint


try:

    con = MongoClient()
    db = con['projeto']
except Exception as e:
    print('Erro: {}'.format(e))

db.usuarios.update({"_id": 1}, {"$set":{"sobrenome"}})


db.usuarios.insert({'_id': 5, 'nome':teste, 'sobrenome':santos})



#usuarios = []
#for usuario in db.usuarios.find():
#    usuarios.append(usuario)

#print(usuarios)