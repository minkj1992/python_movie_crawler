import requests
import datetime
from bs4 import BeautifulSoup


# 15세 또는 19세 영화가 발견시 알림
def get_movie_info_by_age():
    now = datetime.datetime.now()
    cur_datetime = now.strftime('%Y%m%d')
    base_url = "http://www.cgv.co.kr//common/showtimes/iframeTheater.aspx?areacode=02&theatercode=0266&date=%s&screencodes=&screenratingcode=&regioncode=" % cur_datetime
    target_age = ("grade-15", "grade-19")
    html = requests.get(base_url)
    soup = BeautifulSoup(html.text, "html.parser")

    result = ""
    for target in target_age:
        target_movie = soup.select("span." + target)  # select(tag.class)

        if target_movie:
            matched_movie_titles = [_get_movie_title(movie) for movie in target_movie]
            result += f"{target[-2:]}세 영화가 {len(target_movie)}건 발견되었습니다: {matched_movie_titles}\n"

    return result if result else "현재 상영중인 15세 이상 영화가 존재하지 않습니다."


def _get_movie_title(param):
    return param.find_parent("div", class_="info-movie").select_one("a > strong").get_text().strip()






