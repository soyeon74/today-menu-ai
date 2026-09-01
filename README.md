# 🍽️ 오늘 뭐 먹지 AI

> 메뉴 하나가 아니라, 오늘 먹고 싶은 한 상을 골라드립니다.

사용자의 식사 상황, 취향, 조리시간, 술, 보유 재료 등을 입력받아  
AI가 오늘 먹기 좋은 **3가지 한 상 차림**을 추천해주는 웹서비스입니다.

🔗 **배포 서비스**  
https://today-menu-ai.vercel.app

---

## 1. 프로젝트 소개

매일 반복되는 고민 중 하나가 바로  
**"오늘 뭐 먹지?"** 입니다.

단순히 음식 하나를 추천받는 것보다 실제 식사에서는

- 누구와 먹는지
- 어떤 분위기의 식사인지
- 어떤 종류의 음식이 먹고 싶은지
- 조리할 시간이 얼마나 있는지
- 어떤 맛을 원하는지
- 술을 함께 마실지
- 집에 어떤 재료가 있는지

등 여러 조건이 메뉴 선택에 영향을 줍니다.

`오늘 뭐 먹지 AI`는 이러한 조건을 입력받아  
AI가 단순 메뉴 하나가 아닌 **서로 어울리는 음식으로 구성된 한 상 차림 3가지**를 추천하도록 구현한 웹서비스입니다.

---

## 2. 주요 기능

### 🍚 AI 한 상 추천

사용자가 다음 조건을 입력할 수 있습니다.

- 함께 먹는 사람
- 식사 상황
- 선호 음식 종류
- 가능한 조리 시간
- 원하는 맛
- 함께 마실 술
- 보유 재료

입력한 조건은 백엔드 API를 통해 AI에 전달됩니다.

AI는 사용자의 조건을 분석하여 **서로 다른 스타일의 한 상 3개**를 추천합니다.

---

### 🥘 PICK별 최소 3개 메뉴 구성

각 추천은 음식 하나가 아니라 최소 3개의 메뉴로 구성됩니다.

예시:

