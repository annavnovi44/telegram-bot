import os
import logging
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, CallbackContext

# Вставьте ваш токен от BotFather сюда
TOKEN = "7747654844:AAFksU8Tlq03TpzJtUzvhI0ytPxB5kdsBrY"

# Ссылки на ботов и контакт
SALES_BOT_LINK = "https://t.me/ExpressStoreBot"
ONLYFANS_BOT_LINK = "https://t.me/contentSellerProBot"
CONTACT_LINK = "https://t.me/ANNAYAV4"

# Включаем логирование
logging.basicConfig(level=logging.INFO)
print("Бот запущен!")

# Функция обработки команды /start
async def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("🛒 Бот для продаж", url=SALES_BOT_LINK)],
        [InlineKeyboardButton("🔥 Бот для OnlyFans", url=ONLYFANS_BOT_LINK)],
        [InlineKeyboardButton("✉ Связаться с нами", url=CONTACT_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Привет!\n"
        "Я помогу тебе автоматизировать продажи и зарабатывать больше с Telegram-ботами. 🚀\n\n"
        "📌 Демо-версии доступных ботов:\n"
        "🔹 Полная автоматизация продаж\n"
        "🔹 Индивидуальные боты под твой бизнес\n\n"
        "Выбери, какой бот тебе нужен:",
        reply_markup=reply_markup
    )

# Основная функция запуска бота
def main():
    app = Application.builder().token(TOKEN).build()

    # Добавляем обработчик команды /start
    app.add_handler(CommandHandler("start", start))

    # Запускаем бота (polling)
    print("Бот готов к работе!")
    app.run_polling()

if __name__ == "__main__":
    main()

