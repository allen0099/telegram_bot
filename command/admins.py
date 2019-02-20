from telegram import TelegramError
from telegram.ext import Filters


def admins(bot, update, args):
    if len(args) == 0:
        if Filters.group(update.message):
            admins = bot.get_chat_administrators(update.message.chat.id)
            mention = ''
            for users in reversed(admins):
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
    elif len(args) == 1:
        if args[0].startswith('@') or args[0].startswith('-100'):
            try:
                mention = 'Admins for the group ' + args[0] + '\n'
                admins = bot.get_chat_administrators(args[0])
                for users in reversed(admins):
                    if users.status == 'creator':
                        mention += 'Creator: ' + users.user.mention_html() + '\n'
                        continue
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
            except TelegramError:
                bot.send_message(chat_id=update.message.chat.id,
                                 text="<b>Error!</b> Check your typo again.",
                                 parse_mode='HTML')
        else:
            bot.send_message(chat_id=update.message.chat.id,
                             text="You need pass <b>@groupname</b> or group UID.",
                             parse_mode='HTML')
    else:
        bot.send_message(chat_id=update.message.chat.id,
                         text="Too many arguments, try edit your argument again.")
