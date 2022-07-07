import pymongo
from bson import ObjectId

class Base():
    def __init__(self,classterMongo):
        self.classterMongo = classterMongo
        self.classter = pymongo.MongoClient(self.classterMongo)


    def saveFrase(self,askWord,answer):
        db = self.classter["Adam"]
        Frase = db["Frase"]

        post = {"askWord":askWord,
                "answer":answer
                }

        Frase.insert_one(post)

    def loadFrace(self,askWord):
        db = self.classter["Adam"]
        Frase = db["Frase"]

        return Frase.find_one({"askWord":askWord})