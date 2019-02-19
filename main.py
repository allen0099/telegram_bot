import configparser
import logging

from telegram import Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from telegram.utils.request import Request

from command import c_admin, info, ping
from message import m_admin

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
    updater.dispatcher.add_handler(CommandHandler('admin', c_admin))
    updater.dispatcher.add_handler(CommandHandler('info', info))
    updater.dispatcher.add_handler(CommandHandler('ping', ping))

    # Message Handlers
    updater.dispatcher.add_handler(MessageHandler(Filters.regex('@admin'), m_admin))

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
