import requests
import json
import random
import html
import time
import argparse


languages = [
    "af","am","ar","az","be","bg","bn","bs","ca","ceb","cs","cy","da","de","el","en","eo","es","et","eu","fa","fi","fr","fy","ga","gd","gl","gu","ha","haw","hi","hmn","hr","ht","hu","hy","id","ig","is","it","iw","ja","jw","ka","kk","km","kn","ko","ku","ky","la","lb","lo","lt","lv","mg","mi","mk","ml","mn","mr","ms","mt","mww","my","ne","nl","no","ny","pa","pl","ps","pt","ro","ru","sd","si","sk","sl","sm","sn","so","sq","sr","sr-La","st","su","sv","sw","ta","te","tg","th","tl","tlh","tr","uk","ur","uz","vi","xh","yi","yo","yua","zh","zh-TW","zu"
]


def translate(text, src="en", dest="zh-TW"):
    session = requests.session()
    url = "https://www.translate.com/translator/ajax_translate"
    headers = {"user-agent": "Mozilla/5.0"}
    data = {"text_to_translate": text,
              "source_lang": src,
              "translated_lang": dest,
              "use_cache_only": "false"}
    page = session.post(url,data=data,headers=headers)
    j = json.loads(page.text)
    if j["translation_id"] != 0:
        return html.unescape(j["translated_text"]).encode('utf-8')


def scatterify(text,verbose=False):
    lang1 = random.choice(languages)
    lang2 = random.choice(languages)

    text = translate(text, "en", lang1)
    if verbose: print('en - %s' % lang1, text)
    if text is not None:
        text = translate(text, lang1, lang2)
        if verbose: print('%s - %s' % (lang1, lang2), text)
        if text is not None:
            text = translate(text, lang2, "en")
    return text


def befuddle(text,verbose=False):
    if isinstance(text,str):
        text = text.encode()
    new = scatterify(text,verbose)
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


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("text", nargs='+', help="text to befuddle")
    parser.add_argument("-n", dest="n", default=1, type=int, help="number of befuddlements to perform")
    parser.add_argument("--no-save", dest="nosave", action="store_true", help="Do not save output")

    args = parser.parse_args()

    text = ' '.join(args.text)
    print(text)
    if not args.nosave:
        save_text(text, True)

    for i in range(args.n):
        text = befuddle(text)
        print(text.decode())
        if not args.nosave:
            save_text(text)


