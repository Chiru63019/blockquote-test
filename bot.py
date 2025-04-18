#YOUR_TOKEN = "7854424887:AAGa42aSgHDInjkWMuVknJuRugQSpB2QtTY" 
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

# Function to handle the /quote command
async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    quotes = [
        "<blockquote>The only limit to our realization of tomorrow is our doubts of today.</blockquote>",
        "Life is 10% what happens to us and 90% how we react to it.",
        "The best way to predict the future is to create it.",
        "Success is not how high you have climbed, but how you make a positive difference to the world."
    ]
    selected_quote = random.choice(quotes)
    
    # Format the message as a blockquote using Markdown
    await update.message.reply_text(f"*Quote:*\n`{selected_quote}`", parse_mode='Markdown')

def main() -> None:
    application = ApplicationBuilder().token("7854424887:AAGa42aSgHDInjkWMuVknJuRugQSpB2QtTY").build()

    # Register the command handler for /quote
    application.add_handler(CommandHandler("quote", quote))

    # Start polling for updates
    application.run_polling()

if __name__ == '__main__':
    main()
