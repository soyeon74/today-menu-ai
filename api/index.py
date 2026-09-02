import json
import os
from pathlib import Path

import httpx
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel


app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent.parent

CODYSSEY_BASE_URL = "https://copa.codyssey.kr"
MODEL_NAME = "gpt-5-mini"


class MenuRequest(BaseModel):
    people: str
    situation: str
    food_type: str = ""
    cook_time: str = ""
    taste: str = ""
    alcohol: str = ""
    ingredients: str = ""


# -------------------------
# 웹페이지
# -------------------------

@app.get("/")
def home():
    return FileResponse(BASE_DIR / "index.html")

@app.get("/index.html")
def home_page():
    return FileResponse(BASE_DIR / "index.html")


@app.get("/menu.html")
def menu_page():
    return FileResponse(BASE_DIR / "menu.html")


@app.get("/about.html")
def about_page():
    return FileResponse(BASE_DIR / "about.html")


@app.get("/css/style.css")
def style_css():
    return FileResponse(BASE_DIR / "css" / "style.css")


@app.get("/js/menu.js")
def menu_js():
    return FileResponse(BASE_DIR / "js" / "menu.js")


# -------------------------
# AI 메뉴 추천
# -------------------------

@app.post("/api/recommend")
def recommend_menu(request: MenuRequest):

    api_key = os.getenv("CODYSSEY_API_KEY")

    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="CODYSSEY_API_KEY 환경변수가 설정되지 않았습니다."
        )

    prompt = f"""
당신은 사용자의 식사 상황과 취향을 분석하여
오늘 먹기 좋은 '한 상 차림'을 추천하는 AI 메뉴 큐레이터입니다.

사용자 조건은 다음과 같습니다.

- 함께 먹는 사람: {request.people}
- 식사 상황: {request.situation}
- 선호 음식 종류: {request.food_type or "상관없음"}
- 가능한 조리 시간: {request.cook_time or "상관없음"}
- 원하는 맛: {request.taste or "상관없음"}
- 함께 마실 술: {request.alcohol or "없음 또는 상관없음"}
- 보유 재료: {request.ingredients or "특별히 없음"}

다음 규칙을 반드시 지켜주세요.

1. 서로 다른 스타일의 한 상을 정확히 3개 추천합니다.
2. 각 PICK에는 함께 먹기 좋은 메뉴를 최소 3개 포함합니다.
3. 메인요리만 3개 나열하지 말고 메인·국물·반찬·안주 등이 조화를 이루게 구성합니다.
4. 사용자가 입력한 음식 종류, 맛, 조리시간, 술, 보유재료를 최대한 반영합니다.
5. 세 가지 PICK이 서로 지나치게 비슷하지 않게 합니다.
6. 실제 일반 가정이나 일상 식사에서 준비할 수 있는 메뉴를 추천합니다.
7. 설명은 짧고 이해하기 쉽게 작성합니다.

응답은 반드시 아래 JSON 형식만 사용하세요.
JSON 앞뒤에 설명이나 마크다운 코드블록을 붙이지 마세요.

{{
  "picks": [
    {{
      "title": "한 상 이름",
      "menus": ["메뉴1", "메뉴2", "메뉴3"],
      "alcohol_match": "★★★★★",
      "difficulty": "쉬움 또는 보통 또는 어려움",
      "taste": "맛 특징",
      "reason": "추천 이유"
    }},
    {{
      "title": "한 상 이름",
      "menus": ["메뉴1", "메뉴2", "메뉴3"],
      "alcohol_match": "★★★★☆",
      "difficulty": "보통",
      "taste": "맛 특징",
      "reason": "추천 이유"
    }},
    {{
      "title": "한 상 이름",
      "menus": ["메뉴1", "메뉴2", "메뉴3"],
      "alcohol_match": "★★★☆☆",
      "difficulty": "쉬움",
      "taste": "맛 특징",
      "reason": "추천 이유"
    }}
  ]
}}
"""

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": "당신은 식사 메뉴 조합을 추천하는 전문 AI입니다."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        with httpx.Client(timeout=30.0) as client:
            response = client.post(
                f"{CODYSSEY_BASE_URL}/v1/chat/completions",
                headers=headers,
                json=payload
            )

        response.raise_for_status()

    except httpx.TimeoutException:
        raise HTTPException(
            status_code=504,
            detail="AI 응답 시간이 너무 오래 걸렸습니다."
        )

    except httpx.HTTPStatusError as error:
        print("Codyssey API 오류:", error.response.text)

        raise HTTPException(
            status_code=502,
            detail="AI 서비스 호출 중 오류가 발생했습니다."
        )

    except httpx.RequestError as error:
        print("네트워크 오류:", str(error))

        raise HTTPException(
            status_code=502,
            detail="AI 서비스에 연결할 수 없습니다."
        )

    try:
        api_result = response.json()

        ai_text = api_result["choices"][0]["message"]["content"]

        ai_text = ai_text.strip()

        # AI가 실수로 ```json 코드블록을 붙였을 경우 제거
        if ai_text.startswith("```json"):
            ai_text = ai_text[7:]

        if ai_text.startswith("```"):
            ai_text = ai_text[3:]

        if ai_text.endswith("```"):
            ai_text = ai_text[:-3]

        result = json.loads(ai_text.strip())

    except (KeyError, IndexError, json.JSONDecodeError) as error:
        print("AI 응답 해석 오류:", str(error))
        print("AI 원본 응답:", response.text)

        raise HTTPException(
            status_code=502,
            detail="AI의 추천 결과를 해석하지 못했습니다."
        )

    # 결과 기본 검증
    picks = result.get("picks")

    if not isinstance(picks, list) or len(picks) != 3:
        raise HTTPException(
            status_code=502,
            detail="AI가 올바른 개수의 추천을 생성하지 못했습니다."
        )

    for pick in picks:
        menus = pick.get("menus", [])

        if not isinstance(menus, list) or len(menus) < 3:
            raise HTTPException(
                status_code=502,
                detail="AI 메뉴 구성이 올바르지 않습니다."
            )

    return result