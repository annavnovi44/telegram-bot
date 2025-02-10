import os
import logging
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, CallbackContext

# Вставьте ваш токен от BotFather сюда
TOKEN = "7747654844:AAFksU8Tlq03TpzJtUzvhI0ytPxB5kdsBrY"
GUMROAD_LINK = "https://novianna.gumroad.com/l/nhmav"

# Включаем логирование
logging.basicConfig(level=logging.INFO)
print("Бот запущен!")

# Функция обработки команды /start
async def start(update: Update, context: CallbackContext):
    keyboard = [[InlineKeyboardButton("💰 Купить гайд", url=GUMROAD_LINK)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Привет! Я помогу тебе заработать с AI.\n"
        "Нажми кнопку ниже, чтобы получить гайд:",
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
