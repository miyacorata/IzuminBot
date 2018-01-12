# coding: utf-8


from slackbot.bot import respond_to
from slackbot.bot import listen_to

@listen_to('開発')
def listen_func(message):
    print()
    message.send('えらい！')