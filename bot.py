import telebot
TOKEN = "8939138418:AAHEn_b-VoAfzpZ9BzftiGrqt2JP5N4LXUc"
ADMIN = 5827364406
bot = telebot.TeleBot(TOKEN)

def menyu():
    kb = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kb.add("🛍️ Zakaz berish","💰 Narxlar","📏 O'lchamlar","🚚 Yetkazib berish","📋 Katalog","📞 Admin")
    return kb

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id,"Salom! 👗 XITOY SHOP\nXitoydan ayollar va qizlar kiyimlari!\n\nQuyidagi bo'limlardan birini tanlang:",reply_markup=menyu())

@bot.message_handler(func=lambda m: m.text=="💰 Narxlar")
def narx(m):
    bot.send_message(m.chat.id,"💰 Narxlarimiz:\n👗 Ko'ylak: 120-200 ming\n👘 Yubka: 100-150 ming\n🥻 Platye: 180-300 ming\n👚 Bluzka: 90-140 ming\n🧥 Palto: 250-500 ming")

@bot.message_handler(func=lambda m: m.text=="📏 O'lchamlar")
def olcham(m):
    bot.send_message(m.chat.id,"📏 O'lcham jadvali:\nXS=42, S=44, M=46\nL=48, XL=50, XXL=52")

@bot.message_handler(func=lambda m: m.text=="🚚 Yetkazib berish")
def yetkazib(m):
    bot.send_message(m.chat.id,"🚚 Yetkazib berish:\n📍 Toshkent: 1 kunda - 15 000 so'm\n📍 Viloyat: 2-3 kunda - 20 000 so'm\n📍 Xitoydan: 10-14 kun\n\n✅ Click, Payme, Uzcard, Naqd")

@bot.message_handler(func=lambda m: m.text=="📋 Katalog")
def katalog(m):
    bot.send_message(m.chat.id,"📋 Katalog:\n👉 @xitoy_shopN_1\n\nZakaz: 🛍️ Zakaz berish tugmasini bosing!")

@bot.message_handler(func=lambda m: m.text=="📞 Admin")
def admin(m):
    bot.send_message(m.chat.id,"📞 Admin ish vaqti: 09:00-21:00\nSavolingizni yozing, javob beramiz!")
    bot.send_message(ADMIN,f"📞 Admin so'radi!\n👤 {m.from_user.first_name}\n🆔 {m.from_user.id}")

@bot.message_handler(func=lambda m: m.text and m.text.upper().startswith('ZAKAZ'))
def zakaz(m):
    bot.send_message(m.chat.id,"✅ Zakazingiz qabul qilindi!\nAdmin tez javob beradi 😊",reply_markup=menyu())
    bot.send_message(ADMIN,f"🆕 ZAKAZ!\n👤 {m.from_user.first_name}\n🆔 {m.from_user.id}\n📝 {m.text}")

@bot.message_handler(func=lambda m: m.text=="🛍️ Zakaz berish")
def zakaz_info(m):
    bot.send_message(m.chat.id,"📦 Zakaz berish uchun:\n\nZAKAZ yozing, keyin:\n1️⃣ Kiyim nomi\n2️⃣ O'lcham\n3️⃣ Rang\n4️⃣ Telefon\n\nMisol:\nZAKAZ Ko'ylak M qizil +998901234567")

@bot.message_handler(func=lambda m: True)
def javob(m):
    bot.send_message(ADMIN,f"💬 {m.from_user.first_name} ({m.from_user.id}):\n{m.text}")
    bot.send_message(m.chat.id,"✉️ Xabaringiz adminga yetkazildi! Tez javob beramiz 😊",reply_markup=menyu())

bot.infinity_polling()
