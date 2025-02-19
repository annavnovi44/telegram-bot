import os
import logging
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Вставьте ваш токен от BotFather сюда
TOKEN = "7747654844:AAFksU8Tlq03TpzJtUzvhI0ytPxB5kdsBrY"
CHANNEL_ID = "@SmartAICashBot"  # Укажите @юзернейм своего канала
CONTACT_USERNAME = "@ANNAYAV4"  # Ссылка на контакт для связи

# Включаем логирование
logging.basicConfig(level=logging.INFO)
print("Бот запущен!")

# Функция обработки команды /start
async def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("🛒 Бот для продаж", callback_data="sales_bot")],
        [InlineKeyboardButton("🔥 Бот для OnlyFans", callback_data="onlyfans_bot")],
        [InlineKeyboardButton("📩 Связаться с нами", url=f"https://t.me/{CONTACT_USERNAME[1:]}")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Привет! Я помогаю автоматизировать продажи и зарабатывать больше с Telegram-ботами. 🚀\n\n"
        "📌 Демо-версии доступных ботов:\n"
        "🔹 Полная автоматизация продаж\n"
        "🔹 Индивидуальные боты под твой бизнес\n\n"
        "Выбери, какой бот тебе нужен:",
        reply_markup=reply_markup
    )

# Функция обработки сообщений и их пересылки в канал
async def forward_to_channel(update: Update, context: CallbackContext):
    message = update.message.text
    user = update.message.from_user

    text_to_send = f"📩 Новое сообщение от @{user.username}:\n\n{message}"

    await context.bot.send_message(chat_id=CHANNEL_ID, text=text_to_send)

# Функция обработки нажатий на кнопки
async def button_click(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    if query.data == "sales_bot":
        await query.message.reply_text(
            "🛍️ **Бот для продаж**:\nЭтот бот автоматизирует заказы и продажи прямо в Telegram.\n\n"
            "Демо-версия: [Посмотреть](https://t.me/ExpressStoreBot)\n"
            f"Чтобы заказать, свяжитесь с нами: {CONTACT_USERNAME}",
            parse_mode="Markdown"
        )
    elif query.data == "onlyfans_bot":
        await query.message.reply_text(
            "🔥 **Бот для OnlyFans**:\nЭтот бот помогает моделям автоматизировать продажи контента и привлекать подписчиков.\n\n"
            "Демо-версия: [Посмотреть](https://t.me/contentSellerProBot)\n"
            f"Чтобы заказать, свяжитесь с нами: {CONTACT_USERNAME}",
            parse_mode="Markdown"
        )

# Функция тестовой отправки в канал
async def send_test(update: Update, context: CallbackContext):
    await context.bot.send_message(chat_id=CHANNEL_ID, text="🔧 Тестовое сообщение от бота!")

# Основная функция запуска бота
def main():
    app = Application.builder().token(TOKEN).build()

    # Добавляем обработчики
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("send", send_test))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_channel))
    app.add_handler(MessageHandler(filters.COMMAND, button_click))

    # Запускаем бота
    print("Бот готов к работе!")
    app.run_polling()

if __name__ == "__main__":
    main()
