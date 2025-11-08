from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Bienvenue sur ARTÉMIS, votre assistant shopping à Kolwezi ! Tape /catalogue pour commencer.")

async def catalogue(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🛍 Catalogue : T-shirts, robes, jeans, chaussures. Tape /commander pour acheter.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("catalogue", catalogue))

print(
app.run_polling()
