import telebot

bot = telebot.TeleBot('1473474865:AAHwxuOFLyuDALMyOess4OYe7yXL4b0hH0E')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока', 'Я тебя люблю')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAANcX7EfxNqZkVF9jlYW_YPUEix6Y2AAAlAJAAJ5XOIJ9QABNrEAATHzSB4E')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling()