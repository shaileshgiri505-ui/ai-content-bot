import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("8739451946:AAF3iL390QppFZ-LBbv48N2akmBBL7GmW54")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot chal raha hai!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Aapne likha: " + update.message.text)

def main():
    print("===== BOT START HO RAHA HAI =====")
    print("TOKEN VALUE:", TOKEN)

    if TOKEN is None:
        print("ERROR: BOT_TOKEN nahi mila!")
        return

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, echo))

    print("===== BOT RUNNING =====")
    app.run_polling()

if __name__ == "__main__":
    main()
