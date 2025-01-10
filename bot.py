from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Привет! Я помогу вам ставить и достигать личные цели. Используйте команду /addgoal для начала.")

async def add_goal(update: Update, context: CallbackContext):
    await update.message.reply_text("Напишите вашу цель, и я сохраню её для вас!")

app = ApplicationBuilder().token("8114842914:AAGyYEZUQCenQuf96nooDi4cr7ct5AYlFAI").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("addgoal", add_goal))

if __name__ == "__main__":
    app.run_polling()
# Хранилище целей
goals = {}

# Команда для добавления цели
async def add_goal(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    goal = ' '.join(context.args)
    if user_id not in goals:
        goals[user_id] = []
    goals[user_id].append(goal)
    await update.message.reply_text(f'Цель "{goal}" добавлена!')

# Команда для отображения списка целей
async def show_goals(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    user_goals = goals.get(user_id, [])
    if not user_goals:
        await update.message.reply_text('У вас пока нет целей.')
    else:
        goals_text = '\n'.join([f"{i + 1}. {g}" for i, g in enumerate(user_goals)])
        await update.message.reply_text(f'Ваши цели:\n{goals_text}')