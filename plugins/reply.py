from slackbot.bot import respond_to

@respond_to('疲れた')
@respond_to('つかれた')
def cheer(message):
    message.reply('ファイト!')

@respond_to('ただいま')
def welcome_back(message):
    message.reply('おかえりなさい')

