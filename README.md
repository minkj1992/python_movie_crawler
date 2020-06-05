# python_movie_crawler
> 파이썬을 활용한 영화 예매 오픈 알리미 서비스

[참고강의](https://www.inflearn.com/course/%EC%98%81%ED%99%94%EC%98%88%EB%A7%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC/lecture/20865)

## 앞으로의 계획
1. 크롤링 
2. 파이썬 OOP
   1. [파이썬 3.2](https://www.inflearn.com/course/%EB%B9%A0%EB%A5%B4%EA%B2%8C-%ED%99%9C%EC%9A%A9-%EA%B0%80%EB%8A%A5%ED%95%9C-%ED%8C%8C%EC%9D%B4%EC%8D%AC-3-2-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D/dashboard)
   2. [파이썬 기초 정리](https://www.inflearn.com/course/%EB%82%98%EB%8F%84%EC%BD%94%EB%94%A9-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B8%B0%EB%B3%B8/dashboard)
3. [asyncIO](https://www.youtube.com/watch?v=qdm2o0JSuXc)
4. [시니어코딩 flask](https://www.youtube.com/watch?v=1CuAJsMz7PA&list=PLEOnZ6GeucBXxloeiT5PaZK2B54FRkIgy)
5. [파이썬으로 서버를 극한까지 끌어다 쓰기](https://www.youtube.com/watch?v=zAvWv_Wi0z0)
6. [파이썬 중급](https://www.inflearn.com/course/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A4%91%EA%B8%89-%EC%9D%B8%ED%94%84%EB%9F%B0-%EC%98%A4%EB%A6%AC%EC%A7%80%EB%84%90)

## 실행 방법
1) `telegram`에 ``
`telegram_bot.py`를 통해 crawling이 시작된다.

## 개발과정

### 1. pyvenv를 활용한 내장 가상환경 설정

`sudo apt-get install -y python3-venv`는 Deppricated된 방식이다.

```bash
minkj1992@minkj1992-900X5L:~/code/python_movie_crawler$ sudo apt-get install -y python3-venv
minkj1992@minkj1992-900X5L:~/code/python_movie_crawler$ sudo apt-get autoremove --purge python3-venv

```

3.6 이상의 방식
```bash
minkj1992@minkj1992-900X5L:~/code/python_movie_crawler$ python3 -m venv ./venv
minkj1992@minkj1992-900X5L:~/code/python_movie_crawler$ ls
README.md  venv
```


실행

    minkj1992@minkj1992-900X5L:~/code/python_movie_crawler$ source ./venv/bin/activate

종료

    (venv) minkj1992@minkj1992-900X5L:~/code/python_movie_crawler$ deactivate 


### Crawler
- `select()`
- `find_parent()`
- `get_text()`
- `find_parent()`
    - `find_parent("div", class_="info-movie")`

`default_location` = "광교 상현 CGV"
`movie_crawling_by_age.py`: 오늘 날짜에 대한 영화목록 중, 15세 이상 영화들을 검색하여 내보내준다.
`movie_crawling_by_genre.py`: 오늘 날짜에 대한 영화목록들과 genre를 보내준다. 

### telegram bot

크롤링 데이터들을 모아서, config.json파일에 기입된 telegram 토큰으로 데이터를 send, get 할 수 있다.
중간에 날짜에 대한 CACHE를 두어 크롤링은 하루에 1번만 진행된다. 

### AWS EC2


## ETC
git 최근 add 취소


git 최신 commit 삭제

    (venv) minkj1992@minkj1992-900X5L:~/code/python_movie_crawler$ git reset HEAD^

