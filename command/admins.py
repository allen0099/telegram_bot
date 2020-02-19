from telegram import TelegramError
from telegram.ext import Filters


def sort_key(elem):
    return elem.user.id


def admins(bot, update, args):
    if len(args) == 0:
        if Filters.group(update.message):
            mention = 'Current group:\n'
            creator = None  # Creator is not set now
            administrator = list()  # Administrators is not set now

            # Make sure Creator is not in list
            for u in bot.get_chat_administrators(update.message.chat.id):
                if u.status != 'creator':
                    administrator.append(u)
                else:
                    creator = u  # Set creator

            admins = [creator]  # Make creator in 0
            administrator.sort(key=sort_key)

            for u in administrator:
                admins.append(u)

            for users in admins:
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
        if args[0].startswith('https://t.me/'):
            args[0] = args[0].replace('https://t.me/', '@')
        if args[0].startswith('@') or args[0].startswith('-100'):
            try:
                mention = 'Admins for the group ' + args[0] + '\n'
                creator = None
                administrator = list()

                for u in bot.get_chat_administrators(args[0]):
                    if u.status != 'creator':
                        administrator.append(u)
                    else:
                        creator = u

                admins = [creator]
                administrator.sort(key=sort_key)

                for u in administrator:
                    admins.append(u)

                for users in admins:
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
