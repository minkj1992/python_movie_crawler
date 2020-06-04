import requests
from bs4 import BeautifulSoup

base_url = "http://www.cgv.co.kr//common/showtimes/iframeTheater.aspx?areacode=02&theatercode=0266&date=20200605&screencodes=&screenratingcode=&regioncode="
html = requests.get(base_url)

soup = BeautifulSoup(html.text,"html.parser")
raw_movie_list = soup.select("div.info-movie")
movie_list = [movie.select_one("a > strong").get_text().strip() for movie in raw_movie_list]
