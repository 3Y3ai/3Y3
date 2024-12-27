from telegram import Bot
import time
import threading
from telegram.error import TelegramError

# Telegram configuration
BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"  # The chat ID where you want to send the alert

# Alert message
def generate_alert_message():
    return "Alert: This is an automated alert from your bot."

def send_alert():
    bot = Bot(token=BOT_TOKEN)
    try:
        bot.send_message(chat_id=CHAT_ID, text=generate_alert_message())
        print("Alert sent via Telegram")
    except TelegramError as e:
        print(f"Failed to send alert via Telegram. Error: {e}")

class AlertBot:
    def __init__(self, interval=3600):  # Default to alert every hour
        self.interval = interval

    def run_bot(self):
        while True:
            send_alert()
            time.sleep(self.interval)

if __name__ == "__main__":
    bot = AlertBot(interval=3600)  # Alert every hour
    thread = threading.Thread(target=bot.run_bot)
    thread.start()
