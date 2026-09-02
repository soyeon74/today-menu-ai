# 🍽️ 오늘 뭐 먹지 AI

> **메뉴 하나가 아니라, 오늘 먹고 싶은 한 상을 골라드립니다.**

사용자의 식사 상황과 취향을 AI가 분석하여  
서로 어울리는 메뉴로 구성된 **3가지 한 상 차림**을 추천하는 웹서비스입니다.

🌐 배포 서비스  
https://today-menu-ai.vercel.app

💻 GitHub  
https://github.com/soyeon74/today-menu-ai


---

## 1. 프로젝트 소개

매일 반복되는 고민 중 하나는

> "오늘 뭐 먹지?"

입니다.

기존 메뉴 추천은 음식 하나를 무작위로 추천하거나
단순 메뉴 목록을 보여주는 경우가 많습니다.

**오늘 뭐 먹지 AI**는 음식 하나를 추천하는 것이 아니라,

- 누구와 먹는지
- 어떤 상황에서 먹는지
- 어떤 종류의 음식을 원하는지
- 조리 가능한 시간
- 원하는 맛
- 함께 마실 술
- 현재 가지고 있는 재료

등을 종합하여 AI가 **한 끼 전체의 조합**을 추천합니다.


---

## 2. 핵심 기능

### 🤖 AI 맞춤 한 상 추천

사용자가 입력한 조건을 AI가 분석하여
서로 다른 스타일의 **3가지 PICK**을 추천합니다.

각 PICK에는 최소 3개의 메뉴가 포함됩니다.

예:

```text
PICK 1. 매콤한 집밥 한 상

🍴 제육볶음
🍴 된장찌개
🍴 계란말이

술 궁합: ★★★★☆
조리 부담: 보통
맛: 매콤 · 구수 · 담백

추천 이유:
매콤한 제육볶음과 구수한 된장찌개,
부드러운 계란말이가 잘 어울리는 집밥 구성입니다.
```


### 🍚 메뉴 하나가 아닌 '한 상' 추천

단순히 메인요리 3개를 나열하지 않고

- 메인요리
- 국물
- 반찬
- 안주

등이 서로 조화를 이루도록 구성합니다.


### 🔍 메뉴별 레시피 검색

AI가 추천한 각 메뉴에는 **레시피 검색 버튼**이 제공됩니다.

버튼을 누르면 해당 음식의 레시피를 바로 검색할 수 있습니다.

예:

```text
🍴 제육볶음       🔍 레시피 검색
🍴 된장찌개       🔍 레시피 검색
🍴 계란말이       🔍 레시피 검색
```


### 📱 모바일 반응형 UI

PC뿐 아니라 스마트폰에서도 사용할 수 있도록
반응형 화면을 구현했습니다.

화면 크기에 따라 메뉴, 입력폼, 추천 카드,
레시피 검색 버튼 등이 자동으로 재배치됩니다.


### ⏳ 로딩 및 오류 처리

AI가 추천을 생성하는 동안 로딩 상태를 표시합니다.

또한 다음과 같은 상황에 대한 오류 처리를 구현했습니다.

- API 환경변수가 설정되지 않은 경우
- AI API 응답 시간이 초과된 경우
- AI 서비스 연결 오류
- AI가 올바른 JSON을 반환하지 않은 경우
- 추천 PICK 개수가 잘못된 경우
- PICK의 메뉴가 3개 미만인 경우


---

## 3. 페이지 구성

서비스는 총 3개의 주요 페이지로 구성되어 있습니다.

### HOME

서비스의 목적과 주요 기능을 소개합니다.

### 메뉴 추천

사용자가 식사 조건을 입력하고
AI 추천 결과를 확인하는 핵심 페이지입니다.

### ABOUT

서비스를 만든 이유와
AI 추천 방식 및 주요 기능을 설명합니다.


---

## 4. AI 입력 정보

사용자는 다음 정보를 입력할 수 있습니다.

| 입력 항목 | 설명 |
|---|---|
| 함께 먹는 사람 | 혼자, 가족, 친구 등 |
| 식사 상황 | 일반 식사, 특별한 식사 등 |
| 음식 종류 | 한식, 중식 등 선호 음식 |
| 조리 시간 | 사용 가능한 조리 시간 |
| 원하는 맛 | 매콤, 담백 등 |
| 함께 마실 술 | 식사와 함께할 술 |
| 보유 재료 | 현재 가지고 있는 재료 |


---

## 5. AI 출력 정보

AI는 정확히 **3개의 PICK**을 생성합니다.

각 PICK에는 다음 정보가 포함됩니다.

- 한 상 이름
- 최소 3개의 메뉴
- 술 궁합
- 조리 난이도
- 맛 특징
- 추천 이유


---

## 6. AI 응답 구조

AI 응답은 화면에서 안정적으로 처리할 수 있도록
JSON 형식을 사용합니다.

```json
{
  "picks": [
    {
      "title": "매콤한 집밥 한 상",
      "menus": [
        "제육볶음",
        "된장찌개",
        "계란말이"
      ],
      "alcohol_match": "★★★★☆",
      "difficulty": "보통",
      "taste": "매콤 · 구수 · 담백",
      "reason": "서로 잘 어울리는 집밥 메뉴 구성입니다."
    }
  ]
}
```


---

## 7. 서비스 동작 구조

전체 데이터 흐름은 다음과 같습니다.

