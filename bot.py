import logging
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters

# Токен бота
TOKEN = "7747654844:AAFksU8Tlq03TpzJtUzvhI0ytPxB5kdsBrY"

# ID Телеграм-канала (важно, чтобы бот был админом!)
CHANNEL_ID = -1002401430345  

# Включаем логирование
logging.basicConfig(level=logging.INFO)
print("Бот запущен!")

# Функция обработки команды /start
async def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("🛒 Бот для продаж", url="https://t.me/ExpressStoreBot?start")],
        [InlineKeyboardButton("🔥 Бот для OnlyFans", url="https://t.me/contentSellerProBot?start")],
        [InlineKeyboardButton("📩 Связаться с нами", url="https://t.me/ANNAYAV4")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Привет! Я помогу тебе автоматизировать продажи и зарабатывать больше с Telegram-ботами. 🚀\n\n"
        "📌 Демо-версии доступных ботов:\n"
        "🔹 Полная автоматизация продаж\n"
        "🔹 Индивидуальные боты под твой бизнес\n\n"
        "Выбери, какой бот тебе нужен:",
        reply_markup=reply_markup
    )

# Функция пересылки сообщений в канал
async def forward_to_channel(update: Update, context: CallbackContext):
    if update.message.text:
        username = update.message.from_user.username
        message_text = update.message.text

        # Отправка сообщения в канал
        await context.bot.send_message(
            chat_id=CHANNEL_ID,
            text=f"📢 Новое сообщение от @{username}:\n\n{message_text}"
        )

        # Подтверждение пользователю
        await update.message.reply_text("✅ Ваше сообщение отправлено в наш канал!")

# Основная функция запуска бота
def main():
    app = Application.builder().token(TOKEN).build()

    # Добавляем обработчик команды /start
    app.add_handler(CommandHandler("start", start))

    # Добавляем обработчик текстовых сообщений (пересылка в канал)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_channel))

    # Запускаем бота (polling)
    print("Бот готов к работе!")
    app.run_polling()

if __name__ == "__main__":
    main()
