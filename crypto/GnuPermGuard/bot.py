import telebot, logging, gnupg
from config import TG_TOKEN
from GnuPermGuard import encrypt_flag

bot = telebot.TeleBot(TG_TOKEN)
telebot.logger.setLevel(logging.DEBUG)

@bot.message_handler(commands=['start', 'help'])
def help(message):
    help_text = '''Hi, lets be more secure. I need your key now in armored format'''
    bot.reply_to(message, help_text)

@bot.message_handler(func=lambda m: True)
def answer(message):
    key_heading = '-----BEGIN PGP PUBLIC KEY BLOCK-----'
    key_ending  = '-----END PGP PUBLIC KEY BLOCK-----'

    if message.text.startswith(key_heading) and message.text.endswith(key_ending):
        ctext = encrypt_flag(message.text)
        bot.reply_to(message, ctext)
    else:
        bot.reply_to(message, "I said I need your key first!!!")


def main_loop():
    bot.polling(True)
    while 1:
        time.sleep(0.3)


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print('\nExiting by user request.\n')
        sys.exit(0)
