from telegram.ext import Filters


def c_admin(bot, update):
    # TODO: Add args for any public group

    if Filters.group(update.message):
        admins = bot.get_chat_administrators(update.message.chat.id)
        mention = ''
        for users in reversed(admins):
            print(users)
            if users.status == 'creator':
                mention += 'Creator: ' + users.user.mention_html() + '\n'
                continue

            # List Permission
            if users.can_change_info is True:
                mention += 'ℹ️'
            else:
                mention += '🌚'
            if users.can_delete_messages is True:
                mention += '🗑️'
            else:
                mention += '🌚'
            if users.can_restrict_members is True:
                mention += '🚫'
            else:
                mention += '🌚'
            if users.can_pin_messages is True:
                mention += '📌'
            else:
                mention += '🌚'
            if users.can_invite_users is True:
                mention += '🔗'
            else:
                mention += '🌚'
            if users.can_promote_members is True:
                mention += '➕'
            else:
                mention += '🌚'

            mention += users.user.mention_html() + '\n'
        bot.send_message(chat_id=update.message.chat.id,
                         text=mention,
                         parse_mode='HTML')
