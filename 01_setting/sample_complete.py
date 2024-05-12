import json
import openai

# response = openai.ChatCompletion.create(
response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt="내가 아는 주찬이는",
    stop=".",
    max_tokens=100,
    n=2,
    temperature=0.5,

    # model="gpt-3.5-turbo",
    # messages=[
    #     {
    #         "role": "user",
    #         "content": "냉면의 원재료를 알려줘"
    #     },
    # ],
    # # max_tokens=100,     # 생성할 문장의 최대 토큰 수
    # temperature=1,      # 생성할 문장의 다양성을 나타내는 매개변수
    # n=2,                # 생성할 문장 수
)

print(json.dumps(response, indent=2, ensure_ascii=False))