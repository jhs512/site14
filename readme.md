# 커밋별 작업

## 커밋 1, 프로젝트 생성, .gitignore 파일 생성
- django-admin startproject config .
- python manage.py migrate
  - 기본적인 테이블 생성
- python manage.py createsuperuser
  - admin / 메일없음 / 1234 
- https://www.toptal.com/developers/gitignore/api/pycharm,django

## 커밋 2, /pybo/ url에 pybo.views.index 함수 연결

## 커밋 3, Question, Answer 모델생성 후 마이그레이트
- pybo/models.py 수정 후
- python manage.py makemigrations pybo
  - DB에 pybo_question, pybo_answer 테이블 생성을 위한 마이그레이션 하나 생성(0001)
- python manage.py migrate pybo
  - pybo 앱과 관련된, 현재 생성은 되어있지만, 아직 적용되지 않은 모든 마이그레이션이 실행됨

## 커밋 4, Question 테이블의, title 칼럼명 subject로 수정, create_date 칼럼 추가
- python manage.py makemigrations pybo
  - 마이그레이션 0002 생성 
- python manage.py migrate pybo

## 커밋 5, 장고 쉘로 질문과 답변 생성
- python manage.py shell
  - 쉘 진입
- 2번 질문 생성
- 2번 질문에 대한 답변(1번 답변) 생성
- exit()
  - 나가는 명령어

## 커밋 6, 관리자페이지에서 질문과 답변을 한개씩 등록

## 커밋 7, pybo/ URL에서 질문 목록표시