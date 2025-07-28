import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler, MessageHandler, Filters

OWNER_ID = 6359368706  # @ssgbots

PAYMENT_INFO = """
💰 *Price:* $24

*Available Payment Methods:*

🔸 *USDT TRC20:* `TFRFZgVKv7TQKxJBWEpvCaUKHHwRTkxrSr`
🔸 *USDT BEP20:* `0x211758304df13388f6997099c995dc300f760f04`
🔸 *Bitcoin:* `bc1q63fgffsq4my9zdcqjea6k3l6g8staeynw5wswu`

📸 After payment, send screenshot within 15 minutes.
"""

keyboard = [
    [InlineKeyboardButton("💰 Buy Now", callback_data="buy")],
    [
        InlineKeyboardButton("📊 Accuracy", url="https://poll.mgbt.xyz"),
        InlineKeyboardButton("📝 Reviews", url="https://review.mgbt.xyz")
    ],
    [
        InlineKeyboardButton("📽️ How to Use", url="https://youtu.be/EdxdQyPGP6U?si=EajC4JCsflaj91-7"),
        InlineKeyboardButton("🆘 Support", url="https://t.me/ssgbots")
    ]
]

markup = InlineKeyboardMarkup(keyboard)

# Handle /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "👋 Welcome to *MG BOT PRO*\n\nChoose an option below:",
        parse_mode="Markdown",
        reply_markup=markup
    )

# Handle button clicks
def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == "buy":
        query.message.reply_text(PAYMENT_INFO, parse_mode="Markdown")

# Handle image/screenshot uploads
def handle_photo(update: Update, context: CallbackContext):
    update.message.reply_text("✅ Screenshot received. Please wait while we verify and send your license key...")

    # Notify admin
    context.bot.send_message(
        chat_id=OWNER_ID,
        text=f"📸 Payment screenshot received from @{update.effective_user.username or 'user'}\n"
             f"User ID: {update.effective_user.id}\n\nSend license key with:\n"
             f"`/sendkey {update.effective_user.id} YOUR_LICENSE_KEY`",
        parse_mode="Markdown"
    )

# Admin command to send license
def send_key(update: Update, context: CallbackContext):
    if update.effective_user.id != OWNER_ID:
        return update.message.reply_text("❌ You are not authorized to use this command.")

    try:
        user_id = int(context.args[0])
        license_key = " ".join(context.args[1:])
        context.bot.send_message(chat_id=user_id, text=f"🔑 Your license key: `{license_key}`", parse_mode="Markdown")
        update.message.reply_text("✅ License key sent.")
    except:
        update.message.reply_text("⚠️ Usage: /sendkey USER_ID LICENSE_KEY")

def main():
    TOKEN = os.getenv("BOT_TOKEN")
    if not TOKEN:
        raise Exception("BOT_TOKEN not set in Railway environment variables")

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button_handler))
    dp.add_handler(MessageHandler(Filters.photo, handle_photo))
    dp.add_handler(CommandHandler("sendkey", send_key, pass_args=True))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
