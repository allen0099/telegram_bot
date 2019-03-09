from command.misc.chinese_shadow import Simplified, Traditional


def convert(bot, update, args):
    flag = False
    str = ""

    if args == []:
        update.message.reply_text('No Arguments')
        return

    for i in args:
        str += i + " "
    for char in str:
        if char in Simplified:
            flag = True
            break

    if (flag):
        result = _trans(str, Simplified, Traditional)
    else:
        result = _trans(str, Traditional, Simplified)

    update.message.reply_text(result)


def _trans(str, a, b):
    result = ""
    for i in str:
        where_i = a.find(i)
        if where_i == -1:
            result += i
        else:
            result += b[where_i]
    return result
