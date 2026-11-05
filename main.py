import telebot

from config import token
from logic import Pokemon

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["go"])
def go(message):
    if message.from_user.username not in Pokemon.pokemons:
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")


@bot.message_handler(commands=["info"])
def info(message):
    if message.from_user.username in Pokemon.pokemons():
        pok = Pokemon.pokemons[message.from_user.username]
        bot.reply_to(message.chat.id, pok)


bot.infinity_polling(none_stop=True)
