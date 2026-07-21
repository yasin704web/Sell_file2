import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

TOKEN = os.getenv("TOKEN")

# ----------- START -----------
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("📞 پشتیبانی", callback_data="support")],
        [InlineKeyboardButton("📂 فروش فایل 1", callback_data="file1")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        "سلام 👋\n"
        "من ربات Smartix هستم 🤖\n"
        "یک ربات هوشمند که بهتون کمک می‌کنم\n\n"
        "یکی از گزینه‌ها رو انتخاب کن 👇",
        reply_markup=reply_markup
    )

# ----------- BUTTON HANDLER -----------
def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == "support":
        query.edit_message_text(
            "📞 پشتیبانی:\n"
            "@FF_Ranked0011"
        )

    elif query.data == "file1":
        query.edit_message_text(
            "📂 فایل شماره 1\n\n"
            "💰 قیمت: 50 هزار تومان\n\n"
            "برای خرید:\n"
            "1. مبلغ رو کارت به کارت کن\n"
            "2. رسید رو ارسال کن"
        )

# ----------- MAIN -----------
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
