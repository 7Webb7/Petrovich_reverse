import telebot

token = ''
bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['start'])
def handle_start(message):
    bot.reply_to(message, "Приветствую, меня зовут Петрович. Текст перевернуть?")
@bot.message_handler(content_types= 'text')
def handle_reverse(message):
    skip_arr = [2, 4]
    mes = message.text
    mes_arr = mes.lower().split()
    mes_arr = list(reversed(mes_arr))
    for i in range(len(mes_arr)):
        if i + 1 in skip_arr:
            continue
        mes_arr[i] = ''.join(reversed(mes_arr[i]))

    mes_arr = ' '.join(mes_arr)
    bot.reply_to(message, mes_arr)







bot.polling(none_stop = True)




