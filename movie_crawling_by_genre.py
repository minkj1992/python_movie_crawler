import requests
import datetime
import pprint
from bs4 import BeautifulSoup
from collections import namedtuple


def get_movie_genre_info():
    now = datetime.datetime.now()
    cur_datetime = now.strftime('%Y%m%d')
    base_url = "http://www.cgv.co.kr//common/showtimes/iframeTheater.aspx?areacode=02&theatercode=0266&date=%s&screencodes=&screenratingcode=&regioncode=" % cur_datetime
    html = requests.get(base_url)

    soup = BeautifulSoup(html.text, "html.parser")
    raw_movie_list = soup.select("div.info-movie")
    movies = []
    movie_info = namedtuple("movie_info", "title genre")

    # ex) movie_info(title='침입자', genre=['미스터리', '스릴러'])
    for raw_moive in raw_movie_list:
        movie_title = raw_moive.select_one("a > strong").get_text().strip()
        movie_genre = raw_moive.select('i')[0].get_text(separator=',', strip=True).replace("\xa0", '').split(',')
        movies.append(movie_info(movie_title, movie_genre))

    return pprint.pformat(movies) if movies else None
