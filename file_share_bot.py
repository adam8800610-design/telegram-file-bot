# file_share_bot.py

import os
from telegram import Update, InputFile
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# BotFather දුන් Token එක
BOT_TOKEN = "8381688712:AAEKwPYShcxEgSGIEbRpLwTspKZnV75Yah4"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hi! මම File Share Bot එක. මට file යවන්න, මම save කරලා share කරන්න දෙනවා.")

# user files receive කරන function
async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await update.message.document.get_file()
    file_path = f"{update.message.document.file_name}"
    await file.download_to_drive(file_path)
    await update.message.reply_text(f"✅ File saved: {file_path}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # commands
    app.add_handler(CommandHandler("start", start))

    # file handler
    app.add_handler(MessageHandler(filters.Document.ALL, handle_file))

    print("🚀 Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