```text
PICK 1
매콤 제육·김치찌개 푸짐상

🍴 제육볶음
🍴 김치찌개
🍴 상추겉절이 / 파채

🍶 술 궁합 ★★★★★
👩‍🍳 조리 부담 보통
🌶️ 맛 매콤 · 칼칼
💡 추천 이유 ...
메인요리만 여러 개 나열하지 않고
메인·국물·반찬·안주 등이 서로 어울리도록 AI 프롬프트를 설계했습니다.

3. 서비스 화면 구성

웹서비스는 다음 페이지로 구성되어 있습니다.

HOME

서비스의 목적과 주요 기능을 소개합니다.

메뉴추천

사용자가 식사 조건을 선택하고 AI에게 메뉴를 추천받는 핵심 페이지입니다.

ABOUT

서비스의 기획 목적과 AI 추천 방식 등을 소개합니다.

4. AI 처리 흐름
사용자 조건 입력
        ↓
JavaScript
        ↓
fetch("/api/recommend")
        ↓
Vercel Python Serverless Function
        ↓
FastAPI
        ↓
Codyssey AI API
        ↓
gpt-5-mini
        ↓
JSON 형태의 추천 결과
        ↓
FastAPI 응답
        ↓
JavaScript
        ↓
PICK 1~3 화면 출력

프론트엔드와 AI API를 직접 연결하지 않고
Python 백엔드를 거쳐 AI API를 호출하도록 구성했습니다.

이를 통해 API Key가 브라우저에 노출되지 않도록 했습니다.

5. AI 응답 구조

AI에게 자유 형식의 문장을 요청하지 않고
프로그램에서 처리하기 쉬운 JSON 형식으로 응답하도록 설계했습니다.

예시:

{
  "picks": [
    {
      "title": "매콤 제육 한 상",
      "menus": [
        "제육볶음",
        "김치찌개",
        "상추겉절이"
      ],
      "alcohol_match": "★★★★★",
      "difficulty": "보통",
      "taste": "매콤 · 칼칼",
      "reason": "매콤한 음식을 원하는 사용자에게 잘 맞는 구성입니다."
    }
  ]
}

백엔드에서는 AI 응답을 확인하여

PICK이 정확히 3개인지
각 PICK에 메뉴가 최소 3개인지

검증한 후 프론트엔드에 전달합니다.

6. 기술 스택
Frontend
HTML5
CSS3
Vanilla JavaScript
Fetch API
Backend
Python
FastAPI
httpx
Vercel Python Serverless Functions
AI
Codyssey API
gpt-5-mini
OpenAI 호환 Chat Completions 방식
Deployment / Version Control
Vercel
Git
GitHub
7. 프로젝트 구조
today-menu-ai/
│
├── api/
│   └── index.py
│
├── css/
│   └── style.css
│
├── docs/
│   └── service-plan.md
│
├── js/
│   └── menu.js
│
├── index.html
├── menu.html
├── about.html
├── pyproject.toml
├── requirements.txt
├── README.md
└── .gitignore

각 파일의 역할은 다음과 같습니다.

파일	역할
index.html	HOME 화면
menu.html	AI 메뉴추천 화면
about.html	서비스 소개
css/style.css	전체 화면 디자인 및 반응형 UI
js/menu.js	입력값 수집, API 요청, 결과 출력
api/index.py	FastAPI 서버 및 AI API 호출
docs/service-plan.md	서비스 기획서
pyproject.toml	Python 프로젝트 및 의존성 설정
.gitignore	Git 제외 파일 설정
8. 로컬 실행 방법
1) 저장소 복제
git clone https://github.com/soyeon74/today-menu-ai.git
cd today-menu-ai
2) Python 가상환경 생성
python -m venv .venv

Windows PowerShell:

.\.venv\Scripts\Activate.ps1
3) 필요한 패키지 설치
pip install -r requirements.txt
4) API 환경변수 설정

Windows PowerShell:

$env:CODYSSEY_API_KEY="YOUR_API_KEY"

실제 API Key는 소스코드나 GitHub 저장소에 저장하지 않습니다.

5) 개발 서버 실행
fastapi dev api/index.py

실행 후 터미널에 표시되는 로컬 주소를 브라우저에서 열어 확인합니다.

9. 환경변수

프로젝트에서 사용하는 환경변수:

CODYSSEY_API_KEY

AI API Key는 코드에 직접 작성하지 않고 환경변수로 관리합니다.

Vercel Production 환경에서도 동일한 환경변수를 Secret으로 등록하여 사용합니다.

10. 오류 처리

사용자가 서비스를 이용할 때 발생할 수 있는 상황을 고려하여 오류 처리를 구현했습니다.

필수 입력값 누락 확인
AI 추천 중 Loading 표시
API 호출 실패 처리
AI 응답 Timeout 처리
잘못된 AI JSON 응답 처리
PICK 개수 검증
각 PICK의 메뉴 개수 검증

오류 발생 시 사용자가 다시 시도할 수 있도록 안내 메시지를 표시합니다.

11. 반응형 웹

PC뿐 아니라 스마트폰에서도 사용할 수 있도록
CSS Media Query를 활용한 반응형 화면을 적용했습니다.

모바일 환경에서는 화면 크기에 맞춰 콘텐츠와 추천 카드가 배치됩니다.

12. 배포

서비스는 Vercel에 배포했습니다.

🌐 서비스 URL

https://today-menu-ai.vercel.app

GitHub 저장소와 별도로 Vercel Production 환경에서 서비스를 실행합니다.

13. GitHub Repository

📦 GitHub

https://github.com/soyeon74/today-menu-ai

14. 프로젝트를 통해 학습한 내용

이 프로젝트를 구현하면서 다음 내용을 학습했습니다.

HTML의 웹페이지 구조
CSS를 이용한 화면 디자인
JavaScript를 이용한 사용자 입력 처리
fetch()를 이용한 프론트엔드와 백엔드 통신
Python FastAPI를 이용한 API 구현
외부 AI API 호출 방법
JSON 데이터 처리
환경변수를 이용한 API Key 보호
오류 및 Timeout 처리
Vercel Serverless Function 구조
Git을 이용한 버전 관리
GitHub Repository 관리
Vercel을 이용한 실제 웹서비스 배포
로컬 환경과 배포 환경의 차이 및 오류 해결
15. 개발 과정에서 해결한 주요 문제
Python Serverless Function 오류

Vercel 배포 후 다음 오류가 발생했습니다.

500: INTERNAL_SERVER_ERROR
FUNCTION_INVOCATION_FAILED

로컬에서는 정상 작동했지만 Vercel 환경에서 필요한 Python 패키지가 설치되지 않아 발생한 문제였습니다.

pyproject.toml에 필요한 의존성을 명시하여 해결했습니다.

dependencies = [
    "fastapi>=0.141.1",
    "httpx>=0.27.0"
]

이 과정을 통해 로컬에서 설치한 패키지와 실제 배포 서버에서 설치되는 패키지는 별도로 관리해야 한다는 점을 확인했습니다.

16. 향후 개선 아이디어

현재 버전은 과제의 핵심 기능에 집중한 MVP입니다.

향후 다음 기능을 확장할 수 있습니다.

추천 결과 다시 추천하기
선택한 메뉴의 레시피 검색
냉장고 재료 활용도 강화
메뉴 즐겨찾기
이전 추천 기록 저장
알레르기 및 제외 식재료 설정
계절·날씨를 반영한 메뉴 추천
서비스 한 줄 소개

「오늘 뭐 먹지 AI」는 사용자의 식사 상황과 취향을 분석하여 메뉴 하나가 아닌, 서로 어울리는 음식으로 구성된 3가지 한 상을 추천하는 AI 웹서비스입니다.