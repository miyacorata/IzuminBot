# coding: utf-8

from slackbot.bot import listen_to

@listen_to('進捗')
def erai(message):
    message.reply('えらい！')

@listen_to('^(.*)(や(る|り)|する|します)')
def fight(message,something,tmp):
    message.reply('{0}やるんだね、頑張って！'.format(something))

@listen_to('つらい')
def tsurai(message):
    message.reply('大丈夫、きっとできるよ...！')
