import requests
import json
import random
import html
import time


languages = [
    "af","am","ar","az","be","bg","bn","bs","ca","ceb","cs","cy","da","de","el","en","eo","es","et","eu","fa","fi","fr","fy","ga","gd","gl","gu","ha","haw","hi","hmn","hr","ht","hu","hy","id","ig","is","it","iw","ja","jw","ka","kk","km","kn","ko","ku","ky","la","lb","lo","lt","lv","mg","mi","mk","ml","mn","mr","ms","mt","mww","my","ne","nl","no","ny","pa","pl","ps","pt","ro","ru","sd","si","sk","sl","sm","sn","so","sq","sr","sr-La","st","su","sv","sw","ta","te","tg","th","tl","tlh","tr","uk","ur","uz","vi","xh","yi","yo","yua","zh","zh-TW","zu"
]


def translate(text, src="en", dest="zh-TW"):
    session = requests.session()
    url = "https://www.translate.com/translator/ajax_translate"
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 OPR/48.0.2685.39"}
    data = {"text_to_translate": text,
              "source_lang": src,
              "translated_lang": dest,
              "use_cache_only": "false"}
    page = session.post(url,data=data,headers=headers)
    j = json.loads(page.text)
    if j["translation_id"] != 0:
        return html.unescape(j["translated_text"]).encode('utf-8')


def scatterify(text,p=False):
    lang1 = random.choice(languages)
    lang2 = random.choice(languages)

    text = translate(text, "en", lang1)
    if p: print('en - %s' % lang1, text)
    if text is not None:
        text = translate(text, lang1, lang2)
        if p: print('%s - %s' % (lang1, lang2), text)
        if text is not None:
            text = translate(text, lang2, "en")
    return text


def befuddle(text,p=False):
    if isinstance(text,str):
        text = text.encode()
    new = scatterify(text,p)
    if new is None:
        new = text
    return new


def save_text(text,br=False):
    if isinstance(text,bytes):
        text = text.decode()
    with open("saved.txt","a") as f:
        if br:
            f.write("\n")
        f.write(text+"\n")


def go_again():
    text = input("text to befuddle: ")

    if SAVETEXT:
        save_text(text, True)
    print(text)

    while True:
        text = befuddle(text)
        if SAVETEXT:
            save_text(text)
        print(text.decode())
        again = input("Would you like to befuddle more text? yes/no: ")
        if again == "yes":
            go_again()
        else:
            quit()


SAVETEXT = False

go_again()




