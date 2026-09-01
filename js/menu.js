const form = document.getElementById("recommend-form");
const recommendButton = document.getElementById("recommend-button");

const loadingSection = document.getElementById("loading");
const errorSection = document.getElementById("error-message");
const resultSection = document.getElementById("recommend-result");
const pickContainer = document.getElementById("pick-container");


form.addEventListener("submit", async function (event) {

    event.preventDefault();

    // 1. 사용자가 입력한 값 가져오기
    const people = document.getElementById("people").value;
    const situation = document.getElementById("situation").value;
    const foodType = document.getElementById("food-type").value;
    const cookTime = document.getElementById("cook-time").value;
    const taste = document.getElementById("taste").value;
    const alcohol = document.getElementById("alcohol").value;
    const ingredients = document.getElementById("ingredients").value.trim();


    // 2. 필수 입력값 확인
    if (!people || !situation) {
        showError("누구와 먹는지와 오늘 식사 분위기를 선택해주세요.");
        return;
    }


    // 3. 이전 오류와 결과 숨기기
    hideError();

    resultSection.classList.add("hidden");
    loadingSection.classList.remove("hidden");

    recommendButton.disabled = true;
    recommendButton.textContent = "추천 중...";


    // 4. Python으로 보낼 데이터
    const requestData = {
        people: people,
        situation: situation,
        food_type: foodType,
        cook_time: cookTime,
        taste: taste,
        alcohol: alcohol,
        ingredients: ingredients
    };


    try {

        // 5. Python 백엔드 호출
        const response = await fetch("/api/recommend", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(requestData)
        });


        // 6. 서버 오류 확인
        if (!response.ok) {
            throw new Error("서버에서 오류가 발생했습니다.");
        }


        // 7. Python이 보내준 JSON 받기
        const data = await response.json();


        // 8. 화면에 PICK 출력
        displayPicks(data.picks);


    } catch (error) {

        console.error(error);

        showError(
            "메뉴 추천 중 오류가 발생했습니다. 잠시 후 다시 시도해주세요."
        );


    } finally {

        // 9. 로딩 종료
        loadingSection.classList.add("hidden");

        recommendButton.disabled = false;
        recommendButton.textContent = "오늘 메뉴 골라줘";
    }

});


function displayPicks(picks) {

    // 이전 추천 결과 삭제
    pickContainer.innerHTML = "";


    picks.forEach(function (pick, index) {

        const card = document.createElement("article");

        card.classList.add("pick-card");


        const menuItems = pick.menus
            .map(function (menu) {
                return `<li>🍴 ${menu}</li>`;
            })
            .join("");


        card.innerHTML = `
            <span class="pick-number">
                PICK ${index + 1}
            </span>

            <h3>${pick.title}</h3>

            <ul class="menu-list">
                ${menuItems}
            </ul>

            <div class="pick-info">

                <p>
                    🍶 <strong>술 궁합</strong>
                    ${pick.alcohol_match}
                </p>

                <p>
                    👩‍🍳 <strong>조리 부담</strong>
                    ${pick.difficulty}
                </p>

                <p>
                    🌶️ <strong>맛</strong>
                    ${pick.taste}
                </p>

                <p>
                    💡 <strong>추천 이유</strong><br>
                    ${pick.reason}
                </p>

            </div>
        `;


        pickContainer.appendChild(card);

    });


    resultSection.classList.remove("hidden");


    resultSection.scrollIntoView({
        behavior: "smooth"
    });

}


function showError(message) {

    errorSection.textContent = message;

    errorSection.classList.remove("hidden");

    resultSection.classList.add("hidden");

}


function hideError() {

    errorSection.textContent = "";

    errorSection.classList.add("hidden");

}