# (SIXMEN))
- 코로나로 지친 사람들을 위한 맞춤형 비대면 극장 커뮤니티 서비스


## 프로젝트 구성 안내

* 로그인 아웃

* 선호 하는 ott 컨텐츠 장르 분석 및 사용자 input(연령, 나이, ott 이용시간대)에 따른 데이터 분석

* 선호 하는 장르에 맞는 게시판 형태의 커뮤니티 사이트 창설 & 가입 기능

## 1. 프로젝트 소개



  - 모델 : Scikit learn의 Logistic Regression model, One vs Rest model
  - 데이터 1: 방송통계 포털에서 제공하는 2019, 2020 방송 매체 이용행태 조사(개인) - https://www.mediastat.or.kr/kor/contents/ContentsList.html
  - 데이터 2: Kaggle의 전세계 넷플릭스 컨텐츠 데이터 - https://www.kaggle.com/ashishgup/netflix-rotten-tomatoes-metacritic-imdb
  - 기술 스택 : python, pandas, jupyter, javascript, MySQL 등
  - 사용된 라이브러리 : numpy, matplotlib, wordcloud, seaborn, scikit learn 등
  - 서비스 개요 : user input(연령, 성별, ott 이용시간)을 이용한 분석 + 선호하는 장르에 대한 분석 + 그것을 바탕으로한 커뮤니티 사이트 기능

## 2. 프로젝트 목표

**웹서비스의 해결 과제와 인공지능으로 해결하기 위한 방안 논의 (50자 이상)**
  - 프로젝트 아이디어 동기 : 코로나로 인한 규제가 지속되고 있는 상황에서, 비슷한 연령과 취향을 가진 사람들과 함께 영화(ott 컨텐츠)를 시청하고 싶은 사람들의 만남을 주선해주는 커뮤니티 성격을 지닌 웹 사이트
  - 문제를 해결하기 위한 질문 : 연령, 성별 등의 요소가 선호하는 영화 장르와 밀접한 관련이 있을까?


## 3. 프로젝트 기능 설명


  - 유저 관리 기능
  - user input (연령, 나이, 성별, ott 이용시간대, 마음에 드는 영화)를 바탕으로 user가 선호하는 영화을 알려주며 
  - user가 선호하는 영화를 연령별, 성별별로 선호도(평점)을 분석하여 알려줌
  - 다른 이용자들의 연령별, 성별별 ott 이용시간을 분석하여 알려줌
  - user가 선호하는 ott 컨텐츠 장르를 좋아하는 사람들이 모인 커뮤니티 게시판으로 이동시켜준 후
  - user가 원하는 커뮤니티에 창설 / 가입 하여 친목 도모 가능
  - 그 외
   - scikit learn 모델을 이용하여 user에게 연령, 나이 ott 이용시간대의 값만을 받았을 경우 평균 70%의 확률로 성별을 예측하였고
   - user에게 연령, 나이, 성별, ott 주중(or주말) 이용시간대 값들을 받았을 경우 <br>
    8개의 카테고리 값을 가지고 있는 ott 주말(or주중) 이용시간대를 50%의 확률로 예측함 <br>
    그러나 해당 기능이 프로젝트의 성격과 맞지 않아 제외

## 4. 프로젝트 구성도
  - https://www.figma.com/file/tKOBvF55UphOw4npydEWBw/Elice%3A-%EC%8B%9D%EC%8A%A4%EB%A7%A8?node-id=219%3A2



## 5. 프로젝트 팀원 역할 분담
| 이름 | 담당 업무 |
| ------ | ------ |
| 김민석 | 백엔드 개발 |
| 김소령 | 프론트엔드/데이터분석 |
| 이서윤 | 백엔드 개발 |
| 이영민 | 데이터분석 |
| 장훈 | 프론트엔드 |

### 데이터분석 파트의 git은 https://kdt-gitlab.elice.io/003-part3-ottservice/team6/data-analysis

**멤버별 responsibility**

1. 팀장

- 기획 단계: 구체적인 설계와 지표에 따른 프로젝트 제안서 작성
- 개발 단계: 팀원간의 일정 등 조율 + 프론트 or 백엔드 or 인공지능 개발
- 수정 단계: 기획, 스크럼 진행, 코치님 피드백 반영해서 수정, 발표 준비

2. 프론트엔드

- 기획 단계: 큰 주제에서 문제 해결 아이디어 도출, 와이어프레임 작성
- 개발 단계: 와이어프레임을 기반으로 구현, 인공지능 학습 결과 시각화 담당, UI 디자인 완성
- 수정 단계: 코치님 피드백 반영해서 프론트 디자인 수정

3. 백엔드

- 기획 단계: 데이터셋을 확보하기 위한 데이터베이스 구축, 데이터셋 수집
- 개발 단계: 데이터 베이스 구축 및 API 활용, 웹서비스 사용자의 정보 수집 기능 구현, 인공지능 학습 결과를 활용한 기능 구현
- 수정 단계: 코치님 피드백 반영해서 백엔드 설계/기능 수정

4. 데이터분석

- 기획 단계: 웹 서비스 프로젝트 주제에 맞는 모델 및 알고리즘 설정, 모델과 알고리즘에 적합한 데이터셋 수집
- 개발 단계: 데이터 전처리, 학습 모델 구현, 학습 데이터 가공 및 모델 정밀도 향상
- 수정 단계: 코치님 피드백 반영해서 인공지능 학습 방식 수정


## 6. 버전
  - 프로젝트의 버전 기입

## 7. FAQ
  - 자주 받는 질문 정리
