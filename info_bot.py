from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import json
import os

TELEGRAM_TOKEN = "api:key"  # Replace with your real token
DATA_FILE = "user_data.json"  # File to store user data

OPTIONS = [["Enter Name", "Enter Age", "Enter Work Experience"], ["Get Info"]]
REPLY_MARKUP = ReplyKeyboardMarkup(OPTIONS, one_time_keyboard=False)

# Load existing data from JSON file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            # Convert keys back to integers since JSON stores them as strings
            return {int(k): v for k, v in json.load(f).items()}
    return {}

# Save data to JSON file
def save_data(user_data):
    with open(DATA_FILE, "w") as f:
        json.dump(user_data, f, indent=4)

def start(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    user_data = load_data()
    if user_id not in user_data:
        user_data[user_id] = {"name": None, "age": None, "work_experience": None}
        save_data(user_data)
    update.message.reply_text(
        "Welcome! Choose an option below to set or get your info:",
        reply_markup=REPLY_MARKUP
    )

def handle_message(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    text = update.message.text
    user_data = load_data()
    
    if user_id not in user_data:
        user_data[user_id] = {"name": None, "age": None, "work_experience": None}
    
    if text == "Enter Name":
        update.message.reply_text("Please type your name:")
        context.user_data["next_step"] = "name"
    elif text == "Enter Age":
        update.message.reply_text("Please type your age:")
        context.user_data["next_step"] = "age"
    elif text == "Enter Work Experience":
        update.message.reply_text("Please type your work experience (e.g., '5 years'):")
        context.user_data["next_step"] = "work_experience"
    elif text == "Get Info":
        data = user_data[user_id]
        response = (
            f"Name: {data['name'] or 'Not set'}\n"
            f"Age: {data['age'] or 'Not set'}\n"
            f"Work Experience: {data['work_experience'] or 'Not set'}"
        )
        update.message.reply_text(response, reply_markup=REPLY_MARKUP)
    elif "next_step" in context.user_data:
        step = context.user_data["next_step"]
        user_data[user_id][step] = text
        save_data(user_data)  # Save after updating
        update.message.reply_text(f"{step.replace('_', ' ').title()} set to: {text}", reply_markup=REPLY_MARKUP)
        del context.user_data["next_step"]
    else:
        update.message.reply_text("Please select an option from the menu:", reply_markup=REPLY_MARKUP)

def main() -> None:
    print("Bot is starting...")
    try:
        updater = Updater(TELEGRAM_TOKEN, use_context=True)
        dp = updater.dispatcher
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
        print("Starting polling...")
        updater.start_polling()
        updater.idle()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()