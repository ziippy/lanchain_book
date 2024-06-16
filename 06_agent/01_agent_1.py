from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.chat_models import ChatOpenAI

chat = ChatOpenAI(
    model="gpt-4o",
    temperature=0       # 0 으로 해서 출력의 다양성을 억제
)

tools = load_tools(
    [
        "requests",
    ]
)

agent = initialize_agent(
    tools=tools,
    llm=chat,
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,   # ReAct 방식으로 동작하도록 설정
    verbose=True,
)

# result = agent.run("""아래 URL에 접속해 body 의 items 의 item 에 있는 정보에서 제주도의 날씨를 검색해 답하세요.
# result = agent.run("""아래 URL에 접속해 response > body > items > item[0] 값을 추출한 다음, 그 안에서 '제주도' 또는 'Jeju Island'와 관련된 정보를 검색해 답하세요.
# https://apis.data.go.kr/1360000/VilageFcstMsgService/getWthrSituation?serviceKey=ooM15u1T0bBgJJA7EXBZOxPoiHeX1lbjayGvT2OtK67lXaPTclhwUW1h6P56TvFvGM9LiXtyuv6xVXot3GIJQQ%3D%3D&pageNo=1&numOfRows=1&dataType=JSON&stnId=108
# """)

result = agent.run("""아래 URL에 접속해 도쿄의 날씨를 검색해 한국어로 답하세요.
https://www.jma.go.jp/bosai/forecast/data/overview_forecast/130000.json
""")

print(result)
