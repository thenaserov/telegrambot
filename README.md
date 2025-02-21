Telegram Info Bot
A simple Telegram bot that allows users to input their name, age, and work experience, stores the data in a JSON file, and retrieves it on demand. Built with Python and the python-telegram-bot library, this bot runs on a Debian 12 server.

Features
Users can start the bot with /start and see a menu of options.
Options include: "Enter Name", "Enter Age", "Enter Work Experience", and "Get Info".
Data is persistently stored in user_data.json and survives bot restarts.
Designed to run as a background service using systemd.
Requirements
Operating System: Debian 12 (tested on a server environment).
Python: Version 3.11 or higher (Debian 12 default).
Python Libraries:
python-telegram-bot==13.15 (Telegram API interaction).
Telegram Bot Token: Obtain from BotFather on Telegram.
Root Access: Required for installation and service setup (can be adapted for a non-root user).
Internet Access: The server must reach api.telegram.org for bot communication.
Installation
1. Clone or Create the Project

If you’re starting fresh, create the directory and file manually (no repo assumed here):

bash
Wrap
Copy
mkdir /root/telegram_info_bot
cd /root/telegram_info_bot
nano info_bot.py
Paste the bot code (provided separately) into info_bot.py, replacing TELEGRAM_TOKEN with your actual token from BotFather.

2. Set Up a Virtual Environment

Create and activate a virtual environment to isolate dependencies:

bash
Wrap
Copy
cd /root
python3 -m venv custom_bot_env
source custom_bot_env/bin/activate
You’ll see (custom_bot_env) in your prompt.

3. Install Dependencies

With the virtual environment active, install the required library:

bash
Wrap
Copy
pip install python-telegram-bot==13.15
Verify installation:

bash
Wrap
Copy
pip show python-telegram-bot
4. Test the Bot

Run the bot manually to ensure it works:

bash
Wrap
Copy
cd /root/telegram_info_bot
python3 info_bot.py
Expected output: Bot is starting... and Starting polling....
Open Telegram, find your bot (e.g., @YourInfoBot), and send /start. Check if the menu appears and data saves to user_data.json.
Stop with Ctrl+C once tested.

Running as a Service
To keep the bot running persistently on your Debian 12 server, use systemd:

1. Create a Service File

bash
Wrap
Copy
sudo nano /etc/systemd/system/info_bot.service
Add the following:

ini
Wrap
Copy
[Unit]
Description=Telegram Info Bot
After=network.target

[Service]
User=root
WorkingDirectory=/root/telegram_info_bot
ExecStart=/root/custom_bot_env/bin/python3 /root/telegram_info_bot/info_bot.py
Restart=always

[Install]
WantedBy=multi-user.target
User=root: Matches your setup; change to a non-root user if preferred.
ExecStart: Points to the virtual environment’s Python and script location.
Save and exit (Ctrl+O, Enter, Ctrl+X).

2. Enable and Start the Service

bash
Wrap
Copy
sudo systemctl daemon-reload
sudo systemctl enable info_bot.service
sudo systemctl start info_bot.service
3. Check Status

Verify it’s running:

bash
Wrap
Copy
sudo systemctl status info_bot.service
Look for active (running) and logs like Bot is starting....
If it fails, check logs with:
bash
Wrap
Copy
sudo journalctl -u info_bot.service
Usage
In Telegram, start the bot with /start.
Use the menu:
"Enter Name" → Type your name (e.g., "John").
"Enter Age" → Type your age (e.g., "30").
"Enter Work Experience" → Type experience (e.g., "5 years").
"Get Info" → See all your saved data.
Data is saved to /root/telegram_info_bot/user_data.json.
Troubleshooting
Bot Not Responding:
Ensure TELEGRAM_TOKEN is valid.
Check network: ping api.telegram.org.
Review logs: sudo journalctl -u info_bot.service.
ModuleNotFoundError:
Reactivate the virtual environment and reinstall: pip install python-telegram-bot==13.15.
Permission Issues:
Ensure /root/telegram_info_bot/ and user_data.json are writable by the service user (chmod 644 user_data.json if needed).
Notes
Security: Running as root is convenient but less secure. Consider a dedicated user and restricting file permissions.
Data Persistence: user_data.json grows with each new user; consider periodic cleanup for large-scale use.
Enhancements: Add input validation or a database (e.g., SQLite) for scalability.
Explanation

Requirements: Lists the OS, Python version, library, and external needs (token, internet).
Installation: Guides through setting up the environment and testing, matching your /root/custom_bot_env setup.
Service: Matches your server’s paths and user (root), ensuring the bot runs continuously.
Usage/Troubleshooting: Helps users (or you) operate and debug it.
To use this on your server:

Create README.md:
bash
Wrap
Copy
nano /root/telegram_info_bot/README.md
Paste the content above, save, and exit.
Follow its steps to ensure everything’s set up correctly.
Let me know if you need adjustments (e.g., different paths or user)!




