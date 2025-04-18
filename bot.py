from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, Application
import os

YOUR_TOKEN = "7854424887:AAGa42aSgHDInjkWMuVknJuRugQSpB2QtTY" 
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

    # Set a webhook URL
    webhook_url = os.getenv('WEBHOOK_URL')  # Set this in Koyeb's environment variables
    application.run_webhook(listen='0.0.0.0', port=int(os.getenv('PORT', '8443')), url_path='7854424887:AAGa42aSgHDInjkWMuVknJuRugQSpB2QtTY')
    application.bot.set_webhook(f"{webhook_url}/{YOUR_TOKEN}")

if __name__ == '__main__':
    main()
    
