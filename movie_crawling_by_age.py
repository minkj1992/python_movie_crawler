import requests
from bs4 import BeautifulSoup
from collections import namedtuple

# 15세 또는 19세 영화가 발견시 알림
base_url = "http://www.cgv.co.kr//common/showtimes/iframeTheater.aspx?areacode=02&theatercode=0266&date=20200605&screencodes=&screenratingcode=&regioncode="
target_age = ("grade-15", "grade-19")


def get_movie_title(param):
    return param.find_parent("div", class_="info-movie").select_one("a > strong").get_text().strip()


html = requests.get(base_url)
soup = BeautifulSoup(html.text, "html.parser")

for target in target_age:
    target_movie = soup.select("span." + target)  # select(tag.class)

    if target_movie:
        print("{0}세 영화가 {1}건 발견되었습니다: {2}".format(target[-2:], len(target_movie),[get_movie_title(movie) for movie in target_movie]))

    else:
        print("{}세 영화가 발견되지 않았습니다.".format(target[-2:]))
