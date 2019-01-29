from telegram.ext import Filters


def admin(bot, update):
    if Filters.group(update.message):
        admins = bot.get_chat_administrators(update.message.chat.id)
        mention = ''
        for users in reversed(admins):
            mention += users.user.mention_html() + '\n'
        bot.send_message(chat_id=update.message.chat.id,
                         text=mention,
                         parse_mode='HTML')
