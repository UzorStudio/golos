import pymongo
from bson import ObjectId
from vosk import Model, KaldiRecognizer
import os
import webbrowser




class Adam():
    def __init__(self,db):
        self.db = db

        self.globalperm = {"listen":False,"memory":""}

    def neiro(self,lists):
        if "адам" in lists:
            self.globalperm["listen"] = True
            indexz = (lists.index("адам"))

            del lists[0:indexz + 1]

        if self.globalperm["listen"]:

            if "открой" in lists:
                if "текстовый" in lists:
                    os.system("gedit &")
                if "терминал" in lists:
                    os.system("gnome-terminal")
            if "выключи" in lists or "закрой" in lists:
                if "текстовый" in lists:
                    os.system("pkill gedit")
                if "компьютер" in lists:
                    os.system("poweroff")
                if "браузер" in lists:
                    os.system("pkill firefox")
                if "терминал" in lists:
                    os.system("pkill gnome-terminal")
            if "напомни" in lists:
                lists.remove("напомни")
                file = open("memory.json","w")
                file.write(" ".join(lists))
                file.close()
            if "найди" in lists:
                lists.remove("найди")
                webbrowser.open('https://yandex.ru/search/?lr=213&text=' + " ".join(lists), new=1)
            if "не" in lists and "слушай" in lists:
                self.globalperm["listen"] = False
            else:
                answer = []
                for l in lists:
                    answer.append(self.db.loadFrace(l)["answer"])
                print(answer)

    def getListen(self):
        return self.globalperm["listen"]

    def setListen(self,how):
        self.globalperm["listen"] = how


