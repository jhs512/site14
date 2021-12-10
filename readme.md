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

## 커밋 8, 질문목록을 템플릿을 이용해서 출력

## 커밋 9, 질문상세 템플릿을 이용해서 출력

## 커밋 10, 상세페이지 접속시 해당 번호에 해당하는 질문이 없으면 404

## 커밋 11, 상세페이지에 대해서 URL 별칭 사용하기

## 커밋 12, URL 네임스페이스 적용

## 커밋 13, 답변 생성기능 구현

## 커밋 14, static 폴더로 정적파일 서빙, 폰트적용

## 커밋 15, 부트스트랩 4 적용

## 커밋 16, 템플릿 상속