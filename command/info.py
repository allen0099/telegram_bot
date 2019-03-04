from html import escape

from telegram.ext import run_async, Filters


@run_async
def info(bot, update):
    text = '<code>------Conversation Info------</code>\n' \
        f'Send Time: <code>{update.message.date} +08:00</code>\n' \
        f'Message ID: <code>{update.message.message_id}</code>\n' \
        f'ID: <code>{update.message.chat.id}</code>\n' \
        f'Type: <code>{update.message.chat.type}</code>\n'
    if update.message.chat.title is not None:
        text += f'Title: <code>{escape(update.message.chat.title)}</code>\n'
    if update.message.chat.username is not None:
        text += f'Username: @{update.message.chat.username}\n'
    if update.message.chat.first_name is not None:
        text += f'First Name: <code>{escape(update.message.chat.first_name)}</code>\n'
    if update.message.chat.last_name is not None:
        text += f'Last Name: <code>{escape(update.message.chat.last_name)}</code>\n'

    # Reply info, a `message`
    if Filters.reply(update.message):
        text += '<code>--Reply Info--</code>\n' \
            f'Reply Sent Time: <code>{update.message.reply_to_message.date} +08:00</code>\n' \
            f'Reply to ID: <code>{update.message.reply_to_message.message_id}</code>\n' \
            f'UID: <code>{update.message.reply_to_message.from_user.id}</code>\n' \
            f'Is Bot: <code>{update.message.reply_to_message.from_user.is_bot}</code>\n' \
            f'First Name: <code>{update.message.reply_to_message.from_user.first_name}</code>\n'
        if update.message.reply_to_message.from_user.last_name is not None:
            text += f'Last Name: <code>{update.message.reply_to_message.from_user.last_name}</code>\n'
        if update.message.reply_to_message.from_user.username is not None:
            text += f'Username: @{update.message.reply_to_message.from_user.username}\n'
        if update.message.reply_to_message.from_user.language_code is not None:
            text += f'Language Code: <code>{update.message.reply_to_message.from_user.language_code}</code>\n'

        # Forward info, a `message`
        if Filters.forwarded(update.message.reply_to_message):
            text += '<code>--Forward Info--</code>\n'
            if update.message.reply_to_message.forward_from is not None:
                # Only User Here
                text += f'User Id: <code>{update.message.reply_to_message.forward_from.id}</code>\n' \
                    f'Is Bot: <code>{update.message.reply_to_message.forward_from.is_bot}</code>\n' \
                    f'First Name: <code>{escape(update.message.reply_to_message.forward_from.first_name)}</code>\n'
                if update.message.reply_to_message.forward_from.last_name is not None:
                    text += f'Last Name: <code>{update.message.reply_to_message.forward_from.last_name}</code>\n'
                if update.message.reply_to_message.forward_from.username is not None:
                    text += f'Username: @{update.message.reply_to_message.forward_from.username}\n'
                if update.message.reply_to_message.forward_from.language_code is not None:
                    text += f'Language Code: <code>{update.message.reply_to_message.forward_from.language_code}</code>\n'
            if update.message.reply_to_message.forward_from_chat is not None:
                # Only Channel Here
                text += f'Channel ID: <code>{update.message.reply_to_message.forward_from_chat.id}</code>\n' \
                    f'Channel Name: <code>{escape(update.message.reply_to_message.forward_from_chat.title)}</code>\n'
                if update.message.reply_to_message.forward_from_chat.username is not None:
                    text += f'Channel Username: @{update.message.reply_to_message.forward_from_chat.username}\n'
            if update.message.reply_to_message.forward_from_message_id is not None:
                text += f'Message ID: <code>{update.message.reply_to_message.forward_from_message_id}</code>\n'
            if update.message.reply_to_message.forward_date is not None:
                text += f'Sent Time: <code>{update.message.reply_to_message.forward_date} +08:00</code>\n'
            if update.message.reply_to_message.forward_signature is not None:
                text += f'Channel Sign: <code>{escape(update.message.reply_to_message.forward_signature)}</code>\n'

    # Sender info, a `user`
    if not Filters.private(update.message):
        text += '<code>--Sender Info--</code>\n' \
            f'UID: <code>{update.message.from_user.id}</code>\n' \
            f'First Name: <code>{update.message.from_user.first_name}</code>\n'
        if update.message.from_user.last_name is not None:
            text += f'Last Name: <code>{update.message.from_user.last_name}</code>\n'
        if update.message.from_user.username is not None:
            text += f'Username: @{update.message.from_user.username}\n'
        if update.message.from_user.language_code is not None:
            text += f'Language Code: <code>{update.message.from_user.language_code}</code>\n'

    bot.send_message(chat_id=update.message.chat_id,
                     text=text,
                     parse_mode='HTML')
