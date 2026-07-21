import os
import threading
import requests

from flask import Flask, request

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)


TOKEN = os.getenv("TOKEN")

MERCHANT = os.getenv("MERCHANT")
CALLBACK_URL = "https://my-telegram-bot-se9i.onrender.com/verify"


# ---------- Flask ----------

app_flask = Flask(__name__)


@app_flask.route("/")
def home():
    return "Bot is running"


@app_flask.route("/verify", methods=["GET", "POST"])
def verify():
    print("VERIFY DATA:", request.args)
    return "ok"



# ---------- Telegram Bot ----------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("📞 پشتیبانی", callback_data="support")],
        [InlineKeyboardButton("📂 فروش فایل 1", callback_data="file")]
    ]

    await update.message.reply_text(
        "سلام 👋\n\n"
        "من ربات Smartix هستم 🤖\n"
        "یک ربات هوشمند که به شما کمک می‌کنم.\n\n"
        "یکی از گزینه‌ها را انتخاب کنید 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()


    if query.data == "support":

        await query.edit_message_text(
            "📞 پشتیبانی:\n\n@FF_Ranked0011"
        )


    elif query.data == "file":

        data = {
            "api_key": MERCHANT,
            "amount": 160000,
            "callback_uri": CALLBACK_URL
        }

        response = requests.post(
            "https://nextpay.org/nx/gateway/token",
            json=data
        )

        result = response.json()

        if result.get("trans_id"):

            pay_url = (
                "https://nextpay.org/nx/gateway/payment/"
                + result["trans_id"]
            )

            keyboard = [
                [
                    InlineKeyboardButton(
                        "💳 پرداخت",
                        url=pay_url
                    )
                ]
            ]

            await query.edit_message_text(
                "برای خرید فایل روی پرداخت بزنید 👇",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )

        else:
            await query.edit_message_text(
                "❌ خطا در ساخت پرداخت"
            )



def run_bot():

    application = Application.builder().token(TOKEN).build()

    application.add_handler(
        CommandHandler("start", start)
    )

    application.add_handler(
        CallbackQueryHandler(button_handler)
    )

    print("Smartix Started ✅")

    application.run_polling()



def run_web():

    app_flask.run(
        host="0.0.0.0",
        port=10000
    )



if __name__ == "__main__":

    threading.Thread(
        target=run_bot
    ).start()

    run_web()
