from telegram.ext import Filters


def delete_msg(bot, update):
    if Filters.reply(update.message):
        print(update.message.reply_to_message)
        bot.delete_message(chat_id=update.message.chat.id,
                           message_id=update.message.reply_to_message.message_id)
