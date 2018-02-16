import telepot
import json
import datetime
import os
from telepot.loop import MessageLoop
from newsapi import NewsApiClient


def listen(msg):
    *_, chat_id = telepot.glance(msg)
    content = msg['text']
    proccess(chat_id, content)

def proccess(chat_id, content):
    if content == "hello":
        content = "Hello, how are you?"
    elif content == "/start":
        content = "Hello, how are you?"
    elif content == "news":
        content = "News Delivered :)"
        news(chat_id)
    else:
        content = "Sorry, I do not understand."
    sendMsg(chat_id, content)   

def news(chat_id):
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    newsapi = NewsApiClient(api_key=(os.environ['newsapikey']))
    content = newsapi.get_everything(q='news'
                                        ,sources='bbc-news,the-verge'
                                        ,domains='bbc.co.uk,techcrunch.com'
                                        ,from_parameter=date
                                        ,to=date
                                        ,language='en'
                                        ,sort_by='relevancy'
                                        ,page=1)
    for article in content.get('articles',[]):
        print (article.get('url'))
        sendMsg(chat_id, article.get('url'))
    

def sendMsg(chat_id, content):
        bot.sendMessage(chat_id, content)

TOKEN = os.environ['telegramtoken'] 
bot = telepot.Bot(TOKEN)
MessageLoop(bot, listen).run_as_thread()

while True:
    pass
