import telebot

TOKEN = "надо свой токен"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот, давай начнем!")

@bot.message_handler(commands=['palindrom'])
def palindrom(message):
    words = message.text.split()[1:]
    reversed_words = [word[::-1] for word in words]
    reversed_text = ' '.join(reversed_words)
    bot.send_message(message.chat.id, f"Перевернутые слова: {reversed_text}")


@bot.message_handler(commands=['caps'])
def caps(message):
    text = ' '.join(message.text.split()[1:])
    caps_text = text.upper()
    bot.send_message(message.chat.id, f"Текст   в заглавных буквах: {caps_text}")


@bot.message_handler(commands=['letter'])
def letter(message):
    vowels = 'aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ'
    text = ' '.join(message.text.split()[1:])
    filtered_text = ''.join(letter for letter in text if letter not in vowels)
    bot.send_message(message.chat.id, f"Текст без гласных букв: {filtered_text}")

bot.polling()
