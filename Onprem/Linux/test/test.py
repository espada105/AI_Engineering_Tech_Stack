import json
import random
from pathlib import Path


def normalize(value):
    return "".join(ch for ch in value.lower() if ch.isalnum() or ch.isspace()).strip()


with (Path(__file__).parent / "test.json").open(encoding="utf-8") as file:
    data = json.load(file)

questions = data if isinstance(data, list) else data.get("questions", [])
if not questions:
    raise ValueError("퀴즈 데이터가 비어 있습니다.")

random.shuffle(questions)
score = 0

for idx, item in enumerate(questions, start=1):
    print(f"\n문제 {idx}/{len(questions)}: {item['question']}")
    user_answer = input("답: ").strip()

    correct_answer = normalize(item["answer"])
    user_answer_normalized = normalize(user_answer)

    if user_answer_normalized == correct_answer or user_answer_normalized in correct_answer or correct_answer in user_answer_normalized:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. 정답: {item['answer']}")

print(f"\n최종 점수: {score}/{len(questions)}")

if score <= len(questions)/2:
    print("사람은 아닌듯 ㅇㅇ.. 개에바")
elif score == len(questions):
    print("You are a good person")