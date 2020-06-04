# python_movie_crawler
> 파이썬을 활용한 영화 예매 오픈 알리미 서비스

[참고강의](https://www.inflearn.com/course/%EC%98%81%ED%99%94%EC%98%88%EB%A7%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC/lecture/20865)


## 1. pyvenv를 활용한 내장 가상환경 설정

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




## ETC
git 최신 commit 삭제

    (venv) minkj1992@minkj1992-900X5L:~/code/python_movie_crawler$ git reset HEAD^

