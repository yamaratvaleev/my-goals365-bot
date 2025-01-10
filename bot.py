from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext

async def start(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я помогу вам ставить и достигать личные цели. Используйте команду /addgoal для начала.")

async def add_goal(update: Update, context: CallbackContext.DEFAULT_TYPE):
    await update.message.reply_text("Напишите вашу цель, и я сохраню её для вас!")

app = ApplicationBuilder().token("8114842914:AAGyYEZUQCenQuf96nooDi4cr7ct5AYlFAI").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("addgoal", add_goal))

if __name__ == "__main__":
    app.run_polling()
