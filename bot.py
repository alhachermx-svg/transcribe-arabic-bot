import os
import telebot

TOKEN = "8473350767:AAG5HeUsBQRML-R_0R20U2lJACSAmJwlSYY"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! أرسل لي أي ملف صوتي أو تسجيل بصوتي وسأقوم بتفريغه إلى نص كاملاً وبدقة.")

@bot.message_handler(content_types=['voice', 'audio'])
def handle_audio(message):
    bot.reply_to(message, "جاري استلام الملف الصوتي ومعالجته...")

if __name__ == "__main__":
    print("Bot is running successfully...")
    bot.infinity_polling()
  
