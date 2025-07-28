from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# === CONFIGURATION ===
TOKEN = "7931224055:AAEvH_MLjJNmKxg_ytU0yu0Xpop3Xp7iSsA"
OWNER_ID = 6359368706

# === START COMMAND ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎁 Get Free License Key", callback_data='get_free')],
        [InlineKeyboardButton("💳 Buy License Key", callback_data='buy_key')],
        [InlineKeyboardButton("📊 Accuracy (96.8%)", url='https://poll.mgbt.xyz')],
        [InlineKeyboardButton("🌟 Reviews (639)", url='https://review.mgbt.xyz')],
        [InlineKeyboardButton("🎥 How to Use Guide", url='https://video.mgbt.xyz')],
        [InlineKeyboardButton("💬 Support", url='https://t.me/ssgbots')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Welcome to **MG BOT PRO**\n\n"
        "🚀 AI-powered, high-accuracy trading signals for Quotex.\n"
        "📈 Over *286,427 signals* with *96.8%* accuracy!\n\n"
        "👇 Choose an option below to get started:",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# === CALLBACK HANDLER ===
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "get_free":
        await query.edit_message_text(
            "🎁 **Get Free License Key**\n\n"
            "1️⃣ Create a Quotex account using our referral link:\n"
            "👉 https://market-qx.pro/?lid=1314694\n\n"
            "2️⃣ Deposit *at least $50* and complete verification.\n"
            "3️⃣ Send your *Quotex Account ID* to @ssgbots\n\n"
            "✅ You’ll receive your license key for FREE!\n\n"
            "📩 For help, contact @ssgbots"
        )

    elif query.data == "buy_key":
        await query.edit_message_text(
            "💳 **Buy License Key**\n\n"
            "💰 Price: $24 (One-time)\n\n"
            "📌 Payment Options:\n\n"
            "🔸 Binance Pay:\n"
            "🔹 Pay ID: `171932375` (boter 66)\n\n"
            "🔸 USDT (TRC20):\n"
            "`TTBQWhF3uoBhynYCB2NsGBrrq4hcYxdXUw`\n\n"
            "🔸 USDT (BEP20):\n"
            "`0xa46e2beedc42d61ab6061adc4e9989a5624504da`\n\n"
            "📸 After payment, send a screenshot to @ssgbots\n"
            "🕒 You will receive your license key within *15 minutes*.\n\n"
            "📩 For help, contact @ssgbots"
        )

# === MAIN ===
def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_callback))
    app.run_polling()

if __name__ == "__main__":
    main()
