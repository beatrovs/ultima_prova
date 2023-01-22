from pymongo import MongoClient

def obter_colecao_mongodb(url_conexao, colecao):
    conex = MongoClient(url_conexao)
    db = conex[colecao]
    