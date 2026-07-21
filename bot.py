import os
import threading

from flask import Flask, request

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

TOKEN = os.getenv("TOKEN")

# ---------- Flask ----------
app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return "Bot is running"

@app_flask.route('/verify', methods=['GET', 'POST'])
def verify():
    print("VERIFY DATA:", request.args)
    return "ok"


# ---------- Telegram Bot ----------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("📞 پشتیبانی", callback_data="support")],
        [InlineKeyboardButton("📂 فروش فایل 1", callback_data="file")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "سلام 👋\n\n"
        "من ربات Smartix هستم 🤖\n"
        "یکی از گزینه‌ها را انتخاب کنید 👇",
        reply_markup=reply_markup
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == "support":
        await query.edit_message_text("📞 پشتیبانی:\n\n@FF_Ranked0011")

    elif query.data == "file":
        await query.edit_message_text(
            "📂 فروش فایل 1\n\n"
            "به زودی پرداخت فعال میشه 💳"
        )


def run_bot():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    print("Smartix Started ✅")

    application.run_polling()


def run_web():
    app_flask.run(host="0.0.0.0", port=10000)


# ---------- Run Both ----------
if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    run_web()
