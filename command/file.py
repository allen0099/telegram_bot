from telegram.ext import run_async


@run_async
def file(bot, update):
    warning_list = ['application/x-ms-dos-executable', 'application/zip',
                    'application/x-msdownload', 'application/x-rar']
    for i in warning_list:
        if update.message.document.mime_type == i:
            # 執行封鎖等等
            bot.send_message(update.message.chat.id, "WARNING")
