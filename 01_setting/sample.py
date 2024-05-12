import json
import openai

response = openai.ChatCompletion.create(
    model="gpt-4-turbo",
    messages=[
        {
            "role": "user",
            "content": "Create an image of a \"한화시스템과 고려대 공과대학은 '인간 중심 인공지능 공동연구센터(HCAI)'를 설립하여 AI 기술과 인재 개발에 협력한다. 이 연구센터는 AI 연구 및 개발, 전문가 양성 프로그램, 학술 활동 등을 진행하며, 한화시스템의 AI 연구원들이 현장에 상주할 예정이다. 초대 센터장은 김성범 교수가 맡으며, 한화시스템은 이를 통해 AI 기술 개발과 사업화를 추진하고, 고려대는 특화된 AI 인재 양성을 목표로 한다. 또한, HCAI는 다양한 기관과의 개방형 협력을 통해 네트워크를 확장할 계획이다.\""
        },
    ]
)

print(json.dumps(response, indent=2, ensure_ascii=False))

# response = openai.chat.completions.create(
#     model="gpt-4-turbo",
#     messages=[
#         {
#             "role": "user",
#             "content": "Create subject of a \"한화시스템과 고려대 공과대학은 '인간 중심 인공지능 공동연구센터(HCAI)'를 설립하여 AI 기술과 인재 개발에 협력한다. 이 연구센터는 AI 연구 및 개발, 전문가 양성 프로그램, 학술 활동 등을 진행하며, 한화시스템의 AI 연구원들이 현장에 상주할 예정이다. 초대 센터장은 김성범 교수가 맡으며, 한화시스템은 이를 통해 AI 기술 개발과 사업화를 추진하고, 고려대는 특화된 AI 인재 양성을 목표로 한다. 또한, HCAI는 다양한 기관과의 개방형 협력을 통해 네트워크를 확장할 계획이다.\" article"
#             # "content": "Create an image of a \"한화시스템과 고려대 공과대학은 '인간 중심 인공지능 공동연구센터(HCAI)'를 설립하여 AI 기술과 인재 개발에 협력한다. 이 연구센터는 AI 연구 및 개발, 전문가 양성 프로그램, 학술 활동 등을 진행하며, 한화시스템의 AI 연구원들이 현장에 상주할 예정이다. 초대 센터장은 김성범 교수가 맡으며, 한화시스템은 이를 통해 AI 기술 개발과 사업화를 추진하고, 고려대는 특화된 AI 인재 양성을 목표로 한다. 또한, HCAI는 다양한 기관과의 개방형 협력을 통해 네트워크를 확장할 계획이다.\""
#         },
#     ]
# )
# # print(response)
# print(response.choices[0].message.content)
# # print(response.model_dump_json(indent=2))

