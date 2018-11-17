
from http_app import app

app.run('0.0.0.0', debug=True)




# proxy = "http://xNRDkU:WLm8U9@176.107.189.60:8000"
#
# request = Request(proxy_url=proxy)
# bot = telegram.Bot(token='674889120:AAE6gI4t4sa59g2wgMO_aOBQOGgS7unYF9U', request=request)
# updater = Updater(bot=bot)
# world = World()
# dispatcher = updater.dispatcher
#
#
# def main():
#     updater.start_polling()
#     start_handler = CommandHandler('start', start)
#     dispatcher.add_handler(start_handler)
#     echo_handler = MessageHandler(Filters.text, echo)
#     dispatcher.add_handler(echo_handler)
#
#
# def start(bot, update):
#     user = next((user for user in world.users if user.id == update.message.chat_id), None)
#     if user is None:
#         world.add_user(update.message.chat_id, update.message.from_user.username)
#         bot.send_message(chat_id=update.message.chat_id, text="New user")
#     else:
#         bot.send_message(chat_id=update.message.chat_id, text="User exist")
#     # keyboard = ReplyKeyboardMarkup([['12345', 'хуй']])
#
#
# def echo(bot, update):
#     bot.send_message(chat_id=update.message.chat_id, text=update.message.text)
#
#
# if __name__ == '__main__':
#     try:
#         main()
#     except KeyboardInterrupt:
#         exit()