```text
사용자
  ↓
HTML 입력폼
  ↓
JavaScript
  ↓
fetch()
  ↓
/api/recommend
  ↓
Python FastAPI
  ↓
Codyssey AI API
  ↓
gpt-5-mini
  ↓
JSON 응답
  ↓
FastAPI
  ↓
JavaScript
  ↓
PICK 1 / PICK 2 / PICK 3
  ↓
화면 출력
```


---

## 8. 기술 스택

### Frontend

- HTML5
- CSS3
- Vanilla JavaScript

### Backend

- Python
- FastAPI
- httpx

### AI

- Codyssey AI API
- gpt-5-mini

### Deployment

- Vercel

### Version Control

- Git
- GitHub


---

## 9. 프로젝트 구조

```text
today-menu-ai
│
├── api
│   └── index.py
│
├── css
│   └── style.css
│
├── docs
│   └── service-plan.md
│
├── images
│
├── js
│   └── menu.js
│
├── about.html
├── index.html
├── menu.html
├── pyproject.toml
├── README.md
├── requirements.txt
└── .gitignore
```


---

## 10. 프론트엔드와 백엔드 분리

AI API Key가 브라우저에 노출되지 않도록
프론트엔드에서 AI API를 직접 호출하지 않습니다.

```text
브라우저
   ↓
/api/recommend
   ↓
Python FastAPI
   ↓
AI API
```

API Key는 서버의 환경변수에서만 읽습니다.


---

## 11. 환경변수

AI API Key는 코드에 직접 작성하지 않습니다.

필요한 환경변수:

```text
CODYSSEY_API_KEY
```

Vercel 배포 환경에서는
Vercel Environment Variables에 등록하여 사용합니다.

> ⚠️ 실제 API Key는 GitHub, README, 코드에 공개하지 않습니다.


---

## 12. 로컬 실행

Python 가상환경을 활성화한 후 필요한 패키지를 설치합니다.

```powershell
pip install -r requirements.txt
```

FastAPI 서버를 실행합니다.

```powershell
uvicorn api.index:app --reload
```

환경에 따라 로컬 실행 방식과
Vercel 배포 환경의 동작에는 차이가 있을 수 있습니다.


---

## 13. Vercel 배포

Vercel CLI를 이용하여 배포할 수 있습니다.

```powershell
vercel --prod
```

배포 완료 후 공개 URL에서 서비스를 사용할 수 있습니다.

🌐 https://today-menu-ai.vercel.app


---

## 14. 개발 중 해결한 문제

### Python 의존성 문제

초기 Vercel 배포 과정에서 서버 함수가 정상 실행되지 않는
`FUNCTION_INVOCATION_FAILED` 오류가 발생했습니다.

원인을 확인한 결과 Python 코드에서 사용하는 `httpx`가
배포 환경의 의존성에 포함되지 않은 것이 문제였습니다.

`pyproject.toml`에 필요한 패키지를 명시하여 해결했습니다.

```toml
dependencies = [
    "fastapi>=0.141.1",
    "httpx>=0.27.0"
]
```


### 페이지 라우팅 문제

메뉴 추천 페이지에서 HOME으로 이동할 때
FastAPI에서 다음 오류가 발생했습니다.

```json
{
  "detail": "Not Found"
}
```

`/index.html` 라우트를 추가하여 해결했습니다.


### 한글 인코딩 문제

ABOUT 페이지 작성 과정에서 한글이 깨지는 문제가 발생했습니다.

파일을 UTF-8 형식으로 다시 작성하고 저장하여 해결했습니다.


---

## 15. 반응형 웹 확인

Chrome 개발자 도구의 모바일 화면 기능을 이용하여
스마트폰 환경에서 UI를 확인했습니다.

확인 항목:

- 페이지가 화면 밖으로 벗어나지 않는지
- 입력폼이 모바일 화면에 맞게 표시되는지
- AI 추천 카드가 자연스럽게 배치되는지
- 메뉴와 레시피 검색 버튼이 겹치지 않는지
- HOME / 메뉴 추천 / ABOUT 이동이 정상적인지


---

## 16. 프로젝트를 통해 학습한 내용

이번 프로젝트를 통해 다음 내용을 직접 구현하고 확인했습니다.

- HTML의 역할과 웹페이지 구조
- CSS를 이용한 화면 디자인
- 반응형 웹 구현
- JavaScript 이벤트 처리
- `fetch()`를 이용한 API 요청
- 프론트엔드와 백엔드의 역할 차이
- Python FastAPI API 구현
- 외부 AI API 연동
- JSON 데이터 처리
- 환경변수를 이용한 API Key 보호
- API 오류 및 timeout 처리
- Git / GitHub 버전 관리
- Vercel 웹서비스 배포
- 실제 배포 환경에서의 오류 분석과 수정


---

## 17. 향후 개선 방향

현재 서비스에서 추가로 발전시킬 수 있는 기능은 다음과 같습니다.

- 추천 결과 저장
- 즐겨찾기 기능
- 실제 레시피 API 연동
- 냉장고 재료 기반 추천 강화
- 음식 이미지 표시
- 영양정보 제공
- 장보기 목록 자동 생성
- 사용자 평가를 반영한 개인화 추천


---

## 18. 서비스 URL

### 배포 서비스

https://today-menu-ai.vercel.app

### GitHub Repository

https://github.com/soyeon74/today-menu-ai


---

## 프로젝트 한 줄 요약

> **오늘 뭐 먹지 AI는 사용자의 식사 상황과 취향을 AI가 분석하여, 메뉴 하나가 아닌 서로 어울리는 3가지 한 상을 추천하는 반응형 웹서비스입니다.**