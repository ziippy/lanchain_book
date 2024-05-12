import json
import openai

response = openai.ChatCompletion.create(
    # model="gpt-3.5-turbo",
    model="gpt-4-turbo",
    messages=[
        {
            "role": "user",
            "content": "냉면의 원재료를 알려줘"
        },
    ],
    # max_tokens=100,     # 생성할 문장의 최대 토큰 수
    temperature=1,      # 생성할 문장의 다양성을 나타내는 매개변수
    n=2,                # 생성할 문장 수
)

print(json.dumps(response, indent=2, ensure_ascii=False))

# response = openai.chat.completions.create(
#     model="gpt-4-turbo",
#     messages=[
#         {
#             "role": "user",
#             "content": "냉면의 원재료를 알려줘"
#         },
#     ],
#     # max_tokens=100,     # 생성할 문장의 최대 토큰 수
#     temperature=1,      # 생성할 문장의 다양성을 나타내는 매개변수
#     n=2,                # 생성할 문장 수
# )
# # print(response)
# # print(response.choices[0].message.content)
# print(response.model_dump_json(indent=2))