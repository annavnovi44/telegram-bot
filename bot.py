import os
import logging
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Твой токен от BotFather
TOKEN = "7747654844:AAFksU8Tlq03TpzJtUzvhI0ytPxB5kdsBrY"

# Ссылки на демо-версии ботов
DEMO_BOT_STORE = "https://t.me/ExpressStoreBot"
DEMO_BOT_ONLYFANS = "https://t.me/ContentSellerProBot"
CONTACT_ADMIN = "https://t.me/ТВОЙ_ЛОГИН"  # Замени на свой логин Telegram

# Включаем логирование
logging.basicConfig(level=logging.INFO)
print("Бот запущен!")

# Функция обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🛒 Бот для продаж", callback_data="store_bot")],
        [InlineKeyboardButton("🔥 Бот для OnlyFans", callback_data="onlyfans_bot")],
        [InlineKeyboardButton("📩 Связаться с нами", url=CONTACT_ADMIN)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Привет! Я помогу тебе автоматизировать продажи и заработать больше с Telegram-ботами.\n\n"
        "Выбери, какой бот тебе нужен:",
        reply_markup=reply_markup
    )

# Обработка выбора бота
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "store_bot":
        text = f"🛒 Бот для продаж:\n\nЭтот бот автоматизирует заказы и продажи прямо в Telegram.\n\nДемо-версия: [Посмотреть]({DEMO_BOT_STORE})\n\nЧтобы заказать, свяжитесь с нами: [Контакт]({CONTACT_ADMIN})"
    elif query.data == "onlyfans_bot":
        text = f"🔥 Бот для OnlyFans:\n\nЭтот бот помогает моделям продавать контент автоматически.\n\nДемо-версия: [Посмотреть]({DEMO_BOT_ONLYFANS})\n\nЧтобы заказать, свяжитесь с нами: [Контакт]({CONTACT_ADMIN})"
    
    keyboard = [[InlineKeyboardButton("🔙 Назад", callback_data="back")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(text=text, reply_markup=reply_markup, parse_mode="Markdown")

# Обработка возврата в меню
async def back_to_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await start(query, context)

# Основная функция запуска бота
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_click))
    app.add_handler(CallbackQueryHandler(back_to_menu, pattern="back"))

    print("Бот готов к работе!")
    app.run_polling()

if __name__ == "__main__":
    main()
