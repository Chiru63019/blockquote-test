#YOUR_TOKEN = "7854424887:AAGa42aSgHDInjkWMuVknJuRugQSpB2QtTY" 
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    quotes = [
        "The only limit to our realization of tomorrow is our doubts of today.",
        "Life is 10% what happens to us and 90% how we react to it.",
        "The best way to predict the future is to create it.",
        "Success is not how high you have climbed, but how you make a positive difference to the world."
    ]
    selected_quote = random.choice(quotes)
    await update.message.reply_text(selected_quote)

def main() -> None:
    application = ApplicationBuilder().token("7854424887:AAGa42aSgHDInjkWMuVknJuRugQSpB2QtTY").build()
    application.add_handler(CommandHandler("quote", quote))

    # Run the bot using polling
    application.run_polling()

if __name__ == '__main__':
    main()
    
