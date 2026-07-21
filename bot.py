import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)


TOKEN = os.getenv("TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton(
                "📞 پشتیبانی",
                callback_data="support"
            )
        ],
        [
            InlineKeyboardButton(
                "📂 فروش فایل 1",
                callback_data="file"
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "سلام 👋\n\n"
        "من ربات Smartix هستم 🤖\n"
        "یک ربات هوشمند که به شما کمک می‌کنم.\n\n"
        "یکی از گزینه‌ها را انتخاب کنید 👇",
        reply_markup=reply_markup
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == "support":

        await query.edit_message_text(
            "📞 پشتیبانی:\n\n"
            "@FF_Ranked0011"
        )


    elif query.data == "file":

        await query.edit_message_text(
            "📂 فروش فایل 1\n\n"
            "این بخش به زودی فعال می‌شود 🚀"
        )


def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CallbackQueryHandler(button_handler)
    )

    print("Smartix Started ✅")

    app.run_polling()


if __name__ == "__main__":
    main()
