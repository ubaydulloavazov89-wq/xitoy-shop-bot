import telebot
TOKEN = "8939138418:AAHEn_b-VoAfzpZ9BzftiGrqt2JP5N4LXUc"
ADMIN = 5827364406
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, "Salom! XITOY SHOP 👗\n/narx - Narxlar\nZAKAZ yozing - Zakaz berish")

@bot.message_handler(commands=['narx'])
def narx(m):
    bot.send_message(m.chat.id, "💰 Narxlar:\n👗 Koynak: 120-200 ming\n👘 Yubka: 100-150 ming\n🥻 Platye: 180-300 ming")

@bot.message_handler(func=lambda m: m.text and m.text.upper().startswith('ZAKAZ'))
def zakaz(m):
    bot.send_message(m.chat.id, "✅ Zakazingiz qabul qilindi! Tez javob beramiz 😊")
    bot.send_message(ADMIN, f"🆕 ZAKAZ!\n👤 {m.from_user.first_name}\n🆔 {m.from_user.id}\n📝 {m.text}")

@bot.message_handler(func=lambda m: True)
def javob(m):
    bot.send_message(ADMIN, f"💬 {m.from_user.first_name} ({m.from_user.id}):\n{m.text}")
    bot.send_message(m.chat.id, "✉️ Xabaringiz adminga yetkazildi! Tez javob beramiz 😊")

bot.infinity_polling()
