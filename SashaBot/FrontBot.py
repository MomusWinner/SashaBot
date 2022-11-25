import telebot
from Back import Verify

bot = telebot.TeleBot('5929602163:AAGpsT7zULV6z95GbEERjo80i4dW-YI8h_o')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Добрый день, {message.from_user.first_name}. Я помогу вам"
                                      f" разобраться в написании слов с сомнением при написании о/ё.\n"
                                      f"Если вы хотите проверить слово, вам необходимо ввести "
                                      f"его с со знаком '_' в месте сомнения\nПример: ш_л")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    a = Verify(message.text.lower(), 'ё', 'о')
    bot.send_message(message.chat.id, a.correct_word())


bot.infinity_polling()