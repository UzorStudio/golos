
import requests
from bs4 import BeautifulSoup
from collections import Counter
import random
import basa
import subprocess

db = basa.Base("localhost")

def yandexq(text):
    url = "https://yandex.ru/q/search/answers/?text="+text
    answermass = []

    headers = {
            'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0'}
    q = requests.get(url, headers=headers)
    soup = BeautifulSoup(q.text, 'lxml')
    linkToCoin = soup.find_all('div', class_="formatted")
    print(soup)

    for l in linkToCoin:
        answermass.append(l.find("p").text)

    return answermass




def tallk(qustuin, answers):
    qus = qustuin.split(" ")
    ans = []

    for q in qus:
        if db.loadFrace(q) != None:
            ans.append(db.loadFrace(q)["answer"])
        else:
            pass
    if len(ans) > 1:
        c = Counter(ans)
        return min(c)
    else:
        saveAnswersAndQuastions(random.choice(answers),qustuin)


def saveAnswersAndQuastions(answr,qstions):
    qstions = qstions.split(" ")
    for q in qstions:
        db.saveFrase(q,answr)

def randomFrace():
    url = "http://text-box.ru/phrases/random.html"

    frace = []

    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0'}
    q = requests.get(url, headers=headers)
    soup = BeautifulSoup(q.text, 'lxml')
    linkToCoin = soup.find_all('div', class_="text__line__content__rus text__line--cell")
    #print(soup)

    for l in linkToCoin:
        frace.append(l.text)

    #print(answermass)

    return random.choice(frace)

#http://text-box.ru
#unable to connect to server: fe_sendauth
print(randomFrace())
#a = subprocess.run("ls",capture_output=True).stdout.decode()
#print(a.split())
#qst = "ты знаешь рейгана"
#s = yandexq(qst)
#print(s)
#
#print(tallk(qustuin=qst,answers=s))





#def say(txt):
#    engine = pyttsx3.init()
#
#    voices = engine.getProperty('voices')
#
#    for voice in voices:
#        print('=======')
#
#        print('Имя: %s' % voice.name)
#
#        print('ID: %s' % voice.id)
#
#        print('Язык(и): %s' % voice.languages)
#
#        print('Пол: %s' % voice.gender)
#
#        print('Возраст: %s' % voice.age)
#
#    engine.setProperty('voice', "russian")
#    engine.setProperty('volume', 0.6)
#    engine.setProperty('rate', 100)
#
#    engine.say(txt)
#    engine.runAndWait()
#
#say("пидарас")