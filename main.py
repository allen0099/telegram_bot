import configparser
import logging

from telegram import Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from telegram.utils.request import Request

from command import admins, info, ping, delete_msg
from message import admin

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main(token):
    request = Request(con_pool_size=150)
    bot = Bot(token, request=request)
    updater = Updater(bot=bot, workers=120)

    # Command Handlers
    updater.dispatcher.add_handler(CommandHandler('admins', admins, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler('del', delete_msg))
    updater.dispatcher.add_handler(CommandHandler('info', info))
    updater.dispatcher.add_handler(CommandHandler('ping', ping))

    # Message Handlers
    updater.dispatcher.add_handler(MessageHandler(Filters.regex('@admin'), admin))

    # Error and the others, must at the end
    updater.dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # updater.start_webhook(listen='127.0.0.1',
    #                       port=9900,
    #                       url_path=webhook_url_path)
    # updater.bot.set_webhook(webhook_url=f'https://meow.com/{webhook_url_path}')

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    token = config.get('bot', 'token')
    main(token)