plain md file


Here’s a plain .md file version of the README.md without GitHub-flavored Markdown headings (e.g., #) or extra formatting, keeping it simple and compatible with any Markdown viewer. It follows your request for a "plain md file" and matches your Telegram bot project on Debian 12.

Telegram Info Bot

A simple Telegram bot that allows users to input their name, age, and work experience, stores the data in a JSON file, and retrieves it on demand. Built with Python and the python-telegram-bot library, this bot runs on a Debian 12 server.

Features:

Users can start the bot with /start and see a menu of options.
Options include: "Enter Name", "Enter Age", "Enter Work Experience", and "Get Info".
Data is persistently stored in user_data.json and survives bot restarts.
Designed to run as a background service using systemd.
Requirements:

Operating System: Debian 12 (tested on a server environment).
Python: Version 3.11 or higher (Debian 12 default).
Python Libraries:
python-telegram-bot==13.15 (Telegram API interaction).
Telegram Bot Token: Obtain from BotFather on Telegram.
Root Access: Required for installation and service setup (can be adapted for a non-root user).
Internet Access: The server must reach api.telegram.org for bot communication.
Installation:

Clone or Create the Project If you’re starting fresh, create the directory and file manually (no repo assumed here):
text
Wrap
Copy
mkdir /root/telegram_info_bot
cd /root/telegram_info_bot
nano info_bot.py
Paste the bot code (provided separately) into info_bot.py, replacing TELEGRAM_TOKEN with your actual token from BotFather.

Set Up a Virtual Environment Create and activate a virtual environment to isolate dependencies:
text
Wrap
Copy
cd /root
python3 -m venv custom_bot_env
source custom_bot_env/bin/activate
You’ll see (custom_bot_env) in your prompt.

Install Dependencies With the virtual environment active, install the required library:
text
Wrap
Copy
pip install python-telegram-bot==13.15
Verify installation:

text
Wrap
Copy
pip show python-telegram-bot
Test the Bot Run the bot manually to ensure it works:
text
Wrap
Copy
cd /root/telegram_info_bot
python3 info_bot.py
Expected output: Bot is starting... and Starting polling....
Open Telegram, find your bot (e.g., @YourInfoBot), and send /start. Check if the menu appears and data saves to user_data.json.
Stop with Ctrl+C once tested.

Running as a Service:

To keep the bot running persistently on your Debian 12 server, use systemd:

Create a Service File
text
Wrap
Copy
sudo nano /etc/systemd/system/info_bot.service
Add the following:

text
Wrap
Copy
[Unit]
Description=Telegram Info Bot
After=network.target

[Service]
User=root
WorkingDirectory=/root/telegram_info_bot
ExecStart=/root/custom_bot_env/bin/python3 /root/telegram_info_bot/info_bot.py
Restart=always

[Install]
WantedBy=multi-user.target
User=root: Matches your setup; change to a non-root user if preferred.
ExecStart: Points to the virtual environment’s Python and script location.
Save and exit (Ctrl+O, Enter, Ctrl+X).

Enable and Start the Service
text
Wrap
Copy
sudo systemctl daemon-reload
sudo systemctl enable info_bot.service
sudo systemctl start info_bot.service
Check Status Verify it’s running:
text
Wrap
Copy
sudo systemctl status info_bot.service
Look for active (running) and logs like Bot is starting....
If it fails, check logs with:
text
Wrap
Copy
sudo journalctl -u info_bot.service
Usage:

In Telegram, start the bot with /start.
Use the menu:
"Enter Name" → Type your name (e.g., "John").
"Enter Age" → Type your age (e.g., "30").
"Enter Work Experience" → Type experience (e.g., "5 years").
"Get Info" → See all your saved data.
Data is saved to /root/telegram_info_bot/user_data.json.
Troubleshooting:

Bot Not Responding:
Ensure TELEGRAM_TOKEN is valid.
Check network: ping api.telegram.org.
Review logs: sudo journalctl -u info_bot.service.
ModuleNotFoundError:
Reactivate the virtual environment and reinstall: pip install python-telegram-bot==13.15.
Permission Issues:
Ensure /root/telegram_info_bot/ and user_data.json are writable by the service user (chmod 644 user_data.json if needed).
Notes:

Security: Running as root is convenient but less secure. Consider a dedicated user and restricting file permissions.
Data Persistence: user_data.json grows with each new user; consider periodic cleanup for large-scale use.
Enhancements: Add input validation or a database (e.g., SQLite) for scalability.
How to Use It

On your server:
bash
Wrap
Copy
nano /root/telegram_info_bot/README.md
Paste the content above, save, and exit (Ctrl+O, Enter, Ctrl+X).
Follow the instructions to set up or verify your bot.