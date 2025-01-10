from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Словарь для хранения целей пользователей
goals = {}

# Функция для команды /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Привет! Я помогу вам ставить и достигать личные цели. "
        "Используйте команду /addgoal для добавления цели, "
        "и /listgoals для просмотра ваших целей."
    )

# Функция для команды /addgoal
async def add_goal(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id not in goals:
        goals[user_id] = []
    await update.message.reply_text("Напишите вашу цель, и я сохраню её для вас!")

    # Ожидание следующего сообщения для добавления цели
    context.user_data['awaiting_goal'] = True

# Функция для добавления цели из текстового сообщения
async def save_goal(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if context.user_data.get('awaiting_goal'):
        goals[user_id].append(update.message.text)
        context.user_data['awaiting_goal'] = False
        await update.message.reply_text("Цель успешно добавлена!")

# Функция для команды /listgoals
async def list_goals(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if user_id in goals and goals[user_id]:
        goals_text = '\n'.join(f"{idx + 1}. {goal}" for idx, goal in enumerate(goals[user_id]))
        await update.message.reply_text(f"Ваши цели:\n{goals_text}")
    else:
        await update.message.reply_text("У вас пока нет сохраненных целей. Добавьте новую с помощью /addgoal.")

# Основной блок приложения
def main():
    # Создаем приложение
    app = Application.builder().token("ВАШ_ТОКЕН_БОТА").build()

    # Регистрация обработчиков команд
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("addgoal", add_goal))
    app.add_handler(CommandHandler("listgoals", list_goals))

    # Обработчик текстовых сообщений для сохранения целей
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, save_goal))

    # Запуск бота
    app.run_polling()

if __name__ == "__main__":
    main()
