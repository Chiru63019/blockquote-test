from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import random

# Function to handle the /quote command
def quote(update: Update, context: CallbackContext) -> None:
    quotes = [
        "The only limit to our realization of tomorrow is our doubts of today.",
        "Life is 10% what happens to us and 90% how we react to it.",
        "The best way to predict the future is to create it.",
        "Success is not how high you have climbed, but how you make a positive difference to the world."
    ]
    selected_quote = random.choice(quotes)
    update.message.reply_text(selected_quote)

def main() -> None:
    # Replace 'YOUR_TOK' with your bot's token
    updater = Updater("7854424887:AAGa42aSgHDInjkWMuVknJuRugQSpB2QtTY")

    # Register the command handler
    updater.dispatcher.add_handler(CommandHandler("quote", quote))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
  
