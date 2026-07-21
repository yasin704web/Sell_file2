import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    CallbackContext
)

TOKEN = os.getenv("TOKEN")


def start(update: Update, context: CallbackContext):

    buttons = [
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

    keyboard = InlineKeyboardMarkup(buttons)

    update.message.reply_text(
        "سلام 👋\n\n"
        "من ربات Smartix هستم 🤖\n"
        "یک ربات هوشمند که به شما کمک می‌کنم.\n\n"
        "لطفاً یکی از گزینه‌ها را انتخاب کنید 👇",
        reply_markup=keyboard
    )


def button(update: Update, context: CallbackContext):

    query = update.callback_query
    query.answer()

    if query.data == "support":
        query.edit_message_text(
            "📞 پشتیبانی:\n\n"
            "@FF_Ranked0011"
        )

    elif query.data == "file":
        query.edit_message_text(
            "📂 فروش فایل 1\n\n"
            "به زودی فعال می‌شود 🚀"
        )


def main():

    updater = Updater(
        TOKEN,
        use_context=True
    )

    updater.dispatcher.add_handler(
        CommandHandler("start", start)
    )

    updater.dispatcher.add_handler(
        CallbackQueryHandler(button)
    )

    updater.start_polling()

    print("Smartix is running...")

    updater.idle()


if __name__ == "__main__":
    main()
