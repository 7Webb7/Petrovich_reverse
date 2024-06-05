import telebot
import re

token = ''
bot = telebot.TeleBot(token)

pattern = re.compile(r'\(\d+(?:\s*,\s*\d+)*\)+$')

@bot.message_handler(commands = ['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Приветствую, меня зовут Петрович. Текст перевернуть?")
@bot.message_handler(content_types= 'text')
def handle_reverse(message):
    match = pattern.search(message.text)
    skip_arr = []

    if match:
        matched_numbers = match.group()
        stripped_matched = re.sub(r'[(,)]', '', matched_numbers)

        skip_arr = [int(i) for i in stripped_matched.split()]
        print(skip_arr)

        message.text = message.text[:match.start()].strip()

    mes = message.text
    mes_arr = mes.lower().split()

    for i in range(len(mes_arr)):
        if i + 1 in skip_arr:
            continue
        mes_arr[i] = ''.join(reversed(mes_arr[i]))
    mes_arr = list(reversed(mes_arr))

    mes_arr = ' '.join(mes_arr)
    bot.reply_to(message, mes_arr)







bot.polling(none_stop = True)




