import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Токен бота и ID канала (замени на свой)
TOKEN = "7747654844:AAFksU8Tlq03TpzJtUzvhI0ytPxB5kdsBrY"
CHANNEL_ID = "@SmartAICash"  # Укажи @юзернейм своего канала

# Включаем логирование
logging.basicConfig(level=logging.INFO)
print("Бот запущен!")

# Функция обработки команды /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "👋 Привет! Я помогаю автоматизировать продажи через Telegram-ботов.\n"
        "Напишите сообщение, и я отправлю его в наш канал!"
    )

# Функция пересылки сообщений в канал
async def forward_to_channel(update: Update, context: CallbackContext):
    message = update.message.text  # Получаем текст сообщения
    user = update.message.from_user  # Получаем данные пользователя

    # Текст для канала
    text_to_send = f"📩 Новое сообщение от @{user.username}:\n\n{message}"

    # Отправляем в канал
    await context.bot.send_message(chat_id=CHANNEL_ID, text=text_to_send)

# Функция ручной проверки (если пересылка не работает)
async def send_test(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=CHANNEL_ID, text="🔧 Тестовое сообщение от бота!")

# Основная функция запуска бота
def main():
    app = Application.builder().token(TOKEN).build()

    # Добавляем обработчики команд
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("send", send_test))  # Проверка работы
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_channel))  # Пересылка сообщений

    # Запускаем бота (polling)
    print("Бот готов к работе!")
    app.run_polling()

if __name__ == "__main__":
    main()
