# telegram info bot

mkdir telegram_info_bot

cd telegram_info_bot

apt install python3.11-venv

python3 -m venv custom_bot_env

source custom_bot_env/bin/activate

pip install python-telegram-bot

python3 info_bot.py