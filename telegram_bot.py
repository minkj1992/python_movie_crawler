import telegram
import json
import datetime
from movie_crawling_by_age import get_movie_info_by_age
from movie_crawling_by_genre import get_movie_genre_info

"""
{
  "token": <telegram bot token>,
  "chat_id" : <telegram chat_id>
}
"""
AGE_CACHE = {}
GENRE_CACHE = {}


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
cur_datetime = now.strftime('%Y%m%d')

# get data

# 1) age
if AGE_CACHE.get(cur_datetime, -1) == -1:
    result = get_movie_info_by_age()
    if result:
        AGE_CACHE[cur_datetime] = result
        send_message(AGE_CACHE[cur_datetime])

# 2) genre
if GENRE_CACHE.get(cur_datetime, -1) == -1:
    result = get_movie_genre_info()
    if result:
        GENRE_CACHE[cur_datetime] = result
        send_message(GENRE_CACHE[cur_datetime])

# telegram -> application
history = get_history()
print(history)
