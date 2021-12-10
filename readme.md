# 커밋별 작업

## 커밋 1, 프로젝트 생성, .gitignore 파일 생성
- django-admin startproject config .
- python manage.py migrate
  - 기본적인 테이블 생성
- python manage.py createsuperuser
  - admin / 메일없음 / 1234 
- https://www.toptal.com/developers/gitignore/api/pycharm,django

## 커밋 2, /pybo/ url에 pybo.views.index 함수 연결

## 커밋 3, Question, Answer 모델생성
- pybo/models.py 수정 후
- python manage.py makemigrations pybo
  - DB에 pybo_question, pybo_answer 테이블 생성을 위한 마이그레이션 하나 생성(0001)
- python manage.py migrate pybo
  - pybo 앱과 관련된, 현재 생성은 되어있지만, 아직 적용되지 않은 모든 마이그레이션이 실행됨
