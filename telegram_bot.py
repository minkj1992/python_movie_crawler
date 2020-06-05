import telegram
import json
import datetime

"""
{
  "token": <telegram bot token>,
  "chat_id" : <telegram chat_id>
}
"""
def init(path=None):
    global config_data
    if path == None:
        raise FileExistsError("파일이 없습니다.")

    with open(path, 'r') as f:
        config_data = json.load(f)


def create_bot():
    global bot
    bot = telegram.Bot(token=config_data["token"])
    return bot


def send_message(text):
    return bot.sendMessage(chat_id=config_data["chat_id"], text=text)


def get_history():
    all_history = [(history.message['chat'], history.message['text']) for history in bot.getUpdates()]
    results = []
    for chat, text in all_history:
        user_id = chat["last_name"] + " " + chat["first_name"]
        message = user_id + ": " + text
        results.append(message)
    return results


path = "./config.json"  # where your telegram config json file located
init(path)
bot = create_bot()
now = datetime.datetime.now()
cur_datetime = now.strftime('%Y-%m-%d %H:%M:%S')

# application -> telegram
print("성공") if send_message("[ " + cur_datetime + " ] " + "제주도 개발자의 테스트입니다.") else print("실패")

# telegram -> application
history = get_history()
print(history)
