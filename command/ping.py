import time
from datetime import datetime

from telegram.ext import run_async


@run_async
def ping(bot, update):
    d_time = round(time.time() - datetime.timestamp(update.message.date), 2)
    update.message.reply_text(f'Response Time: {d_time}')
